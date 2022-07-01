-- Создаём базу данных
CREATE DATABASE learnsql;

-- Создаём таблицу departments структура две колонки
-- id - первичный ключ, самогененрируемый не изменяемый
-- name - небольшое текстовое поле
CREATE TABLE departments (
	id SMALLINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(255)
	);

-- Наполняем данными таблицу departments колонку name
INSERT INTO departments (name) VALUES ('IT'),('Sales');
SELECT * FROM employees;
 --id | name
------+-------
--  1 | IT
--  2 | Sales
--(2 rows)

-- Создаём таблицу departments структура две колонки
-- id - первичный ключ, самогененрируемый не изменяемый
-- name - небольшое текстовое поле
-- salary - DATA TYPE NUMERIC
-- department_id связь с departments (id)
CREATE TABLE employees (
	id SMALLINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(255) NOT NULL,
	salary NUMERIC NOT NULL,
	department_id SMALLINT REFERENCES departments (id)
	);

-- Наполняем данными таблицу employees
INSERT INTO employees (name, salary, department_id) VALUES 
	('Joe',70000,1),
	('Henry',80000,2),
	('Sam',60000,2),
	('Max',90000,1);
SELECT * FROM employees;
 --name  | salary | department_id
---------+--------+---------------
 --Joe   |  70000 |             1
 --Sam   |  60000 |             2
 --Max   |  90000 |             1
 --Henry |  80000 |             2
--(4 rows)

-- Промежуточный результат, доболняем полем departments.id
-- используем псевдонимы employees AS e, departments AS d
SELECT e.*, d.name
  FROM employees AS e
  LEFT JOIN departments AS d ON d.id = e.department_id;

-- id | name  | salary | department_id | manager_id | name
------+-------+--------+---------------+------------+-------
--  1 | Joe   |  70000 |             1 |          3 | IT
--  3 | Sam   |  60000 |             2 |            | Sales
--  4 | Max   |  90000 |             1 |            | IT
--  2 | Henry |  80000 |             2 |          4 | Sales
--(4 rows)

-- оставляем только нужные поля, агрегируем (суммируем), группируем, сортируем
SELECT d.name AS name, MAX(e.salary) AS salary
  FROM employees e JOIN departments d ON d.id = e.department_id
  GROUP BY d.name
  ORDER BY salary DESC;
-- name  | salary
---------+--------
-- IT    |  90000
-- Sales |  80000
--(2 rows)

-- Дополняем таблицу employees колонкой manager_id, наполняем данными
UPDATE employees SET manager_id = 3 WHERE id = 1;
UPDATE employees SET manager_id = 4 WHERE id = 2;
UPDATE employees SET manager_id = NULL WHERE id in (3,4);
SELECT * FROM employees;
 --id | name  | salary | department_id | manager_id
------+-------+--------+---------------+------------
--  1 | Joe   |  70000 |             1 |          3
--  2 | Henry |  80000 |             2 |          4
--  3 | Sam   |  60000 |             2 |
--  4 | Max   |  90000 |             1 |

-- Делаем выборку с таблицы employees находим имена всех работников которые получают больше
-- чем их менеджер указаный в поле manager_id. если нет менеджера они не попадают в выборку
SELECT e.name AS employer, e.salary AS salary_e, m.name AS manager, m.salary AS salary_m
	FROM employees e JOIN employees m ON (e.manager_id IS NOT NULL) and e.manager_id = m.id
	WHERE e.salary > m.salary;
-- employer | salary_e | manager | salary_m
------------+----------+---------+----------
-- Joe      |    70000 | Sam     |    60000
--(1 row)

-- Создаём таблицу weathers структура три колонки
-- id - первичный ключ, самогененрируемый не изменяемый
-- date - DATA TYPE TIMESTAMP
-- temperature - DATA TYPE SMALLINT
CREATE TABLE weathers (
	id SMALLINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	date TIMESTAMP WITHOUT TIME NOT NULL,
	temperature SMALLINT NOT NULL
	);
-- Наполняем данными таблицу weathers
INSERT INTO weathers (date, temperature) VALUES 
	('2022-01-01',10),
	('2022-01-02',25),
	('2022-01-03',20),
	('2022-01-04',30);
SELECT * FROM weathers;
-- id |        date         | temperature
------+---------------------+-------------
--  5 | 2022-06-01 00:00:00 |          10
--  6 | 2022-06-02 00:00:00 |          25
--  7 | 2022-06-03 00:00:00 |          20
--  8 | 2022-06-04 00:00:00 |          30
--(4 rows)

-- Делаем выборку с таблицы temperature находим все дни в которых
-- температура была выше чем вчера (в предыдущий день)
-- для наглядности выводим даты и температуры
SELECT t1.id, t1.date AS today, t1.temperature AS t_today, t2.temperature AS t_yesterday, t2.date AS yesterday
	FROM weathers t1 JOIN weathers t2
	ON EXTRACT(day FROM t1.date) - EXTRACT(day FROM t2.date) = 1
	WHERE t1.temperature > t2.temperature;
-- id |        today        | t_today | t_yesterday |      yesterday
------+---------------------+---------+-------------+---------------------
--  6 | 2022-06-02 00:00:00 |      25 |          10 | 2022-06-01 00:00:00
--  8 | 2022-06-04 00:00:00 |      30 |          20 | 2022-06-03 00:00:00

-- Создаём таблицу universities структура три колонки
-- id - первичный ключ, самогененрируемый не изменяемый
-- name - DATA TYPE VARCHAR(255)
CREATE TABLE universities (
	id SMALLINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(255) NOT NULL
	);
-- Наполняем данными таблицу universities
INSERT INTO universities (name) VALUES
	('name1'), ('name2'), ('name3');
-- id | name
------+-------
--  1 | name1
--  2 | name2
--  3 | name3
--(3 rows)

-- Создаём таблицу students структура три колонки
-- id - первичный ключ, самогененрируемый не изменяемый
-- name - DATA TYPE VARCHAR(255)
-- university_id - DATA TYPE SMALLINT (связь) REFERENCES universities (id)
CREATE TABLE students (
	id SMALLINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(255) NOT NULL,
	university_id SMALLINT REFERENCES universities (id)
	);
-- Наполняем данными таблицу universities
INSERT INTO students (name, university_id) VALUES
	('vASYA', 1), ('petya', 2), ('misha', 2), ('anna', 3);
-- id | name  | university_id
------+-------+---------------
--  1 | vASYA |             1
--  2 | petya |             2
--  3 | misha |             2
--  4 | anna  |             3
--(4 rows)
-- Делаем выборку с таблицы students, дополняем названием университета с таблицы universities,
-- находим только тех студентов, где название университета соответствует строке: 'name2'
SELECT s.id, s.name, u.name
FROM students s JOIN universities u
ON s.university_id = u.id
WHERE u.name = 'name2';
-- id | name  | name
------+-------+-------
--  2 | petya | name2
--  3 | misha | name2
--(2 rows)