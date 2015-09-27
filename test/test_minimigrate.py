from __future__ import print_function
import os
import unittest
import mock
from nose.tools import eq_
from sqlalchemy import create_engine
from minimigrate import *

DB_URI = 'sqlite:///:memory:'
MIGRATIONS = os.path.join(os.path.dirname(__file__), 'fixtures/migrations')


class TestMigrationFile(unittest.TestCase):
    def setUp(self):
        file_name = os.path.join(MIGRATIONS, 'v001_first.py')
        pattern = '^v(?P<version>\d+).*.py$'
        self.mf = MigrationFile(file_name, pattern=pattern)

    def test_version(self):
        assert self.mf.version == 1

    def test_module(self):
        assert self.mf.module.__name__ == 'v001_first'

    def test_upgrade_and_downgrade(self):
        self.mf.module.upgrade = mock.MagicMock()
        self.mf.module.downgrade = mock.MagicMock()
        
        self.mf.upgrade('hello')
        self.mf.downgrade('hello')
        
        self.mf.module.upgrade.assert_called_with('hello')
        self.mf.module.downgrade.assert_called_with('hello')

    def test_is_valid(self):
        assert self.mf.is_valid()


class TestMigrations(unittest.TestCase):
    def test_get_migrations(self):
        migrations = Migrations(MIGRATIONS)
        results = migrations.migrations
        assert sorted(results.keys()) == [1, 2, 3]
        for version, migration in results.items():
            assert migration.is_valid()



class TestMigrate(unittest.TestCase):
    def setUp(self):
        self.migrator = Migrator(DB_URI, MIGRATIONS)

    def select_records(self):
        query = 'select * from person'
        return self.migrator.engine.execute(query).fetchall()

    def select_version(self):
        query = 'select version from schema_info'
        return self.migrator.engine.execute(query).scalar()

    def assert_version_is(self, version):
        eq_(self.select_version(), version)

    def assert_records_eq(self, records):
        eq_(self.select_records(), records)

    def test_migrate_up(self):
        self.migrator.migrate()
        self.assert_version_is(3)
        expected_records = [
            ('foo', 1, 'white'),
            ('bar', 2, 'white'),
            ('baz', 3, 'white')
        ]
        self.assert_records_eq(expected_records)
        
    def test_migrate_down(self):
        self.test_migrate_up()
        self.migrator.migrate(1)
        self.assert_version_is(1)
        expected_records = [
            ('foo',),
            ('bar',),
            ('baz',)
        ]
        self.assert_records_eq(expected_records)


class TestSchemaVersion(unittest.TestCase):
    def setUp(self):
        engine = create_engine(DB_URI)
        self.schema_version = SchemaVersion(engine)

    def test_it(self):
        eq_(self.schema_version.get(), 0)
        self.schema_version.update(7)
        eq_(self.schema_version.get(), 7)
