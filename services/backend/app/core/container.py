#services/backend/app/core/container.py
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["app.media"]
    )

container = Container()
