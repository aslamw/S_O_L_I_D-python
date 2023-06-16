
"""
Nesse exemplo, a classe AllInOnePrinter implementa as interfaces 
Printer e Scanner. Ao usar o ISP, as interfaces são segregadas 
em unidades coesas, permitindo que as classes implementem apenas os 
métodos relevantes para elas. Dessa forma, as classes não precisam 
implementar métodos desnecessários.
"""

class Printer:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self):
        pass

class Fax:
    def send_fax(self, recipient, document):
        pass

class AllInOnePrinter(Printer, Scanner, Fax):
    def print_document(self, document):
        print("Printing document:", document)

    def scan_document(self):
        print("Scanning document")

    def send_fax(self, recipient, document):
        print("Sending fax to:", recipient)
        print("Faxing document:", document)
