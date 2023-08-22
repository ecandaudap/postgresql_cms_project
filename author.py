""" author.py """
import db

TABLE =  "author"

def create(first_name, last_name, email, password):
    columns = ["first_name", "last_name", "email", "pass"]
    db.insert(TABLE, columns, f"('{first_name}','{last_name}', '{email}', '{password}')")

def get():
    columns = ["author_id","first_name", "last_name", "email", "pass"]
    return db.select(columns, TABLE, "")

def update(id, first_name, last_name, email, password):
    values = f"first_name='{first_name}', last_name='{last_name}' , email='{email}', pass='{password}'"
    where = ('author_id', '=', id)
    db.update(TABLE, values, where)

