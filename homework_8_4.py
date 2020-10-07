"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую
структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class OfficeEquipment:  # прим.: принтер, сканер, ксерокс

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.flag = 0
        self.count = 0

    def weight_net(self):
        return self.weight_net

    def weight_brut(self):
        return self.weight_brut

    def inventory_id(self):
        return '_'.join(f'{self.flag: int}{self.count: int}')


class Printer(OfficeEquipment):  # принтер1, принт2, принт3
    count = 0

    def __init__(self, brand: str, model: str):
        super(Printer, self).__init__(brand, model)
        Printer.count += 1
        self.count = Printer.count
        self.flag = 1

    def is_color(self):
        return self.is_color

    def print_speed(self):
        return self.print_speed

    def __str__(self):
        return f"\nИнвентарный номер: {self.inventory_id()}\n" \
               f"Производитель: {self.brand}\n" \
               f"Модель: {self.model}\n" \
               f"Вес НЕТТО: {self.weight_net}\n" \
               f"Вес БРУТТО: {self.weight_brut}\n" \
               f"Цветность печати: {self.is_color}\n" \
               f"Скорость печати (кол-во страниц в минуту): {self.print_speed}\n" \



class Scanner(OfficeEquipment):
    count = 0

    def __init__(self, brand: str, model: str):
        super(Scanner, self).__init__(brand, model)
        Scanner.count += 1
        self.count = Scanner.count
        self.flag = 2

    def max_format(self):
        return self.max_format

    def resolution(self):
        return self.resolution

    def __str__(self):
        return f"\nИнвентарный номер: {self.inventory_id()}\n" \
               f"Производитель: {self.brand}\n" \
               f"Модель: {self.model}\n" \
               f"Вес НЕТТО: {self.weight_net}\n" \
               f"Вес БРУТТО: {self.weight_brut}\n" \
               f"Максимальный формат: {self.max_format}\n" \
               f"Максимальное разрешение: {self.resolution}\n" \



class Copier(OfficeEquipment):
    count = 0

    def __init__(self, brand: str, model: str):
        super(Copier, self).__init__(brand, model)
        Copier.count += 1
        self.count = Copier.count
        self.flag = 3

    def copy_speed(self):
        return self.copy_speed()

    def __str__(self):
        return f"\nИнвентарный номер: {self.inventory_id()}\n" \
               f"Производитель: {self.brand}\n" \
               f"Модель: {self.model}\n" \
               f"Вес НЕТТО: {self.weight_net}\n" \
               f"Вес БРУТТО: {self.weight_brut}\n" \
               f"Максимальный формат: {self.copy_speed}\n" \
            # Склад


class Warehouse:
    def __init__(self):
        self.items = []
        self.inv_count = 0

    def add_new_itm(self, new_itm: OfficeEquipment):
        self.inv_count += 1
        self.items.append(new_itm)

    def __str__(self):
        return "\n".join(str(itm) for itm in self.items)\



warehouse = Warehouse()

printer1 = Printer('Samsung', 'MFU')
printer1.is_color = 'Цветная'
printer1.print_speed = 20
printer1.weight_net = 25
printer1.weight_brut = 30
printer2 = Printer('Philips', 'MFU-5')
printer2.is_color = 'Ч.б'
printer2.print_speed = 10
printer2.weight_net = 15
printer2.weight_brut = 20

scanner1 = Scanner('HP', 'AAA')
scanner1.max_format = 'A4'
scanner1.resolution = '1200x1200'
scanner1.weight_net = 14
scanner1.weight_brut = 17

copier1 = Copier('Xerox', 'XXL')
copier1.copy_speed = 500
copier1.weight_net = 50
copier1.weight_brut = 60

warehouse.add_new_itm(printer1)
warehouse.add_new_itm(printer2)
warehouse.add_new_itm(copier1)
warehouse.add_new_itm(scanner1)

print(f'{"*" * 5}Количество продукции на складе: {warehouse.inv_count}')
print(f'{"-" * 3}Количество принтеров: {Printer.count}')
print(f'{"-" * 3}Количество сканеров: {Scanner.count}')
print(f'{"-" * 3}Количество копиров: {Copier.count}')

print(warehouse)
