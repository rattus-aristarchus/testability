import tkinter as tk


class UI:

    def __init__(self):
        self.weather_message = None

    def show(self, run_func):
        root = tk.Tk()

        button = tk.Button(root, text="What's the weather like?", command=run_func)
        button.pack()
        self.weather_message = tk.StringVar()
        self.weather_message.set("The answer will be here")
        message = tk.Label(root, textvariable=self.weather_message)
        message.pack()

        root.mainloop()

    def show_message(self, message):
        self.weather_message.set(message)
