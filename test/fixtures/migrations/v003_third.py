from test.sqliteutils import drop_column


def upgrade(conn):
    print('adding favorite_color column to person table.')
    conn.execute('alter table person add column favorite_color text default "white"')


def downgrade(conn):
    print('Dropping favorite_color column from person table.')
    # SQLite doesn't support `DROP COLUMN` so we have to do some gymnastics here
    # conn.execute('alter table person drop column favorite_color')
    drop_column(conn, 'person', 'favorite_color')
