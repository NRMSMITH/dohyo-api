from fastapi import HTTPException
from pg8000 import DatabaseError
from db.connection import connect_to_db
from pg8000.native import literal
from src.utils import format_owned_stable

def get_rikishi():
    query = f"SELECT * FROM rikishi;"

    conn = connect_to_db()
    result = conn.run(query)
    return result


def get_rikishi_by_id(id):
    try:
        int_id = int(id)
        query = f"SELECT * FROM rikishi WHERE id = {literal(int_id)};"
        conn = connect_to_db()
        result = conn.run(query)
        if not result:
            raise HTTPException(status_code=404, detail=f"No rikishi with id: {id}")
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Rikishi id should be a number")
    return result

def get_stable_by_id(id):
    try:
        int_id = int(id)
        query = f"SELECT * FROM stables WHERE stable_id = {literal(int_id)};"
        conn = connect_to_db()
        result = conn.run(query)
        if not result:
            raise HTTPException(status_code=404, detail=f"Stable {id} not found!")
    except ValueError:
        raise HTTPException(status_code=400, detail="Stable id should be a number")
    return result

def post_stable(rikishis):
    rikishi_with_id = {}
    for k,v in rikishis:
        rikishi = get_rikishi_by_id(v)
        rikishi_with_id[k] = rikishi[0][0]
    query = f"INSERT INTO rikishi_stable (makuuchi, juryo, makushita, sandanme, jonidan, jonokuchi) VALUES(:makuuchi, :juryo, :makushita, :sandanme, :jonidan, :jonokuchi) RETURNING *;"
    conn = connect_to_db()
    result = conn.run(query, makuuchi=rikishi_with_id['makuuchi'], juryo=rikishi_with_id['juryo'], makushita=rikishi_with_id['makushita'], sandanme=rikishi_with_id['sandanme'], jonidan=rikishi_with_id['jonidan'], jonokuchi=rikishi_with_id['jonokuchi'])
    columns = [col['name'] for col in conn.columns]
    formatted = format_owned_stable(columns, result[0])
    return formatted