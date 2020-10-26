import tkinter as tk
from random import randint

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        global number, numberRange
        number = randint(1, 100)
        numberRange = [1, 100]

    def create_widgets(self):
        title = tk.Label(root,
		 text="guessingGame",
		 fg = "black",
		 font = "Verdana 18 bold").grid(columnspan=10)

        self.numberTitle = tk.Label(root, text="1 - 100", font=("Arial", 14))
        self.numberTitle.grid(row=0, column=0, columnspan=2)

        self.button = tk.Button(root, font=("Helvetica", 10), text="restart", bg="#eae2db", command = self.restartButton, state=tk.DISABLED)
        self.button.grid(row=0, column=9, columnspan=2)

        buttonNumber = 0
        self.buttons = {}
        for height in range(10):
            for width in range(10):
                buttonNumber += 1
                self.buttons[buttonNumber] = tk.Button(root, font=("Helvetica", 14), text=buttonNumber, bg="#eae2db", command=lambda buttonNumber=buttonNumber: self.onClick(buttonNumber)) # lambda is used for calling the arq*
                self.buttons[buttonNumber].grid(row=height+2, column=width, sticky='NWNESWSE')
        subTitle = tk.Label(root,
                             text="Made by Rafał Ochorok, Jakub Rejdych, Antoni Zuber",
                             fg="grey",
                             font="Verdana 10").grid(columnspan=10)

    def onClick(self, guess):
        # print(number)

        self.buttons[guess].configure(bg="#9b8ce1")

        if guess < number and guess > numberRange[0]:

            for i in range(1, guess):
                self.buttons[i].configure(bg="#dc5e81")

            numberRange[0] = guess+1

        elif guess > number and guess < numberRange[1]:

            for i in range(guess+1, numberRange[1]+1):
                self.buttons[i].configure(bg="#dc5e81")

            numberRange[1] = guess-1

        elif guess == number:
            # self.numberTitle.configure(text="WIN!") TODO: It doesn't work
            for i in range(1, 101):
                self.buttons[i].configure(bg="gray", state=tk.DISABLED)
            self.buttons[guess].configure(bg="green", fg="yellow", state=tk.NORMAL)
            self.button.configure(state=tk.NORMAL, bg="#d6cd00")

        titleString = str(numberRange[0]) + " - " + str(numberRange[1])
        self.numberTitle.configure(text=titleString)
        # print(numberRange)

    def restartButton(self):
        numberRange[0] = 1
        numberRange[1] = 100
        global number
        number = randint(1, 100)
        for i in range(1, 101):
            self.buttons[i].configure(bg="#eae2db", fg="black", state=tk.NORMAL)
        self.button.configure(bg="grey", state=tk.DISABLED)
        self.numberTitle.configure(text="1 - 100")


root = tk.Tk()
root.title("guessingGame")
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()
