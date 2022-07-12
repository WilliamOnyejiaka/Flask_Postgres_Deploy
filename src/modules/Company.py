from .Database import Database
from typing import Dict,Tuple


class Company(Database):

    def __init__(self) -> None:
        super().__init__()

    def create_table(self):
        create_script = '''
            CREATE TABLE IF NOT EXISTS company (
                id      SERIAL PRIMARY KEY,
                name    varchar(40) NOT NULL,
                salary  int,
                dept_id varchar(30)
            )
        '''
        self.connect()

        self.cur.execute(create_script)
        self.commit()

    def insert_one(self,insert_value: Tuple):
        insert_script = 'INSERT INTO company (name,salary,dept_id) VALUES (%s,%s,%s)'
        self.connect()

        self.cur.execute(insert_script,insert_value)
        self.commit()

    def find(self):
        query = 'SELECT * FROM company'
        self.connect()
        self.cur.execute(query)
        return self.cur.fetchall()

    def find_one(self, id):
        query = 'SELECT * FROM company WHERE id = %s'
        self.connect()
        self.cur.execute(query, (id,))
        return self.cur.fetchall()

    def drop_table(self):
        self.connect()

        self.cur.execute("DROP TABLE IF EXISTS company")
        self.conn.commit()
