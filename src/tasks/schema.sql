DROP TABLE IF EXISTS sale_history;
DROP TABLE IF EXISTS sale_has_good;
DROP TABLE IF EXISTS category_has_good;
DROP TABLE IF EXISTS good;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS sale;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS source;
DROP TABLE IF EXISTS category;

CREATE TABLE status(
    name TEXT
);
INSERT INTO status
( name      ) VALUES
('Отменен'  ),
('Оплачен'  ),
('В пути'   ),
('Доставлен'),
('Получено' );

CREATE TABLE source(
    name TEXT
);
INSERT INTO source
( name     ) VALUES
('источник');


CREATE TABLE category(
    name TEXT
);
INSERT INTO category
( name       ) VALUES
('еда'       ),
('одежда'    ),
('гигиена'   ),
('техника'   ),
('мебель'    ),
('канцелярия'),
('обувь'     ),
('медицина'  );


CREATE TABLE good(
    name  TEXT,
    price REAL
);
INSERT INTO good
( name              ,price) VALUES
('шоколадка вкусная',70    ),
('штаны кожаные'    ,1000  ),
('ноутбук крутой'   ,35000 ),
('лак швецкий'      ,350   ),
('диплом врача'     ,2000  ),
('капли глазные'    ,50    ),
('настольная лампа' ,200   ),
('мышка B7 Tech'    ,2700  ),
('тетрадъ'          ,150   ),
('ботинки абибас'   ,15000 );


CREATE TABLE client(
    code       TEXT,
    first_name TEXT,
    last_name  TEXT,
    source_id  INTEGER,
    FOREIGN KEY(source_id) REFERENCES source(id)
);
INSERT INTO client
( code, first_name, last_name    ,source_id  ) VALUES
('1'  ,'Диана'    ,'Александрова',1          ),
('2'  ,'Евгений'  ,'Смирнов'     ,1          ),
('3'  ,'Игорь'    ,'Петров'      ,1          ),
('4'  ,'Валентин' ,'Кушков'      ,1          ),
('5'  ,'Ярослав'  ,'Волков'      ,1          );


CREATE TABLE sale(
    client_id   INTEGER,
    number      TEXT,
    dt_created  DATE,
    dt_modified DATE,
    sale_sum    REAL,
    status_id   INTEGER,
    FOREIGN KEY(client_id) REFERENCES client(id),
    FOREIGN KEY(status_id) REFERENCES status(id)
);
INSERT INTO sale
(client_id, number, dt_created , dt_modified,sale_sum,status_id) VALUES
(1        ,'000'  ,'2022-08-05','2022-08-05',94      ,2        ),
(2        ,'000'  ,'2022-08-13','2022-08-13',326     ,5        ),
(3        ,'000'  ,'2022-08-24','2022-08-24',92      ,1        ),
(4        ,'000'  ,'2022-08-01','2022-08-01',1996    ,4        ),
(5        ,'000'  ,'2022-08-04','2022-08-04',256     ,3        ),
(1        ,'000'  ,'2022-08-05','2022-08-05',941     ,5        ),
(2        ,'000'  ,'2022-08-13','2022-08-13',95      ,1        ),
(3        ,'000'  ,'2022-08-24','2022-08-24',936     ,4        ),
(4        ,'000'  ,'2022-08-01','2022-08-01',984     ,3        ),
(5        ,'000'  ,'2022-08-04','2022-08-04',821     ,2        );

CREATE TABLE sale_history(
    sale_id     INTEGER,
    status_id   INTEGER,
    sale_sum    REAL,
    active_from DATE,
    active_to   DATE,
    FOREIGN KEY(sale_id) REFERENCES sale(id),
    FOREIGN KEY(status_id) REFERENCES status(id)
);
INSERT INTO sale_history
(sale_id,status_id,sale_sum, active_from, active_to  ) VALUES
(1      ,2        ,94      ,'2022-08-05','2022-09-23'),
(2      ,5        ,326     ,'2022-08-13','2022-09-12'),
(3      ,1        ,92      ,'2022-08-24','2022-09-20'),
(4      ,4        ,1996    ,'2022-08-01','2022-09-15'),
(5      ,3        ,256     ,'2022-08-04','2022-09-26'),
(6      ,5        ,941     ,'2022-08-05','2022-09-23'),
(7      ,1        ,95      ,'2022-08-13','2022-09-12'),
(8      ,4        ,936     ,'2022-08-24','2022-09-20'),
(9      ,3        ,984     ,'2022-08-01','2022-09-15'),
(10     ,2        ,821     ,'2022-08-04','2022-09-26');

CREATE TABLE sale_has_good(
    sale_id INTEGER,
    good_id INTEGER,
    FOREIGN KEY(sale_id) REFERENCES sale(id),
    FOREIGN KEY(good_id) REFERENCES good(id)
);

CREATE TABLE category_has_good(
    category_id INTEGER,
    good_id     INTEGER,
    FOREIGN KEY(category_id) REFERENCES category(id),
    FOREIGN KEY(good_id) REFERENCES good(id)
);
INSERT INTO category_has_good
(good_id,category_id) VALUES
(1      ,1          ),
(2      ,2          ),
(3      ,4          ),
(4      ,3          ),
(6      ,8          ),
(7      ,5          ),
(8      ,4          ),
(9      ,6          ),
(10     ,7          ),
(10     ,2          );