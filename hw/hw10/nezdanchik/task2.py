class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    @classmethod
    def type(cls):
        return "Homosapiens"

    @staticmethod
    def fact_about_human():
        return ("Humans are the only known species that blush —"
                " it happens when small blood vessels in the face"
                " expand due to emotions like embarrassment or social attention.")


if __name__ == "__main__":
    h1 = Human("John")
    print(h1.greet())
    print(h1.type())
    print(h1.fact_about_human())
