# services/backend/app/media/application/use_cases/process_job_use_case.py
"""
# 🧩 1. Use case: ProcessJobUseCase

            Responsabilidades:

                Obtener jobs pendientes desde JobPort (carpetas en /incoming).
                Para cada job:
                    Cambiar a processing (mover carpeta a /processing y actualizar status.json).
                    Si hay ZIP:
                        Usar ZipExtractorPort para extraer dentro de la carpeta del job.
                    Para cada fichero:
                        Detectar tipo (media_type_detector.py)
                        Leer EXIF (exif_reader.py)
                        Calcular hash (hasher.py)
                        Decidir  ruta final (media_path_factory.py)
                        Mover a /media/{foto|video}/{YYYY}/{MM}/...
                    Si todo va bien:
                        Actualizar status.json a done
                        Mover carpeta a /done/{job_id} y dejar solo status.json.
                    Si hay error:
                        Actualizar status.json a error con mensaje
                        Mover carpeta a /error/{job_id} manteniendo los ficheros originales.

    Este caso de uso es el corazón del worker.
"""
from pathlib import Path

from media.domain.jobs.job_port import JobPort
from media.domain.jobs.job_status import JobStatus

class ProcessJobUseCase:
    def __init__(
        self,
        job_port: JobPort,
        zip_extractor,
        media_type_detector,
        exif_reader,
        hasher,
        media_path_factory,
    ):
        self.job_port = job_port
        self.zip_extractor = zip_extractor
        self.media_type_detector = media_type_detector
        self.exif_reader = exif_reader
        self.hasher = hasher
        self.media_path_factory = media_path_factory

    def execute(self, job_id: str):
        job = self.job_port.get_job(job_id)

        # 1) Mover a processing
        self.job_port.move_job_to(job_id, JobStatus.PROCESSING)

        job_folder = self.job_port._job_folder(JobStatus.PROCESSING, job_id)

        try:
            # 2) Extraer ZIPs si los hay
            for file in list(job_folder.iterdir()):
                if file.suffix.lower() == ".zip":
                    self.zip_extractor.extract(file, job_folder)
                    file.unlink()  # borrar ZIP tras extraer

            # 3) Procesar cada fichero
            for file in job_folder.iterdir():
                if file.name == "status.json":
                    continue

                media_type = self.media_type_detector.detect(file)
                exif = self.exif_reader.read(file)
                checksum = self.hasher.compute(file)

                final_path = self.media_path_factory.build_path(
                    file=file,
                    media_type=media_type,
                    exif=exif,
                    checksum=checksum,
                )

                final_path.parent.mkdir(parents=True, exist_ok=True)
                file.rename(final_path)

            # 4) Finalizar
            self.job_port.move_job_to(job_id, JobStatus.DONE)

        except Exception as e:
            self.job_port.update_status(job_id, JobStatus.ERROR, str(e))
            self.job_port.move_job_to(job_id, JobStatus.ERROR)
            raise
