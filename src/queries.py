from fastapi import HTTPException
from pg8000 import DatabaseError
from db.connection import connect_to_db
from pg8000.native import literal

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