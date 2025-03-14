### Luokan UI suunnittelussa on hyödynnetty kurssimateriaalia: https://ohjelmistotekniikka-hy.github.io/python/tkinter

from tkinter import Tk, ttk
from services.calculator_logic import CalculatorLogic

class Calculator:
    def __init__(self, root):
        
        self._root = root
        self._entry = None

        self._calculator_logic = CalculatorLogic()

    def start(self):
        self._entry = ttk.Entry(master=self._root)

        self._entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.add_numbers()
        self.add_operators_and_result()

        self._logout = ttk.Button(master=self._root, text="Kirjaudu ulos", command=lambda: self._logging_out())
        self._logout.grid(row=6, columnspan=4)

    def _handle_button_click(self, button):
        entry_value = self._entry.get()

### ChatGPT:llä generoitu koodi alkaa

        result = self._calculator_logic.handle_click(entry_value, button)
        
        self.update_entry(result)

    def update_entry(self, update):

        self._entry.config(state="normal")  # Tehdään kentästä muokattavissa oleva
        self._entry.delete(0, "end")  # Tyhjennetään nykyinen sisältä
        self._entry.insert(0, update)  # Lisätään uuden painikkeen arvo loppuun
        self._entry.config(state="readonly")  # Asetetaan kenttä taas luettavaksi

### ChatGPT:llä generoitu koodi päättyy

    def _logging_out(self):
        from login_view import Login
        self._login = Login(self._root)

        self.destroy_calculator_view()

        self._login.start()
    
    def add_numbers(self):

        self._number0 = ttk.Button(master=self._root, text="0", command=lambda: self._handle_button_click("0"))
        self._number1 = ttk.Button(master=self._root, text="1", command=lambda: self._handle_button_click("1"))
        self._number2 = ttk.Button(master=self._root, text="2", command=lambda: self._handle_button_click("2"))
        self._number3 = ttk.Button(master=self._root, text="3", command=lambda: self._handle_button_click("3"))
        self._number4 = ttk.Button(master=self._root, text="4", command=lambda: self._handle_button_click("4"))
        self._number5 = ttk.Button(master=self._root, text="5", command=lambda: self._handle_button_click("5"))
        self._number6 = ttk.Button(master=self._root, text="6", command=lambda: self._handle_button_click("6"))
        self._number7 = ttk.Button(master=self._root, text="7", command=lambda: self._handle_button_click("7"))
        self._number8 = ttk.Button(master=self._root, text="8", command=lambda: self._handle_button_click("8"))
        self._number9 = ttk.Button(master=self._root, text="9", command=lambda: self._handle_button_click("9"))

        self._number1.grid(row=3, column=0)
        self._number2.grid(row=3, column=1)
        self._number3.grid(row=3, column=2)
        self._number4.grid(row=2, column=0)
        self._number5.grid(row=2, column=1)
        self._number6.grid(row=2, column=2)
        self._number7.grid(row=1, column=0)
        self._number8.grid(row=1, column=1)
        self._number9.grid(row=1, column=2)
        self._number0.grid(row=4, column=1)
    
    def add_operators_and_result(self):

        self._plus = ttk.Button(master=self._root, text="+", command=lambda: self._handle_button_click("+"))
        self._minus = ttk.Button(master=self._root, text="-", command=lambda: self._handle_button_click("-"))
        self._multiply = ttk.Button(master=self._root, text="*", command=lambda: self._handle_button_click("*"))
        self._divide = ttk.Button(master=self._root, text="/", command=lambda: self._handle_button_click("/"))
        self._result = ttk.Button(master=self._root, text="=", command=lambda: self._handle_button_click("="))

        self._plus.grid(row=1, column=4)
        self._minus.grid(row=2, column=4)
        self._multiply.grid(row=3, column=4)
        self._divide.grid(row=4, column=4)
        self._result.grid(row=5, column=4)
    
    def destroy_calculator_view(self):

        self._number0.destroy()
        self._number1.destroy()
        self._number2.destroy()
        self._number3.destroy()
        self._number4.destroy()
        self._number5.destroy()
        self._number6.destroy()
        self._number7.destroy()
        self._number8.destroy()
        self._number9.destroy()

        self._entry.destroy()
        self._logout.destroy()

        self._plus.destroy()
        self._minus.destroy()
        self._multiply.destroy()
        self._divide.destroy()
        self._result.destroy()