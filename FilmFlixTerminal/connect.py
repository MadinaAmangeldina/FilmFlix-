import sqlite3 as sql

try:
  with sql.connect("C:/Users/madin/Desktop/JustIT Bootcamp/PythonProject/FilmFlixTerminal/filmflix.db") as conn:
    cursor = conn.cursor()

except sql.OperationalError as e:
  print(f"Connection Failed!, {e}")