import databases
import sqlalchemy
import os


DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
TEST_DATABESE = os.getenv('TESTE_DATABASE', 'false') in ('true', 'yes' )
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABESE)
metadata = sqlalchemy.MetaData()