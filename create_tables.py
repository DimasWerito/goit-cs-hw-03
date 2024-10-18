import psycopg2

db_config = {
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': 'localhost',
    'port': '5432',
    'dbname': 'postgres'
}

create_tables_sql = [
    """
    create table if not exists users(
	id serial primary key,
	fullname VARCHAR(100),
	email VARCHAR(100) unique
);""",

"""create table if not exists status(
	id serial primary key,
	name VARCHAR(50) unique
);""",

"""create table if not exists tasks(
	id serial primary key,
	title VARCHAR(100),
	description text,
	status_id INTEGER not null,
	user_id INTEGER not null,
	foreign key (status_id) references status(id),
	foreign key (user_id) references users(id) on delete cascade
);"""

]

def create_tables():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        for command in create_tables_sql:
            cur.execute(command)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()