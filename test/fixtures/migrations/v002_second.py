from test.sqliteutils import drop_column


def upgrade(conn):
    print('adding age column to person table.')
    conn.execute('alter table person add column age integer default 0')
    conn.execute('update person set age = 1 where name = "foo"')
    conn.execute('update person set age = 2 where name = "bar"')
    conn.execute('update person set age = 3 where name = "baz"')


def downgrade(conn):
    print('Dropping age column from person table.')
    # SQLite doesn't support `DROP COLUMN` so we have to do some gymnastics here
    # conn.execute('alter table person drop column age')
    drop_column(conn, 'person', 'age')
