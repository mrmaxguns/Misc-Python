'''
https://www.edureka.co/blog/tkinter-tutorial/
'''

import tkinter    #Import the tkinter module

window = tkinter.Tk()   #Create a tkinter window to store widgets

window.title("HELLO WORLD!!!")  #Title the window

window.geometry("450x350")  #Set window size

label1 = tkinter.Label(window, text = "Hello World!", font =("Arial Bold", 50)).pack() #Add text to window

window.mainloop()   #Put the window in main loop

