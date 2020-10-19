class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dolphin(Animal):
    def get_name_age(self):
        return print("I'm a dolphin and I'm %s years old and my name is %s" % (self.age, self.name))


class Zebra(Animal):
    def get_name_age(self):
        return print("I'm a zebra and I'm %s years old and my name is %s" % (self.age, self.name))


dolphin = Dolphin("Yasha", 37)
zebra = Zebra("Vladislav Olegovich", 19)
dolphin.get_name_age()
zebra.get_name_age()
