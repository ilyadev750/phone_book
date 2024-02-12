COLUMN_SEPARATORS = '                     |                 |                       |                       |                 |                 |\n'    
# COLUMNS =         '       Фамилия       |       Имя       |       Отчество        |     Организация       | Телефон рабочий | Телефон сотовый |\n'
BORDERS =           '_ _ _ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _ | _ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _ |\n'

COLUMNS = f"{'Фамилия':^21}|{'Имя':^17}|{'Отчество':^23}|{'Организация':^23}|{'Рабочий телефон':^17}|{'Телефон сотовый':^17}|\n" 

TABLE_TOP = [COLUMN_SEPARATORS, COLUMNS, BORDERS, COLUMN_SEPARATORS]

class PhoneBook:

    def __init__(self) -> None:
        self.new_filestring = None
        self.current_filestring = None
        self.all_filestrings = None

    def read_file(self):
        try:
            with open('phonebook.txt', 'r') as phonebook:
                self.all_filestrings = phonebook.readlines()
        except FileNotFoundError as exc:
            with open('phonebook.txt', 'w') as phonebook:
                for row in TABLE_TOP:
                    phonebook.write(row)
    
    def add_new_note(self):
        surname = self.input_info_and_check(column_name='фамилию', length=19)
        name = self.input_info_and_check(column_name='имя', length=17)
        patronymic = self.input_info_and_check(column_name='отчество', length=21)
        workplace = self.input_info_and_check(column_name='компанию работодателя', length=21)
        working_phone_number = self.input_phone_numbers_and_check(column_name='рабочий телефон', length=15),
        personal_phone_number = self.input_phone_numbers_and_check(column_name='мобильный телефон', length=17)

        new_note = f'{surname:^21}|{name:^17}|{patronymic:^23}|{workplace:^23}|{working_phone_number[0]:^17}|{personal_phone_number:^17}|\n'
        with open('phonebook.txt', 'a') as phonebook:
            phonebook.write(new_note)
            phonebook.write(BORDERS)
            phonebook.write(COLUMN_SEPARATORS)

    def input_info_and_check(self, column_name, length):
        while True:
            info = input(f'Введите {column_name} пользователя: ')
            if info.isalpha() and len(info) <= length:
                return info
            else:
                print(f'Введите конкретно {column_name}. Без пробелов и цифр. Длина меньше или равно {length} знаков.')

    def input_phone_numbers_and_check(self, column_name, length):
        while True:
            info = input(f'Введите {column_name} пользователя без пробелов: ')
            if info.isdigit() and len(info) <= length:
                return info
            else:
                print(f'Введите конкретно {column_name}. Без букв. Длина меньше или равно {length} знаков.')

    def run(self):
        self.read_file()
        self.add_new_note()