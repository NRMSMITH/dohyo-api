from fastapi import FastAPI, HTTPException, Request
from src.queries import get_rikishi, get_rikishi_by_id, get_stable_by_id, post_stable
from src.utils import format_rikishi, format_stables
from pydantic import BaseModel



app = FastAPI()


@app.get("/api/rikishi")
def root():
    rikishi_list = get_rikishi()
    formatted_rikishi = format_rikishi(rikishi_list)
    return {"rikishi": formatted_rikishi}

@app.get("/api/rikishi/{id}")
def root(id=int):
        rikishi = get_rikishi_by_id(id)
        formatted_rikishi = format_rikishi(rikishi)[0]
        return {"rikishi": formatted_rikishi}

@app.get("/api/stables/{stable_id}")
def root(stable_id=int):
      stable = get_stable_by_id(stable_id)
      formatted_stable = format_stables(stable)[0]
      return {"stable": formatted_stable}

class Details(BaseModel):
      makuuchi:int
      juryo:int
      makushita:int
      sandanme:int
      jonidan:int
      jonokuchi:int

@app.post("/api/rikishistables", status_code=201)
def root(details:Details):
    posted_stable = post_stable(details)
    return {"stable": posted_stable}