# MiniMigrate

MiniMigrate is a simple schema migration too written in Python and intended for projects that want to mangage migrations with simple SQL statements.

- Migrations are Python files in a directory
- The file name must be like `v001_some_name.py`
- The migrations will be run up or down in order
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

- `conn` is a SQLAlchemy connection passed into the the `upgrade` and `downgrade` functions
- A migration file must have an `upgrade` and `downgrade` function


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

