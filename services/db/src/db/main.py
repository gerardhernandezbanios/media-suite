# main.py
import uvicorn
from fastapi import FastAPI
from db.logging_config import configure_logging
from db.infrastructure.api.routes import router

def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title="Media Suite DB Service")
    app.include_router(router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("db.main:app", host="0.0.0.0", port=8000, reload=True)
