from read import *
from addRecord import *
from update import *
from delete import *
from reportMenu import *


def menuOptions():
  options = 0
  while options not in ["1", "2", "3", "4", "5", "6"]:
    with open("C:/Users/madin/Desktop/JustIT Bootcamp/PythonProject/FilmFlixTerminal/dbMenu.txt", "r") as menu:
      choices = menu.readlines()
    for line in choices:
      print(line, end="")
    options = input("Enter a menu option: ")
    # logging opportunity - INFO - user selected value x
    if options not in ["1", "2", "3", "4", "5", "6"]:
      print(f"{options} is not a valid choice")
    
  return options
         
      
#print(menuOptions())


def mainMenu():

  while True:
    mainMenu = menuOptions()
    if mainMenu == "1":
      insertFilm()
    elif mainMenu == "2":
      delete()
    elif mainMenu == "3":
      update()
    elif mainMenu == "4":
      read()
    elif mainMenu == "5":
      exit_now = reportMenu()
      if exit_now:
        break
    else:
      input("Press enter to exit the Main menu")
      break
  print("Finished")

if __name__ == "__main__":
  mainMenu()