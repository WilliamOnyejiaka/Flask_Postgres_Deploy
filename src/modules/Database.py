import psycopg2
import psycopg2.extras
from .config import HOST,DBNAME,USER,PASSWORD,PORT


# HOST = "ec2-3-223-169-166.compute-1.amazonaws.com"
# DBNAME = "dfl9vjpp5o9m6l"
# USER = "tmelhbtldopzsl"
# PASSWORD = "276fdeb85b68733838900aee7a3826044be5d440d90158e0f87e0d694b94c0af"
# PORT = 5432

class Database:

    def __init__(self) -> None:
        self.host = HOST
        self.dbname = DBNAME
        self.user = USER
        self.password = PASSWORD
        self.port = int(PORT)
        self.conn = None
        self.cur = None
        self.error = None

    def __initiate_connection(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )

            self.cur = self.conn.cursor(
                cursor_factory=psycopg2.extras.DictCursor)

        except Exception as error:
            print(error)
            self.error = error
            self.close()
        
    def connect(self):
        if not self.cur and not self.conn:
            self.__initiate_connection()

    def close(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()

    def commit(self) -> None:
        if self.conn:
            self.conn.commit()
