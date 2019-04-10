from peewee import *

sqlite_db = SqliteDatabase('diff.db',
    pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class ORM(Model):
    """Modelo base para que use nuestra instancia de peewee."""
    class Meta:
        database = sqlite_db

    def setup_db(self):
        sqlite_db.connect()
        sqlite_db.create_tables([Optimizacion])
        sqlite_db.close()


class Optimizacion(ORM):
    funcion = CharField()
    dimension = IntegerField()
    generacion = IntegerField()
    fitness = DoubleField()


if __name__ == "__main__":
    orm = ORM()
    orm.setup_db()

    # data = PerformanceGenetico()
    # data.funcion = "na"
    # data.dimension = 2
    # data.fitness = 2.2
    # data.generacion = 0
    # data.save()
