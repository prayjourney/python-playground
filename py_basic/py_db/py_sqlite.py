import sqlite3

# 数据库文件名
DB_NAME = "py_sqlite.db"


def create_connection():
    """
    创建与SQLite数据库的连接
    如果数据库不存在，则会创建一个新的数据库文件
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def create_table(conn):
    """
    在数据库连接上创建表（如果不存在）
    """
    try:
        cursor = conn.cursor()
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT
        );
        """
        cursor.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def insert_data(conn, data):
    """
    向employees表中插入多条数据
    """
    try:
        cursor = conn.cursor()
        insert_sql = "INSERT INTO employees (name, age, department) VALUES (?,?,?)"
        cursor.executemany(insert_sql, data)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def query_data(conn):
    """
    从employees表中查询数据并打印
    """
    try:
        cursor = conn.cursor()
        select_sql = "SELECT * FROM employees"
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def update_data(conn, name, new_age):
    """
    根据员工姓名更新其年龄信息
    """
    try:
        cursor = conn.cursor()
        update_sql = "UPDATE employees SET age =? WHERE name =?"
        cursor.execute(update_sql, (new_age, name))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_data(conn, name):
    """
    根据员工姓名删除对应的数据
    """
    try:
        cursor = conn.cursor()
        delete_sql = "DELETE FROM employees WHERE name =?"
        cursor.execute(delete_sql, (name,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    # 创建数据库连接
    connection = create_connection()
    if connection is not None:
        # 创建表
        cursor = connection.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type= 'table' AND name= 'employees'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows[0] is None:
            print("create table")
            create_table(connection)

        # 准备要插入的数据
        employees_data = [
            ("Alice", 28, "HR"),
            ("Bob", 32, "Engineering"),
            ("Charlie", 30, "Marketing")
        ]
        # 插入数据
        insert_data(connection, employees_data)

        # 查询数据
        print("查询插入后的数据:")
        query_data(connection)

        # 更新数据
        update_data(connection, "Alice", 29)
        print("查询更新后的数据:")
        query_data(connection)

        # 删除数据
        delete_data(connection, "Bob")
        print("查询删除后的数据:")
        query_data(connection)

        # 关闭数据库连接
        connection.close()
    else:
        print("无法创建数据库连接")
