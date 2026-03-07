import httpx

class HttpClient:

    def __init__(self, base_url: str, timeout: float = 10.0):
        self.client = httpx.AsyncClient(base_url=base_url, timeout=timeout)

    async def get(self, url: str, params=None):
        return await self.client.get(url, params=params)

    async def post(self, url: str, json=None):
        return await self.client.post(url, json=json)
