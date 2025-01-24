from src.app import app
from fastapi.testclient import TestClient
import pytest
from db.seed import seed_db
from fastapi import HTTPException

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

class TestRikishiTable():
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

    def test_get_rikishi_by_id(self, re_seed):
        client = TestClient(app)
        response = client.get("/api/rikishi/5")
        assert response.status_code == 200
        rikishi = response.json()['rikishi']
        assert rikishi == {"id": 5, "sumodb_id": 12239, "nsk_id": 3630, "shikona_en": "Hokutofuji", "shikona_jp": "北勝富士 大輝", "current_rank": "Maegashira 3 West", "heya": "Hakkaku", "birth_date": "1992-07-15T00:00:00Z", "shusshin": "Saitama-ken, Tokorozawa-shi", "height": "182", "weight": "158", "debut": "201503", "sumoapi_id": 12349}

    def test_get_rikishi_by_id_no_rikishi(self, re_seed):
        expected = 'No rikishi with id: 27'
        client = TestClient(app)
        response = client.get("/api/rikishi/27")
        assert response.status_code == 404
        assert response.json()['detail'] == expected
        
    def test_get_rikishi_by_id_invalid_id(self, re_seed):
        expected = "Rikishi id should be a number"
        client = TestClient(app)
        response = client.get("/api/rikishi/not_an_id")
        assert response.status_code == 400
        assert response.json()['detail'] == expected

class TestGenericError():
    def test_404_endpoint_not_found(self, re_seed):
        client = TestClient(app)
        response = client.get("/a")
        assert response.status_code == 404
