class Ident:
    def __init__(self, name):
        self.name = name
        self.value = "default"

    def setValue(self,value):
        self.value = value