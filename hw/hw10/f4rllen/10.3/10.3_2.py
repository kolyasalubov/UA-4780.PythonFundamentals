class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Привіт, {self.name}!")

    @classmethod
    def get_species(cls):
        return "Species: Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "Це довільне повідомлення."

person = Human("Влад")
person.welcome()
print(Human.get_species())
print(Human.arbitrary_message())