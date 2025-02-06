from src.app import app
from fastapi.testclient import TestClient
import pytest
from db.seed import seed_db
from fastapi import HTTPException

@pytest.fixture
def re_seed():
    seed_db('test')

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

class TestStableTable():

    def test_get_stable_200(self, re_seed):
        client = TestClient(app)
        response = client.get("/api/stables/1")
        assert response.status_code == 200
        assert response.json()['stable'] == {
            "stable_name": "honshu",
            "stable_id": 1,
            "ranking": 0,
            "rikishi": None
        }
    
    def test_get_stable_404(self, re_seed):
        client = TestClient(app)
        response = client.get("/api/stables/123456789")
        assert response.status_code == 404
        assert response.json()['detail'] == "Stable 123456789 not found!"

    def test_get_stable_400(self, re_seed):
        client = TestClient(app)
        response = client.get("/api/stables/not_an_id")
        assert response.status_code == 400
        assert response.json()['detail'] == "Stable id should be a number"

class TestRikishiStableTable():
    def test_post_rikishi_stable_201(self, re_seed):
        client = TestClient(app)
        response = client.post("/api/rikishistables", json={"makuuchi": 4,"juryo": 13, "makushita": 12, "sandanme": 1, "jonidan": 2, "jonokuchi": 7})
        assert response.status_code == 201
        owned_stable = response.json()
        assert owned_stable["stable"] == {
    "rikishi_stable_id": 1,
    "makuuchi": 4,
    "juryo": 13,
    "makushita": 12,
    "sandanme": 1,
    "jonidan": 2,
    "jonokuchi": 7
}