import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller, model):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.model = model

        title = tk.Label(self, text="H O M E P A G E", font=("Helvetica", 20))
        title.pack()

        buyTicket = tk.Button(self, text='Buy ticket', relief=tk.GROOVE, font=("Helvetica", 12), command=self.buy_ticket) # command=lambda:
        buyTicket.pack(fill='x', pady=10, ipady=10)

        myTicket = tk.Button(self, text='My ticket', relief=tk.GROOVE, font=("Helvetica", 12), command=self.my_tickets) # command=lambda:
        myTicket.pack(fill='x', pady=5, ipady=10)

        logout = tk.Button(self, text='Log out', relief=tk.GROOVE, font=("Helvetica", 12), command=self.logout) 
        logout.pack(fill='x', pady=10, ipady=10)
    
    def buy_ticket(self):
        self.controller.create_pages()
        self.controller.show_page("BuyTicket")

    def my_tickets(self):
        self.model.myTickets.listMyTickets(self.model.user.id)
        self.controller.create_pages()
        self.controller.show_page("MyTickets")

    def logout(self):
        self.model = None
        self.controller.create_pages()
        self.controller.show_page("Welcome")