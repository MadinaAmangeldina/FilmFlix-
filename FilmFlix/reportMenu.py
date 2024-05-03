from read import *
from report import *
from menu import *


def reportOptions():
  options = 0
  while options not in ["1", "2", "3", "4", "5", "6"]:
    with open("PythonProject\FilmFlix\dbReportMenu.txt", "r") as menu:
      choices = menu.readlines()
    for line in choices:
      print(line, end="")
    options = input("Enter a report option: ")
    # logging opportunity - INFO - user selected value x
    if options not in ["1", "2", "3", "4", "5", "6"]:
      print(f"{options} not a valid choice")
    
  return options
         
      
#print(reportOptions())


def reportMenu():
  exit_now = False

  while True:
    reportMenu = reportOptions()
    if reportMenu == "1":
      read()
    elif reportMenu == "2":
      genre()
    elif reportMenu == "3":
      year()
    elif reportMenu == "4":
      rating()
    elif reportMenu == "5":
      break  
    else:
      exit_now = True
      break
  #input("Press enter to exit the Options menu")
  return exit_now

if __name__ == "__main__":
  reportMenu()