Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел. Строки треугольника симметричны относительно вертикальной оси.

```
0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
```
src/solution.py
Напишите функцию triangle(), которая возвращает указанную строку треугольника Паскаля в виде списка.

### Пример:

```
>>> triangle(0)
[1]
>>> triangle(4)
[1, 4, 6, 4, 1]
```