#services/backend/main.py
from fastapi import FastAPI
from app.core.events import register_events
from app.core.container import container
from app.media.api.upload import router as upload_router
from app.media.api.media import router as media_router
from app.media.api.albums import router as albums_router

def create_app() -> FastAPI:
    app = FastAPI(title="Media Suite Backend")

    # Routers
    app.include_router(upload_router, prefix="/media")
    app.include_router(media_router, prefix="/media")
    app.include_router(albums_router, prefix="/albums")

    # Startup / Shutdown
    register_events(app)

    return app

app = create_app()
