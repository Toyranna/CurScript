def interpreter():
    open("default.curscript")

def helpmenu():
    print("")
    print("exit - exit CurScript")
    print("help - show the help menu")
    print("learn - a brief explanation on how to write CurScript")
    print("run [filename] - runs a CurScript file")
    print("config - open the settings menu")
    print("")
    
def learnmenu():
    print("")
    print("CurScript files are a bunch of different commands written on new lines")
    print("Here are all the commands you can use:")
    print("")
    print("L[num] - Move left by [num] pixels")
    print("R[num] - Move right by [num] pixels")
    print("U[num] - Move up by [num] pixels")
    print("D[num] - Move down by [num] pixels")    
    print("W[sec] - Wait for [sec] seconds")
    print("X[num] - Go to [num] on the X axis")
    print("Y[num] - Go to [num on the Y axis")
    print("")
    print("If you want to see these commands in action, run default.curscript")
    
def terminal():
    command = input("> ")

    if command == "help":
        helpmenu()
        terminal()
    elif command == "learn":
        learnmenu()
        terminal()
    elif command == "exit":
        print("exiting")
    elif command == "config":
        print("")
        print("1. pixel multiplier")
        print("")
        settingchange = input("select a setting to change - ")
        if settingchange == "1":
            multiplier = input ("configure pixel multiplier: ")
        else:
            print("setting not recognised. Please input a valid number")
        print("")
        terminal()
    elif command == "run":
        filetorun = input("file to run: ")
        interpreter()
    else:
        print("")
        print("command not recognised - input 'help' for a list of commands")
        print("")
        terminal()

print("CurScript 1.0.0")
print("Created by Toyranna")
print("")
print("input 'help' for instructions on how to use this app")
print("input 'learn' for instructions on how to write CurScript")
print("")
terminal()