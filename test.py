class Help_Ticket:
    def __init__(self, title, body, status):
        self.title  = title
        self.body = body
        self.status = status
        
    def closeTicket(self):
        self.status = "Closed"

    def __str__(self):
        return f"Title={self.title} Body={self.body} Status={self.status}"

myTicket = Help_Ticket("Test", "This is some text", "Open")
secondTicket = Help_Ticket("Test2", "This is different text", "Open")

print(Help_Ticket.__str__(myTicket))