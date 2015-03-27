def upgrade(conn):
    print('Creating the person table.')
    conn.execute('create table person (name text)')
    conn.execute('insert into person (name) values ("foo"), ("bar"), ("baz")')


def downgrade(conn):
    print('Dropping the person table.')
    conn.execute('drop table person')
