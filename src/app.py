from fastapi import FastAPI
from src.queries import get_rikishi
from src.utils import format_rikishi



app = FastAPI()


@app.get("/api/rikishi")
def root():
    rikishi_list = get_rikishi()
    formatted_rikishi = format_rikishi(rikishi_list)
    return {"rikishi": formatted_rikishi}