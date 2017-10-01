from Tkinter import *
import ttk


class Hangman():
    """docstring for Hangman"""

    def __init__(self, master):
        self.label = ttk.Label(master, text="HANGMAN")
        self.label.pack()
        self.label.config(font=('Courier', 30, 'bold'))
        self.label.config(foreground='blue', background='black')
        self.label.config(image=PhotoImage(file='C:\\Users\\S K Sharma\\Desktop\\Project_Hangman\\python_logo.gif'))


def main():
    root = Tk()
    Hangman(root)
    root.mainloop()


if __name__ == '__main__':
    main()
