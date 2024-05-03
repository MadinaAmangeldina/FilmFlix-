import sqlite3 as sql

try:
  with sql.connect("PythonProject/FilmFlix/filmflix.db") as conn:
    cursor = conn.cursor()

except sql.OperationalError as e:
  print(f"Connection Failed!, {e}")