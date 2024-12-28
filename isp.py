class printer:
    def print_doc(self,doc):
        pass

class scanner:
    def scan_doc(self,doc):
        pass

class basic(printer):
    def print_doc(self,doc):
        print(f"printing:{doc}")

class multi(printer,scanner):
    def print_doc(self,doc):
        print(f"printing:{doc}")

    def scan_doc(self,doc):
        print(f"scanning:{doc}")

bas=basic()
bas.print_doc("report4.pdf")

mul=multi()
mul.scan_doc("weather.pdf")
mul.print_doc("w3.pdf")