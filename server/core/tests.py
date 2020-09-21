from django.test import TestCase, AsyncClient


class TestApiWithClient(TestCase):
    async def test_api_with_async_client(self):
        """ the client can retrieve the orders """
        client = AsyncClient()
        response = await client.get('http://127.0.0.1:8000/api/orders/')
        self.assertEqual(response.status_code, 200)
        
