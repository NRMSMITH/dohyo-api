from db.connection import connect_to_db

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
                sumoapi_id INT NOT NULL, \
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
                debut VARCHAR(6)\
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