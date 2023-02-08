class newString():
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


string1 = newString()
string1.getString()
string1.printString()
