# CICD-2 Sample Template
Test and Coverage
Syntax error in parametrize tests causing failure. No coverage report generated

Running without param tests results in this report
There are some gaps in test coverage for main, as we are not testing some enpoints
For example we are not testing get_db. 

_______________ coverage: platform linux, python 3.11.18-final-0 _______________
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
app/__init__.py       0      0   100%
app/database.py      10      4    60%   18-22
app/main.py          32     16    50%   14, 24-32, 39-40, 47-53
app/models.py        12      0   100%
app/schemas.py       17      0   100%
-----------------------------------------------
TOTAL                71     20    72%
Use this `README.md` as the standard structure for future labs.
