"""

for starting a,ending n=select * from employees where name like 'a%n' 
specific amount=

group by= groups rows having the same values into one summary

window functions
syntax:= 
function()
over(partition by order):-perform the calculations over these rows 
partition b (combine rows)

Function()

OVER (PARTITION BY ... ORDER BY ...):
Performs calculations over a set of rows (window).
PARTITION BY: Combines rows into groups.

ROW_NUMBER():
Gives unique numbering to each row.

RANK():
Same values receive the same rank, but gaps appear afterward.

DENSE_RANK():
Same values receive the same rank, with no gaps.

LEAD():
Returns the next row's value.

LAG():
Returns the previous row's value.

like:=
select name, salary,ROW_NUMBER()
over (order by salary)
from employees;

CTE (Common Table Expression)= cte is like temporary named result set used to mke complex queries eaiser to read and reuse 
with new_colon_name as (select * from employees where salary>20000)
select * from new_colon_name ;

indexing=improves the speed of searching data slows down insertion update and delete
create index id_employee_name on employee(name);# for single column
types of indexing:
1)single col
2)composite index(combine 2 col)
3) unique index= no duplicates allowed
4)primary key index

to connect python with mysql we need driver
    """