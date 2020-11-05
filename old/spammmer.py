import tkinter as tk

cook = 0
def startspam():
    global cook
    cook +=1
    print("You now have %s cookies"%cook)

root = tk.Tk()
label = tk.Label(root, text = "Cookie Clicker!")
label.pack()
spam = tk.Button(root, text = "Cookie", command = startspam)
spam.pack()
tk.mainloop()
