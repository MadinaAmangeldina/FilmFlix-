from connect import *

def delete():
  idField = input("Enter the ID of the record to be deleted: ")   # int()

  try:
    cursor.execute(F"DELETE FROM tblFilms WHERE filmID = {idField}")
    conn.commit()                                   
    print(f"Record {idField} has been deleted")

  except sql.OperationalError as e:
    conn.rollback()
    print(f"Record could not be deleted: {e}")

if __name__ == "__main__":
  delete()