## Dohyo-Disco API

This API collates information from the sumodb-api and sanitizes it for the use of a Fantasy Sumo League in development.

This is built with FastAPI and is built in Python.


### Endpoints available:
#### GET all rikishis
```py
/api/rikishi

response = 
{
    "rikishi": [
        {"id": 218,
        "sumodb_id": 300,
        "nsk_id": 1306, 
        "shikona_en": "Dairaido", 
        "shikona_jp": "大雷童(だいらいどう)", 
        "current_rank": "Sandanme 37 East", 
        "heya": "Takadagawa", 
        "birth_date": "1980-04-17T00:00:00Z", 
        "shusshin": "Fukuoka-ken, Onojo-shi", 
        "height": 177, 
        "weight": 151, 
        "debut": "199603", 
        "sumoapi_id": 12345}
    ] ...
}
```

#### GET single rikishi
```py
/api/rikishi/299

response = {
    "rikishi": {
        "id": 299,
        "sumodb_id": 7124, 
        "nsk_id": 2983, 
        "shikona_en": "Kayatoiwa", 
        "shikona_jp": "夏野登岩(かやといわ)", 
        "current_rank": "Jonidan 3 East", 
        "heya": "Minato", 
        "birth_date": "1991-07-13T00:00:00Z", 
        "shusshin": "Gunma-ken, Takasaki-shi", 
        "height": 176, 
        "weight": 103.5, 
        "debut": "200703", 
        "sumoapi_id": 12346}
}


#### GET stable
```py
/api/stables/1

response = {
    "stable_name": "honshu",
    "stable_id": 1,
    "ranking": 0,
    "rikishi": None
}

```