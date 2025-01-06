from src.app import app
from fastapi.testclient import TestClient
import pytest
from db.seed import seed_db

@pytest.fixture
def re_seed():
    seed_db('test')

class TestRikishi():
    def test_get_rikishi(self, re_seed):
        client = TestClient(app)
        response = client.get("/api/rikishi")
        assert response.status_code == 200
        rikishi = response.json()['rikishi']
        for ri in rikishi:
            assert isinstance(ri['id'], int)
            assert isinstance(ri['sumodb_id'], int)
            assert isinstance(ri['nsk_id'], int)
            assert isinstance(ri['shikona_en'], str)
            assert isinstance(ri['shikona_jp'], str)
            assert isinstance(ri['current_rank'], str)
            assert isinstance(ri['heya'], str)
            assert isinstance(ri['birth_date'], str)
            assert isinstance(ri['shusshin'], str)
            assert isinstance(ri['height'], str)
            assert isinstance(ri['weight'], str)
            assert isinstance(ri['debut'], str)
            assert isinstance(ri['sumoapi_id'], int)

