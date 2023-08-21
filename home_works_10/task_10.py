'''
Задание №1
Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
'''

class Animal():
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return self._size

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return self._color

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' special: {self.get_specific()}'


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return self._spec

    def get_animal_info(self):
        return f'Вид: {self.get_kind()}, кличка: {self.get_name()}, возраст: {self.get_age()} лет,' \
               f' specific: {self.get_specific()}'

class Fabric:

    def __init__(self, animal_class, **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'kind':
                self.kind = value
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'spec':
                self.spec = value
            if key == 'size':
                self.size = value

    def get_info(self):
        if self.animal_class == 'bird':
            return Birds(self.kind, self.name, self.age, self.color)
        elif self.animal_class == 'mammal':
            return Mammals(self.kind, self.name, self.age, self.spec)
        elif self.animal_class == 'fish':
            return Fishes(self.kind, self.name, self.age, self.size)


if __name__ == '__main__':
    animal1 = Fabric(animal_class='bird', kind='Петух', name='Петя', age=1, color='серый')
    print(animal1.get_info().get_animal_info())

    animal2 = Fabric(animal_class='mammal', kind='Корова', name='Зорька', age=7, spec='намясо')
    print(animal2.get_info().get_animal_info())

    animal3 = Fabric(animal_class='mammal', kind='Свинья', name='Борька', age=5, spec='намясо')
    print(animal3.get_info().get_animal_info())

    animal4 = Fabric(animal_class='fish', kind='Карп', name='Вася', age=1, size=5)
    print(animal4.get_info().get_animal_info())
