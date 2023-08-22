""" article.py """
import db

TABLE =  "article"

def create(title, content, author_id, category_id):
    columns = ["title", "cont", "author_id", "category_id", "published_date", "last_updated", "active"]
    db.insert(TABLE, columns, f"('{title}','{content}', {author_id}, {category_id}, now(), now(), true)")

def get():
    columns = ["title_id","title", "cont", "author_id", "category_id", "published_date", "last_updated", "active"]
    return db.select(columns, TABLE, "")

def get_by_id(id):
    columns = ["title_id","title", "cont", "author_id", "category_id", "published_date", "last_updated", "active"]
    where = ('title_id', '=', id)
    return db.select(columns, TABLE, where)

def get_active():
    columns = ["title_id","title", "cont", "author_id", "category_id", "published_date", "last_updated", "active"]
    where = ("active", "=", "true")
    return db.select(columns, TABLE, where)

def update(id, title, content, author_id, category_id):
    values = f"title='{title}', cont='{content}' , author_id={author_id}, category_id={category_id}, last_updated=now()"
    where = ("title_id", "=", id)
    db.update(TABLE, values, where)

def desactive(id):
    values = f"last_updated=now(), active=false"
    where = ("title_id", "=", id)
    db.update(TABLE, values, where)


def get_by_category(category):
    table = "article a"
    columns = [ "a.title_id", "a.title", "a.cont", "a.author_id", "au.first_name", "au.last_name", "a.category_id", "c.cat_name", "c.description",  "a.published_date", "a.last_updated", "a.active" ]
    where = ("c.cat_name", "LIKE", f"'%{category}%'")
    join = """
            INNER JOIN category c ON a.category_id = c.category_id
            INNER JOIN author au on a.author_id = au.author_id
          """
    return db.select_join(columns, table, join, where)

def get_by_author(author):
    table = "article a"
    columns = [ "a.title_id", "a.title", "a.cont", "a.author_id", "au.first_name", "au.last_name", "a.category_id", "c.cat_name", "c.description",  "a.published_date", "a.last_updated", "a.active" ]
    where = ("au.first_name", "LIKE", f"'%{author}%'")
    join = """
            INNER JOIN category c ON a.category_id = c.category_id
            INNER JOIN author au on a.author_id = au.author_id
          """
    return db.select_join(columns, table, join, where)