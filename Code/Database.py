import Videogame
import Developer
import Utilities
from Utilities import clean, options_menu, title

if __name__ == '__main__':

    #Accesibility
    menu_map = {
    "Add Videogame": "add_videogame",
    "Delete Videogame": "delete_videogame",
    "Show Videogames": "show_videogames",
    "Show Developers": "show_developers",
    "Options": options_menu,
    "Information": "information_menu",
    "Exit": "exit_program"
    }
    #Main Menu
    title("Videogames")
    #It will show the options: Add Videogame, Delete Videogame, Show Videogames, Show Developers, Exit
    menuOptions = ["Add Videogame", "Delete Videogame", "Show Videogames", "Show Developers", "Options", "Information", "Exit"]
    for index, option in enumerate(menuOptions):
        print(f"{index+1}. {option}")
    selection = input("\nPlease choose an option\n> ")
    
    # Get the selected option based on the user's input
    selected_option = menuOptions[int(selection)-1]
    
    # Print out the value of the selected option
    menu_map[selected_option]()