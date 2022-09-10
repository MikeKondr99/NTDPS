## Задание 4

[Реализация](../src/tasks/db.ipynb)

### Тема: "Основы реляционных баз данных".

Дана база данных магазина `store` следующей структуры:

```mermaid
erDiagram
%%{init: {'themeCSS': '.er.entityLabel {fill: black !important;} .er.entityBox { fill:rgb(181, 181, 238) !important; }'}}%%

    sale_history {
        id INT PK
        sale_id INT FK
        status_id INT FK
        sale_sum DECIMAL 
        active_from DATE
        active_to DATE
    }

    status {
        id INT PK
        name VARCHAR
    }

    sale {
        id INT PK
        client_id INT FK
        number VARCHAR
        dt_created DATE
        dt_modified DATE
        sale_sum DECIMAL
        status_id INT FK
    }

    category {
        id INT PK
        name VARCHAR
    }

    good {
        id INT PK
        name VARCHAR
        price DECIMAL
    }

    client {
        id INT PK
        code VARCHAR
        first_name VARCHAR
        last_name VARCHAR
        source_id INT FK
    }

    source {
        id INT PK
        name VARCHAR
    }

    client }|--|| source : has
    sale }o--|| client : sign_by
    good }o--o{ category : has
    sale ||--o| sale_history : has
    status ||--o{ sale_history : of
    status ||--o{ sale : of
    sale }o--|{ good : of

```

В таблице `client` ограничение внешнего ключа называется
`fk_client_source1`, определенное на поле `source_id`.

1. Создайте заданную базу данных или измените уже существующую

2. Удалите из таблицы `client` поля `code` и `source_id`.

Для удаления поля, являющегося внешним ключом, необходимо
удалить ограничение внешнего ключа оператором
`DROP FOREIGN KEY `, для данного задание имя первичного ключа:
`fk_client_source1`.

Удаление ограничения внешнего ключа и поля таблицы необходимо
производить в рамках одного вызова `ALTER TABLE`


### Финальная схема базы данных `store`
```mermaid
erDiagram
%%{init: {'themeCSS': '.er.entityLabel {fill: black !important;} .er.entityBox { fill:rgb(181, 181, 238) !important; }'}}%%

    sale_history {
        id INT PK
        sale_id INT FK
        status_id INT FK
        sale_sum DECIMAL 
        active_from DATE
        active_to DATE
    }

    status {
        id INT PK
        name VARCHAR
    }

    sale {
        id INT PK
        client_id INT FK
        number VARCHAR
        dt_created DATE
        dt_modified DATE
        sale_sum DECIMAL
        status_id INT FK
    }

    category {
        id INT PK
        name VARCHAR
    }

    good {
        id INT PK
        name VARCHAR
        price DECIMAL
    }

    client {
        id INT PK
        first_name VARCHAR
        last_name VARCHAR
    }

    source {
        id INT PK
        name VARCHAR
    }

    sale }o--|| client : sign_by
    good }o--o{ category : has
    sale ||--o| sale_history : has
    status ||--o{ sale_history : of
    status ||--o{ sale : of
    sale }o--|{ good : of

```

> *Примечание*  
> При выполнении `ALTER TABLE` не следует указывать название схемы.  
> Рекомендованные базы данных: `postgreSQL`, `mySQL`