import sqlite3

class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db, check_same_thread=False)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS CARBRANDS (BRAND_ID INTEGER PRIMARY KEY, BRAND_NAME TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS CARMODELS (MODEL_ID INTEGER PRIMARY KEY,BRAND_ID INTEGER, CAR_MODEL TEXT)")
        self.conn.commit()


    def fetch_brand(self):
        self.cur.execute("SELECT * FROM CARBRANDS")
        rows = self.cur.fetchall()
        return rows
    
    def fetch_model(self,brand_id):
        self.cur.execute("SELECT * FROM CARMODELS WHERE BRAND_ID = ? ", (brand_id,))
        rows = self.cur.fetchall()
        return rows

    def insert_brand(self, brand_name):
        self.cur.execute("INSERT INTO CARBRANDS VALUES (NULL, ?)",
                         (brand_name,))
        self.conn.commit()

    def insert_model(self, brand_id, car_model):
        self.cur.execute("INSERT INTO CARMODELS VALUES (NULL, ?, ?)",
                         (brand_id, car_model))
        self.conn.commit()

    def __del__(self):
        self.conn.close()