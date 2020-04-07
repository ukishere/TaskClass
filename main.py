uncle_Joe_farm = {
    1 : ['Гусь','Серый', 3],
    2 : ['Гусь', 'Белый', 3],
    3 : ['Корова', 'Манька', 450],
    4 : ['Баран', 'Барашек', 90],
    5 : ['Баран', 'Кудрявый', 90],
    6 : ['Курица', 'Ко-Ко', 1],
    7 : ['Курица', 'Кукареку', 1],
    8 : ['Коза', 'Рога', 70],
    9 : ['Коза','Копыта', 70],
    10 : ['Утка', 'Кряква', 2]
}

class Pet:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = ''

    def listen(self):
        print(f'Вы слышите {pet.voice}')

    def feed(self):
        return 'Кормежка прошла успешно'

class Ram(Pet):

    def __init__(self, name, weight):
        Pet.__init__(self, name, weight)
        self.voice = 'блеяние'

    def shear(self):
        return 'Стрижка прошла успешно'

class Duck(Pet):

    def __init__(self, name, weight):
        Pet.__init__(self, name, weight)
        self.voice = 'кряканье'

    def collect_eggs(self):
        return 'Сбор яиц прошел успешно'

class Cow(Pet):

    def __init__(self, name, weight):
        Pet.__init__(self, name, weight)
        self.voice = 'мычание'

    def milk(self):
        return 'Дойка прошла упешно'

class Chicken(Pet):

    def __init__(self, name, weight):
        Pet.__init__(self, name, weight)
        self.voice = 'кудахтанье'

    def collect_eggs(self):
        return 'Сбор яиц прошел успешно'

class Goat(Pet):

    def __init__(self, name, weight):
        Pet.__init__(self, name, weight)
        self.voice = 'блеяние'

    def milk(self):
        return 'Дойка прошла упешно'

    def shear(self):
        return 'Стрижка прошла успешно'

class Goose(Pet):

    def __init__(self, name, weight):
        Pet.__init__(self, name, weight)
        self.voice = 'гогот'

    def collect_eggs(self):
        return 'Сбор яиц прошел успешно'

def action(pet, pet_type):
    if pet_type == 'Гусь':
        print('Доступные опции:\n1. Покормить животное\n2. Послушать животное\n3. Собрать яйца')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print(pet.feed())
        elif choise == 2:
            pet.listen()
        elif choise == 3:
            print(pet.collect_eggs())
        else:
            print('Неверный ввод')

    if pet_type == 'Корова':
        print('Доступные опции:\n1. Покормить животное\n2. Послушать животное\n3. Подоить')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print(pet.feed())
        elif choise == 2:
            pet.listen()
        elif choise == 3:
            print(pet.milk())
        else:
            print('Неверный ввод')

    if pet_type == 'Баран':
        print('Доступные опции:\n1. Покормить животное\n2. Послушать животное\n3. Остричь')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print(pet.feed())
        elif choise == 2:
            pet.listen()
        elif choise == 3:
            print(pet.shear())
        else:
            print('Неверный ввод')

    if pet_type == 'Курица':
        print('Доступные опции:\n1. Покормить животное\n2. Послушать животное\n3. Собрать яйца')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print(pet.feed())
        elif choise == 2:
            pet.listen()
        elif choise == 3:
            print(pet.collect_eggs())
        else:
            print('Неверный ввод')

    if pet_type == 'Коза':
        print('Доступные опции:\n1. Покормить животное\n2. Послушать животное\n3. Остричь\n4. Подоить')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print(pet.feed())
        elif choise == 2:
            pet.listen()
        elif choise == 3:
            print(pet.shear())
        elif choise == 4:
            print(pet.milk())
        else:
            print('Неверный ввод')

    if pet_type == 'Утка':
        print('Доступные опции:\n1. Покормить животное\n2. Послушать животное\n3. Собрать яйца')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print(pet.feed())
        elif choise == 2:
            pet.listen()
        elif choise == 3:
            print(pet.collect_eggs())
        else:
            print('Неверный ввод')

while True:

    print('Выберете животное:')
    total_weight = 0
    heaviest_pet_type = ''
    heaviest_pet_name = ''
    heaviest_pet_weight = 0
    for pet in uncle_Joe_farm.keys():
        print(f'Животное {pet}: {uncle_Joe_farm[pet][0]}, цвет "{uncle_Joe_farm[pet][1]}", вес: {uncle_Joe_farm[pet][2]} кг.')
        total_weight += int(uncle_Joe_farm[pet][2])
        if uncle_Joe_farm[pet][2] > heaviest_pet_weight:
            heaviest_pet_type = uncle_Joe_farm[pet][0]
            heaviest_pet_name = uncle_Joe_farm[pet][1]
            heaviest_pet_weight = uncle_Joe_farm[pet][2]
    print(f'Общий вес животных на ферме: {total_weight}  кг., самое тяжелое животное: {heaviest_pet_type}, по кличке {heaviest_pet_name}, с весом {heaviest_pet_weight} кг.')
    pet = int(input('Ваш выбор: '))

    if uncle_Joe_farm.get(pet) == None:
        print('Неверный ввод')
    elif uncle_Joe_farm[pet][0] == 'Гусь':
        pet = Goose(uncle_Joe_farm[pet][1], uncle_Joe_farm[pet][2])
        action(pet,'Гусь')
    elif uncle_Joe_farm[pet][0] == 'Корова':
        pet = Cow(uncle_Joe_farm[pet][1], uncle_Joe_farm[pet][2])
        action(pet, 'Корова')
    elif uncle_Joe_farm[pet][0] == 'Баран':
        pet = Ram(uncle_Joe_farm[pet][1], uncle_Joe_farm[pet][2])
        action(pet, 'Баран')
    elif uncle_Joe_farm[pet][0] == 'Курица':
        pet = Chicken(uncle_Joe_farm[pet][1], uncle_Joe_farm[pet][2])
        action(pet, 'Курица')
    elif uncle_Joe_farm[pet][0] == 'Коза':
        pet = Goat(uncle_Joe_farm[pet][1], uncle_Joe_farm[pet][2])
        action(pet, 'Коза')
    elif uncle_Joe_farm[pet][0] == 'Утка':
        pet = Duck(uncle_Joe_farm[pet][1], uncle_Joe_farm[pet][2])
        action(pet, 'Утка')
    else:
        print('Что-то пошло не так')

    exit_choise = input('Продолжить? (да/нет):')
    if exit_choise != 'да':
        break