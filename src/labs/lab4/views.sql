
DROP VIEW IF EXISTS activation_orders;
CREATE VIEW activation_orders as -- содержит все заказы активации (новые и реактивации)
    SELECT 
        o.order_id as order_id,
        o.user_id as user_id,
        o.order_time as order_time
    FROM orders as o
    JOIN orders as o2 
    ON o.user_id = o2.user_id
    WHERE 
        -- ищем успешные пары заказов с возможной зависимостью от другого заказа
        datetime(o.order_time) BETWEEN datetime(o2.order_time,'-90 day') AND datetime(o2.order_time)
        -- оба заказа должны быть успешными
        AND o.success_order_flg = 1
        AND o2.success_order_flg = 1
    GROUP BY o2.order_id
    -- находим заказ который точно зависит только от себя
    -- он является новым или реактивационным
    HAVING count(o.order_id) = 1
    ORDER BY o.order_id;

DROP VIEW IF EXISTS activation_ranges;
CREATE VIEW activation_ranges as
    SELECT 
        ao1.user_id as user_id,
        ao1.order_id as order_id,
        ao1.order_time as start_time,
        -- для каждой даты начала диапазона нас интересует самый короткий
        min(
            CASE
                WHEN ao1.order_time >= ao2.order_time THEN datetime('now') ELSE datetime(ao2.order_time,'-1 second')
            END) as end_time,
        ao1.order_time = mo.order_time as is_new
    FROM activation_orders as ao1
    LEFT JOIN activation_orders as ao2
    ON ao1.user_id = ao2.user_id
    LEFT JOIN 
        -- по минимальному времени для пользователя определям первый заказ и период активации
        (SELECT user_id,min(order_time) as order_time FROM activation_orders GROUP BY user_id) as mo
    ON ao1.user_id = mo.user_id
    -- интересуют только диапазоны где один раньше другого
    WHERE ao1.order_time <= ao2.order_time 
    GROUP BY ao1.order_id
    ORDER BY ao1.user_id,start_time;


DROP VIEW IF EXISTS Info;
CREATE VIEW Info as
   SELECT r.user_id,r.start_time,o.order_cost,r.is_new
    FROM orders as o
    JOIN activation_ranges as r
    ON o.user_id = r.user_id
    WHERE o.order_time BETWEEN r.start_time AND r.end_time
    ORDER BY o.user_id,o.order_time;

DROP VIEW IF EXISTS Result;
CREATE VIEW Result as
    SELECT  date(start_time) as [date], 
            sum(order_cost * is_new),
            sum(order_cost * NOT is_new),
            sum(order_cost),
            count(DISTINCT CASE WHEN is_new = 1 THEN user_id END) as count_new,
            count(DISTINCT CASE WHEN is_new = 0 THEN user_id END) as coutn_renew,
            count(DISTINCT user_id)
    FROM Info
    GROUP BY [date]

;






