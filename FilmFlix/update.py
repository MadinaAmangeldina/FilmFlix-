from connect import *

def update():
  idField = input("Enter the ID of the record to be updated: ")   # int()

  fieldName = input("Enter the field to be updated (Title, yearReleased, Rating, Duration, Genre): ").title()

  newValue = input(f"Enter the value for {fieldName}: ")  # python string output
  #print the value to check

  # newValue = "'"+newValue+"'"     
   # newValue = "'"+newValue+"'"  converts python string into database text
   
  try:
    cursor.execute(f"UPDATE tblFilms SET {fieldName} = '{newValue}' WHERE filmID = {idField}")
    conn.commit()                                   # ' ' converts python string into database text
    print(f"Record {idField} has been updated")

  except sql.OperationalError as e:
    conn.rollback()
    print(f"Record could not update: {e}")

if __name__ == "__main__":
  update()