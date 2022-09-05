## Задание 4

### Тема: "Основы реляционных баз данных".

Дана база данных магазина `store` следующей структуры:

```mermaid
%%{init: {'themeCSS': '.er.entityLabel {fill: black !important;} .er.entityBox { fill:rgb(181, 181, 238) !important; }'}}%%
erDiagram

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
sale ||--|{ client : sign_by
good }|--o{ category : has
sale }|--|| sale_history : has
status }|--|| sale_history : of
status }|--|| sale : of
sale }|--|{ good : of
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

> *Примечание*  
> При выполнении `ALTER TABLE` не следует указывать название схемы.  
> Рекомендованные базы данных: `postgreSQL`, `mySQL`