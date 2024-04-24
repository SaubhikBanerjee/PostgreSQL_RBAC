#  ![pg.png](images%2Fpg.png) PostgreSQL **R**ole **B**ase **A**ccess **C**ontrol
## Proposed RBAC Architecture:
![postgresql_rbac_architecture.png](images%2Fpostgresql_rbac_architecture.png)
### Files in this repository
#### [config.ini](config%2Fconfig.ini)
Place your configuration here. <br>
**DATABASE** section is used to mention your PostgreSQL database connection credentials.
To these operation you must be a superuser.
<br>
**LOG** section is used to mention the logging configuration.<br>
You can mention `n`  number of teams as per your need, the format should be same!<br>
TEAM_`n` <br>
team`n`_role_name = my_team1_role <br>
team`n`_passwd = passw0rd <br>
team`n`_schema_name = my_team1_schema <br>

#### [create_rbac.py](create_rbac.py)
The main file which implements Role Base Access Control (RBAC). Run `python .\create_rbac.py`
