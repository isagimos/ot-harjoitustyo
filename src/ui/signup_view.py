from tkinter import Tk, ttk
from services.signup import SignUp

class CreateAccount:
    def __init__(self, root):
        self._root = root

        self._signup = SignUp(self._root)

        self._errormessage = None


    def start(self):

        self._username_label = ttk.Label(master=self._root, text="Käyttäjänimi: ")
        self._password_label = ttk.Label(master=self._root, text="Salasana: ")
        self._password_label2 = ttk.Label(master=self._root, text="Salasana uudelleen: ")
        self._signup_button = ttk.Button(master=self._root, text="Luo tunnus",
                                        command=lambda: self._create_account())

        self._username_entry = ttk.Entry(master=self._root)
        self._password_entry = ttk.Entry(master=self._root)
        self._password_entry2 = ttk.Entry(master=self._root)


        self._username_label.grid(row=0, column=0)
        self._password_label.grid(row=1, column=0)

        self._username_entry.grid(row=0, column=1)
        self._password_entry.grid(row=1, column=1)

        self._password_label2.grid(row=2, column=0)
        self._password_entry2.grid(row=2, column=1)

        self._signup_button.grid(row=3, column=0, columnspan=2)
    
    def _create_account(self):

        ### tarkista onko käyttäjänimi uniikki ja täsmäävätkö salasanat,
        ### ja tallenna uusi käyttäjätunnus tiedostoon. palaa sitten login-näkymään

        result = self._signup._create_account(self._username_entry.get(),
                            self._password_entry.get(), self._password_entry2.get())
        
        if result != "Tunnus luotu":
            try:
                self._errormessage.destroy()
            except:
                pass
            self._errormessage = ttk.Label(master=self._root, text=f"{result}")
            self._errormessage.grid(row=4, columnspan=2)
            return "Tunnusta ei luotu"

        from login_view import Login
        self._login = Login(self._root)

        self._destroy_signup_view()

        self._login.start()

    def _destroy_signup_view(self):

        self._username_label.destroy()
        self._password_label.destroy()
        self._password_label2.destroy()
        self._username_entry.destroy()
        self._password_entry.destroy()
        self._password_entry2.destroy()
        self._signup_button.destroy()
        try:
            self._errormessage.destroy()
        except:
            pass
