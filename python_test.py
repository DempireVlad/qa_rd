class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.__city = city
    def Hello(self):
            return F'Hello my name is {self.name} {self.age}'
info = Person('Vola', 23, 'Kyiv')
print(info.name, info.age)
print(info.Hello())
print(info.__dict__)

class Qa(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, language)
        self.language = language

    def learn(self):
        return F'I see you'

tester = Qa('Olga', 22, 'Python', )

print(tester.name, tester.age, tester.language)
print(tester.Hello())
print(tester.__dict__)