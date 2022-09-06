import sqlite3

def create(path:str) -> None:
    connection = sqlite3.connect(path)
    cmd = connection.cursor()
    cmd.executescript(open('src/tasks/schema.sql').read())
    print(f'база создана по пути {path}\n')
    good_category_query(cmd)
    print('\n')
    delete_client_source(cmd)
    print('\n')

def good_category_query(cmd:sqlite3.Cursor) -> None:
    from tabulate import tabulate
    cmd.execute("""
    SELECT good.name,category.name FROM good
    LEFT JOIN category_has_good
        ON good.rowid = category_has_good.good_id
    LEFT JOIN category
        ON category.rowid = category_has_good.category_id
    """)
    data = cmd.fetchall()
    print(tabulate(data,headers=["товар", "категория"]))

# удаляет source_id,code из таблица client и таблицу source
def delete_client_source(cmd:sqlite3.Cursor) -> None:
    from tabulate import tabulate
    print("\nДо изменения")
    cmd.execute("""
    SELECT * FROM client
    """)
    data = cmd.fetchall()
    print(tabulate(data,headers=["код","имя","фамилия","id-источник"]))
    cmd.executescript('''
    DROP TABLE source;
    PRAGMA foreign_keys=off;
    BEGIN TRANSACTION;

    ALTER TABLE client RENAME TO _client_old;

    CREATE TABLE client
    (
        first_name TEXT,
        last_name  TEXT 
    );

    INSERT INTO client SELECT first_name, last_name FROM _client_old;
    DROP TABLE _client_old;

    COMMIT;
    PRAGMA foreign_keys=on;

    ''')
    print("\nПосле изменения")
    cmd.execute("""
    SELECT * FROM client
    """)
    data = cmd.fetchall()
    print(tabulate(data,headers=["имя", "фамилия"]))





