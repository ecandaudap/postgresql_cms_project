""" category.py """
import db

TABLE =  "category"

def create(name, description):
    columns = ["cat_name", "description"]
    db.insert(TABLE, columns, f"('{name}','{description}')")

def get():
    columns = ["category_id", "cat_name", "description"]
    return db.select(columns, TABLE, "")

def update(id, name, description):
    values = f"cat_name='{name}', description='{description}'"
    where = ('category_id', '=', id)
    db.update(TABLE, values, where)

