# Data Platform - models

Usig sqlalchemy library models are generated and it is using mysql database to create these models.

## Installation

It requires [Sqlalchemy 1.4](https://www.sqlalchemy.org/download.html) and pymysql library

To Install the dependencies

```sh
pip install pymysql
pip install sqlalchemy
```

To create models/tables in database follow the steps,

```sh
cd models
python3 create_database.py
```

It create the tables in database and echo the create statement in the console.

Note:
- TEXT data type cannot be set as primary in mysql, instead String with defined character limit can be set as primary key
- Need to handle cascade delete for deleting a record from child tables.
