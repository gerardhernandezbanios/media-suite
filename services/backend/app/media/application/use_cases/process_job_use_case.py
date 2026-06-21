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