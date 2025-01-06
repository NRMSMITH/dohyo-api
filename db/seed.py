from db.connection import connect_to_db
import json

def seed_db(env='test'):
    print("\U0001FAB4 Seeding the database...")
    db = connect_to_db()
    db.run("DROP TABLE if exists users;")
    db.run("DROP TABLE if exists stables;")
    db.run("DROP TABLE if exists rikishi_stable;")
    db.run("DROP TABLE if exists rikishi;")

    db.run(
        'CREATE TABLE rikishi (\
                id SERIAL PRIMARY KEY NOT NULL, \
                sumodb_id INT NOT NULL, \
                nsk_id INT NOT NULL, \
                shikona_en VARCHAR(50), \
                shikona_jp VARCHAR(50), \
                current_rank VARCHAR(500), \
                heya VARCHAR(50), \
                birth_date VARCHAR(50), \
                shusshin VARCHAR(100), \
                height DECIMAL, \
                weight DECIMAL, \
                debut VARCHAR(6),\
                sumoapi_id INT NOT NULL \
            );'
    )

    db.run(
        'CREATE TABLE rikishi_stable(\
            rikishi_stable_id SERIAL PRIMARY KEY NOT NULL, \
            makuuchi INT REFERENCES rikishi(id), \
            juryo INT REFERENCES rikishi(id), \
            makushita INT REFERENCES rikishi(id), \
            sandanme INT REFERENCES rikishi(id), \
            jonidan INT REFERENCES rikishi(id), \
            jonokuchi INT REFERENCES rikishi(id)\
            );'
    )

    db.run(
        'CREATE TABLE stables(\
            stable_name VARCHAR(500) UNIQUE, \
            stable_id SERIAL PRIMARY KEY NOT NULL, \
            ranking INT DEFAULT 0, \
            rikishi INT REFERENCES rikishi_stable(rikishi_stable_id)\
            );'
    )

    db.run(
        'CREATE TABLE users(\
            user_id SERIAL PRIMARY KEY, \
            stable_name VARCHAR(50) REFERENCES stables(stable_name), \
            username VARCHAR(50) \
            );'
    )

    with open(f'data/{env}-data/stables.json', 'r') as file:
        STABLES_DATA = json.load(file)
        ROWS = STABLES_DATA['stables']
        row_count = 0
        for row in ROWS:
            db.run(
                'INSERT INTO stables (stable_name) VALUES \
                (:stable_name)',
                stable_name=row['stable_name'])
            row_count+= 1
        print(
            f'\U0001F4BE Successfully seeded {row_count} rows to `stables` table in the database. \U0001F44D'
        )

    with open(f'data/{env}-data/users.json', 'r') as file:
        USERS_DATA = json.load(file)
        ROWS = USERS_DATA['users']
        row_count = 0
        for row in ROWS:
            db.run(
                'INSERT INTO users (username, stable_name) VALUES \
                (:username, :stable_name)',
                username=row['username'],
                stable_name=row['stable_name']
            )
            row_count+=1
        print(
            f'\U0001F4BE Successfully seeded {row_count} rows to `users` table in the database. \U0001F44D'
        )

    with open(f'data/{env}-data/rikishi.json', 'r') as file:
        RIKISHI_DATA = json.load(file)
        ROWS = RIKISHI_DATA['rikishi']
        row_count = 0
        for row in ROWS:
            db.run(
                'INSERT INTO rikishi (sumodb_id, nsk_id, shikona_en, shikona_jp, current_rank, heya, birth_date, shusshin, height, weight, debut, sumoapi_id) VALUES \
                (:sumodb_id, :nsk_id, :shikona_en, :shikona_jp, :current_rank, :heya, :birth_date, :shusshin, :height, :weight, :debut, :sumoapi_id)',
                sumodb_id=row['sumodb_id'],
                nsk_id=row['nsk_id'],
                shikona_en=row['shikona_en'],
                shikona_jp=row['shikona_jp'],
                current_rank=row['current_rank'],
                heya=row['heya'],
                birth_date=row['birth_date'],
                shusshin=row['shusshin'],
                height=row['height'],
                weight=row['weight'],
                debut=row['debut'],
                sumoapi_id=row['sumoapi_id']
            )
            row_count+=1
        print(
            f'\U0001F4BE Successfully seeded {row_count} rows to `rikishi` table in the database. \U0001F44D'
        )