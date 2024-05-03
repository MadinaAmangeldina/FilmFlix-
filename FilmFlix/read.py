from connect import *   # import everything from the connect.py file

def read():
  try:
    cursor.execute("SELECT * FROM tblFilms")     # selects all the records from the songs table
    row = cursor.fetchall()  # obtain all the records and they are stored in the row variable
    for aRecord in row:
      print(aRecord)

  except sql.OperationalError as e:
    print(f"Record not found: {e}")

if __name__ == "__main__":
  read()