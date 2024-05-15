from connect import *

# subroutines
def genre():
    filmGenre = input("Enter Genre: ").title()
    cursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{filmGenre}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
      print(aRecord)
    if filmGenre not in row:
       print(f"No films found with {filmGenre.lower()} genre.")

def year():
    filmYear = input("Enter a Year Film released: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{filmYear}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
      print(aRecord)
    if filmYear not in row:
      print(f"No films found with {filmYear.lower()} release year.")

def rating():
    filmRating = input("Enter a Film rating (PG, R, G): ").upper()
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{filmRating}' ") # select all records
    row = cursor.fetchall() # get all the selected records from the table in the db
    for aRecord in row:
      print(aRecord)
    if filmRating not in row:
      print(f"No films found with {filmRating.lower()} rating.")


if __name__ == "__main__":
    genre()
    year()
    rating()
    