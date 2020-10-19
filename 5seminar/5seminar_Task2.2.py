class Mother:
    def __str__(self):
        return("She's my daughter!?!?")


class Daughter(Mother):
    def __str__(self):
        return("I'm her daughter!?!?")


print(Mother())
print(Daughter())