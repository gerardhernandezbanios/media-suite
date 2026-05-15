#services/backend/app/core/events.py
from fastapi import FastAPI

def register_events(app: FastAPI):

    @app.on_event("startup")
    async def startup():
        print("Backend iniciado")

    @app.on_event("shutdown")
    async def shutdown():
        print("Backend detenido")
