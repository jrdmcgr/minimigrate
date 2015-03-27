"""ALTER TABLE DROP COLUMN for SQLite databases.

SQLite doesn't support DROP COLUMN, so you have to recreate the table.
"""
from sqlalchemy import MetaData
from sqlalchemy.schema import Table
from sqlalchemy.schema import CreateTable

def _get_table(conn, table_name):
    meta = MetaData()
    table = Table(table_name, meta, autoload=True, autoload_with=conn.engine)
    return table


def _drop_column(table, column):
    new_columns = [c.copy() for c in table.columns if c.name != column]
    return Table(table.name, MetaData(), *new_columns)


def drop_column(conn, table, column):
    old_table = _get_table(conn, table)
    new_table = _drop_column(old_table, column)
    columns = ','.join(c.name for c in new_table.columns)
    statements = [
        'ALTER TABLE %s RENAME TO old_%s' % (table, table),
        CreateTable(new_table),
        'INSERT INTO %s SELECT %s FROM old_%s' % (table, columns, table),
        'DROP TABLE old_%s' % (table)
    ]                                    
    with conn.begin():
        for statement in statements:
            conn.execute(statement)
 
