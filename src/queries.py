from db.connection import connect_to_db


def get_rikishi():
    query = f"SELECT * FROM rikishi;"

    conn = connect_to_db()
    result = conn.run(query)
    return result