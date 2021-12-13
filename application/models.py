# coding: utf-8

from peewee import PostgresqlDatabase, Model, TextField, PrimaryKeyField

database = PostgresqlDatabase(None)

class AbstractModel(Model):
    class Meta:
        database = database

class Cities(AbstractModel):
    id = PrimaryKeyField()
    name = TextField(unique=True)

    class Meta:
        db_table = 'cities'
