from db.connection import connect_to_db
from pg8000.native import literal

def get_rikishi():
    query = f"SELECT * FROM rikishi;"

    conn = connect_to_db()
    result = conn.run(query)
    return result


def get_rikishi_by_id(id):
    int_id = int(id)
    query = f"SELECT * FROM rikishi WHERE id = {int_id};"
    conn = connect_to_db()
    result = conn.run(query)
    return result