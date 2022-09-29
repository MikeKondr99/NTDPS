
CREATE TABLE IF NOT EXISTS orders (
    user_id            INTEGER,    -- уникальный идентификатор пользователя
    order_id           INTEGER,    -- уникальный идентификатор заказа
    order_time         INTEGER,    -- время сделанного заказа в unixtime (секунды, UTC)
    order_cost         REAL,   -- стоимость заказа
    success_order_flag BOOLEAN -- идентификатор, определяющий был ли заказ 
);