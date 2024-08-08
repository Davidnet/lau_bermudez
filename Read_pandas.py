import pandas as pd
import sqlite3

# Ruta al archivo de la base de datos SQLite
db_path = 'database.db'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)

# Consulta SQL para leer datos de una tabla
query = "SELECT * FROM villano;"



# Leer los datos en un DataFrame
df = pd.read_sql_query(query, conn)

# Cerrar la conexión a la base de datos
conn.close()

# Mostrar las primeras filas del DataFrame
print(type(df.head()))
