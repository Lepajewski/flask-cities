# coding: utf-8

from peewee import PostgresqlDatabase, Model, TextField, PrimaryKeyField

database = PostgresqlDatabase(None)

class AbstractModel(Model):
    class Meta:
        database = database

class Cities(AbstractModel):
    id = PrimaryKeyField()
    #czy pole id ma być jednak podawane przez użytkownika?

    name = TextField(unique=True)
    #pole jest oznaczone jako unikatowe, a jednak jestem w stanie dodać dwa miasta o tej samej nazwie

    class Meta:
        db_table = 'cities'
