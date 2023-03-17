import Options
def clean():
    if Options.clean == True:
        import platform, os
        from os import system
        os = platform.system()
        if os == "Linux":
            system("clear")
        elif os == "Windows":
            system("cls")
        else:
            print("Unknown OS, to stop seeing this message please go to options and deactivate clean command")

def options_menu():

    #Options Menu
    clean()
    while True:
        options = ["Clear Screen","It allows the program to clear the screen so its easier to use, disable to stop the screen from cleaning.","Go Back","Go back to the Main Menu"]
        title("Options")
        for index, option in enumerate(options):
            if index % 2 == 0:
                print(f"{index//2+1}. {option}")
            else:
                print(option)
                print("")
        selection = int(input("Select an option please\n> "))
        if selection == 1:
            if Options.clean == True:
                try:
                    Options.clean = False
                except:
                    print("Error OP-01")
                    exit
            if Options.clean == False:
                try:
                    Options.clean = True
                except:
                    print("Error OP-02")
                    exit
            print(f"Clean screen is now {Options.clean}")
        if selection == 2:
            print(exit)

def title(word):
    # Calculate the length of the string plus two for the vertical bars
    str_length = len(word) + 6
    
    # Create the horizontal line using the "=" character
    horizontal_line = "=" * str_length
    
    # Create the string with vertical bars on either side
    decorated_string = f"|| {word} ||"
    
    # Create the final decoration using the horizontal line and the decorated string
    decoration = f"{horizontal_line}\n{decorated_string}\n{horizontal_line}\n"
    
    # Print the decoration
    print(decoration)
