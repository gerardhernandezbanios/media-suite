import typer
from deduper.main import build_service
from deduper.infrastructure.config import Config

app = typer.Typer(help="Servicio de deduplicación de imágenes")

@app.command()
def run(year: int, month: int):
    """
    Busca duplicados en IMAGES_ROOT/<year>/<month>.
    """
    folder = Config.IMAGES_ROOT / f"{year}" / f"{month:02d}"

    if not folder.exists():
        typer.echo(f"❌ La carpeta no existe: {folder}")
        raise typer.Exit(code=1)

    service = build_service()
    service.run(folder)

    typer.echo("✔️ Proceso completado.")


if __name__ == "__main__":
    app()
