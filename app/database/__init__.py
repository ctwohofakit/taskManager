from flask import g;
import sqlite3

DATABASE_URI="main.db"


#signle point of contact,one connection open, avoid duplicate records, and race processing
def get_db():
    db=getattr(g, "_database", None) # if it is not db, db==none
    if not db:
        db=g._database=sqlite3.connect(DATABASE_URI)
    return db


