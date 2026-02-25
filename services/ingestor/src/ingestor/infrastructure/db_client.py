from shared.clients.db_client import PhotoApiClient
from shared.http.http_client import HttpClient

def build_photo_repository(config):
    http = HttpClient(base_url=config.DB_SERVICE_URL)
    return PhotoApiClient(http)
