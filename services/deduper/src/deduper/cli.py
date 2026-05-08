import typer
from pathlib import Path

from deduper.main import build_service
from deduper.infrastructure.config import Config

app = typer.Typer(help="Servicio de deduplicación de imágenes")


# ---------------------------------------------------------
# COMANDO PRINCIPAL: RUN
# ---------------------------------------------------------
@app.command()
def run(year: int, month: int = typer.Argument(None)):
    """
    Ejecuta la deduplicación.
    - Si se pasa año y mes → procesa ese mes.
    - Si se pasa solo año → procesa los 12 meses.
    """

    service = build_service()

    # Caso 1: año + mes
    if month is not None:
        folder = Config.IMAGES_ROOT / f"{year}" / f"{month:02d}"

        if not folder.exists():
            typer.echo(f"❌ La carpeta no existe: {folder}")
            raise typer.Exit(code=1)

        typer.echo(f"▶ Procesando {folder}")
        service.run(folder, year, month)
        typer.echo("✔️ Proceso completado.")
        return

    # Caso 2: solo año → procesar 12 meses
    for m in range(1, 13):
        folder = Config.IMAGES_ROOT / f"{year}" / f"{m:02d}"

        if not folder.exists():
            typer.echo(f"⚠ Carpeta no encontrada, se omite: {folder}")
            continue

        typer.echo(f"▶ Procesando {folder}")
        service.run(folder, year, m)

    typer.echo("✔️ Proceso completado para todo el año.")


# ---------------------------------------------------------
# COMANDO: STATS
# ---------------------------------------------------------
@app.command()
def stats(year: int, month: int = typer.Argument(None)):
    """
    Muestra estadísticas de duplicados detectados previamente.
    """

    if month is None:
        typer.echo("📊 Estadísticas por año aún no implementadas.")
        raise typer.Exit()

    dup_dir = Config.DUPLICATES_ROOT / str(year) / f"{month:02d}"

    if not dup_dir.exists():
        typer.echo(f"❌ No existe carpeta de duplicados: {dup_dir}")
        raise typer.Exit()

    files = list(dup_dir.glob("*"))
    typer.echo(f"📊 Duplicados en {year}/{month:02d}: {len(files)} archivos")


# ---------------------------------------------------------
# COMANDO: REPORT
# ---------------------------------------------------------
@app.command()
def report(year: int, month: int = typer.Argument(None)):
    """
    Genera un informe simple de los duplicados detectados.
    """

    if month is None:
        typer.echo("📄 Informe por año aún no implementado.")
        raise typer.Exit()

    dup_dir = Config.DUPLICATES_ROOT / str(year) / f"{month:02d}"

    if not dup_dir.exists():
        typer.echo(f"❌ No existe carpeta de duplicados: {dup_dir}")
        raise typer.Exit()

    typer.echo(f"📄 Informe de duplicados para {year}/{month:02d}")
    typer.echo("--------------------------------------------------")

    for f in dup_dir.glob("*"):
        typer.echo(f"- {f.name}")

    typer.echo("--------------------------------------------------")
    typer.echo("✔️ Informe completado.")
