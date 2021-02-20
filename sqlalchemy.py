import sqlalchemy
import pandas as pd

connection_uri = "postgresql://<user>:<password>@<host>:<port>/<database name>" 
db_engine = sqlalchemy.create_engine(connection_uri)

query = "SELECT * FROM table"
df = pd.read_seql(query, db_engine)
