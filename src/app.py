from fastapi import FastAPI, HTTPException, Request
from src.queries import get_rikishi, get_rikishi_by_id, get_stable_by_id
from src.utils import format_rikishi, format_stables



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