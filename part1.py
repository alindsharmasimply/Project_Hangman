from Tkinter import *
import ttk


class Hangman():
    """docstring for Hangman"""

    def __init__(self, master):
        self.label = ttk.Label(master, text="HANGMAN")
        self.label.pack()
        self.label.config(font=('Courier', 30, 'bold'))
        self.label.config(foreground='blue', background='black')
        self.label.config(compound='center')

        self.entry = ttk.Entry(master, width=30)
        self.entry.pack()
        self.entry.config(show='*')

        self.button = ttk.Button(master, text="Click Me")
        self.button.pack()
        self.logo = PhotoImage(file='C:\\Users\\S K Sharma\\Desktop\\Project_Hangman\\python_logo.gif')
        self.button.small_logo = self.logo.subsample(5, 5)
        self.button.config(image=self.button.small_logo, compound='left')

        self.canvas = Canvas(master, width=600, height=400)
        self.canvas.pack()
        self.canvas.create_line(50, 50, 20, 20, fill="black", width=5)
        self.canvas.create_text(100, 25, text="Amazing", font="Helvetica 30 bold")


def main():
    root = Tk()
    Hangman(root)
    root.mainloop()


if __name__ == '__main__':
    main()
