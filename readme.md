# MiniMigrate

MiniMigrate is a simple schema migration too written in Python and intended for projects that want to mangage migrations with simple SQL statements.


# Installation

`pip install minimigrate`


# Usage Example

The following will run all the upgrade migrations from the current version to the latest version.

`minimigrate mysql://user:pass@hostname/dbname /path/to/migrations`


# About

- Migrations are Python modules containing an `upgrade` and a `downgrade` function
- The file name must be like `v001_some_name.py`
    - `001` is the version number and will be cast to an integer
    - The leading `v` is necessary since Python modules can't begin with a number
- A migration file looks like this:

```python

def upgrade(conn):
    print('Creating the person table.')
    conn.execute('create table person (name text)')
    conn.execute('insert into person (name) values ("foo"), ("bar"), ("baz")')


def downgrade(conn):
    print('Dropping the person table.')
    conn.execute('drop table person')


```

- A table named `schema_info` will be created in the database to track the version number.


## Non Goals

- Work like Ruby on Rails' Active Record Migrations
- Integrate with an ORM
- Magically generate migrations by introspection


## Testing

Run `nosetests` in the minimigrate directory.
Run `nosetests --with-coverage --cover-package=minimigrate` to see code coverage.


## TODO

This is a work in progress. Below are the things left to do for v1.

- Finish testing the Migrations class
- Additional CLI options
    - Migrate multiple databases (accept multiple URIs)
    - Execute a single migration, up or down
- Better docstrings
- More documentation and examples
- Optionally generate SQL output instead of connecting to the database
- Generate a new migration file with the `upgrade` and `downgrade` functions

