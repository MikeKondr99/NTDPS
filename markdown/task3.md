## Задание 3

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

1. Создайте заданную базу данных

2. Выведите все позиций списка товаров принадлежащие какой-либо категории с названиями товаров и названиями категорий. Список должен быть отсортирован по названию товара, названию категории. Для соединения таблиц необходимо использовать оператор INNER JOIN. Ожидаемый формат результата:


| good_name | category_name |
| -         | -             |
| good 1    | category 1    |
| good 1    | category 2    |
| good 2    | category 3    |
| good 2    | category 4    |
| good 3    | category 7    |


> *Примечание*  
> 1. Выборки, полученные с помощью оператора `SELECT` могут быть отсортированы по нескольким атрибутам. Для этого необходимо в операторе `ORDER BY` указать набор атрибутов через запятую в необходимом порядке.
> 1. В запросе для соединения нескольких источников данных операцию соединения можно использовать многократно. Например, для соединения таблиц A, B и C можно использовать запрос вида:
> 
> ``` SQL
> SELECT * FROM A
>     INNER JOIN B
>         ON A.b_id = B.id
>     INNER JOIN C
>         ON a.c_id = C.id
> ```
> 3. Рекомендованные базы данных: `postgreSQL`, `mySQL`