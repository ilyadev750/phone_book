from printactions import PrintActions


COLUMN_SEPARATORS = '                     |                 |                       |                       |                 |                 |\n'    
# COLUMNS =         '       Фамилия       |       Имя       |       Отчество        |     Организация       | Телефон рабочий | Телефон сотовый |\n'
BORDERS =           '_ _ _ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _ | _ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _ |\n'

COLUMNS = f"{'Фамилия':^21}|{'Имя':^17}|{'Отчество':^23}|{'Организация':^23}|{'Рабочий телефон':^17}|{'Телефон сотовый':^17}|\n" 

TABLE_TOP = [COLUMN_SEPARATORS, COLUMNS, BORDERS, COLUMN_SEPARATORS]

class PhoneBook:

    def __init__(self) -> None:
        self.new_filestring = None
        self.current_filestring = None
        self.all_filestrings = []
        self.surname = None
        self.name = None
        self.patronymic = None
        self.workplace = None
        self.work_phone_number = None
        self.personal_phone_number = None
        self.actions = PrintActions()

    def read_file_and_choose_actions(self):
        try:
            with open('phonebook.txt', 'r') as phonebook:
                for line in phonebook:
                    # isalnum()
                    if line.strip()[0] == '|' or line.strip()[0] == '_':
                        continue
                    else:
                        self.all_filestrings.append(line.strip())
            del self.all_filestrings[0]
            if self.all_filestrings:
                self.choose_the_action_with_phonebook()
            else:
                self.choose_the_action_with_empty_book()
        except FileNotFoundError as exc:
            with open('phonebook.txt', 'w') as phonebook:
                for row in TABLE_TOP:
                    phonebook.write(row)
            self.actions.print_actions_with_empty_book()

    def add_info_in_object(self):
        self.surname = self.input_text_info_and_check(column=self.surname, column_name='фамилию', length=19)
        self.name = self.input_text_info_and_check(column=self.name, column_name='имя', length=17)
        self.patronymic = self.input_text_info_and_check(column=self.patronymic, column_name='отчество', length=21)
        self.workplace = self.input_text_info_and_check(column=self.workplace, column_name='компанию работодателя', length=21)
        self.work_phone_number = self.input_phone_numbers_and_check(column=self.work_phone_number, column_name='рабочий телефон', length=15),
        self.personal_phone_number = self.input_phone_numbers_and_check(column=self.personal_phone_number, column_name='мобильный телефон', length=17)
    
    def choose_the_action_with_empty_book(self):
        while True:
            self.actions.print_actions_with_empty_book()
            action_number = int(input('Пожалуйста, введите номер действия: '))
            if action_number == 1:
                self.add_new_note()
            elif action_number == 2:
                break
            else:
                print('Некорректный номер действия!')



    def choose_the_action_with_phonebook(self):
        while True:
            self.actions.print_actions_with_phonebook()
            action_number = int(input('Пожалуйста, введите номер действия: '))
            if action_number == 1:
                self.print_all_notes()
            elif action_number == 2:
                self.find_note_by_one_param()
            elif action_number == 3:
                self.find_note_by_several_params()
            elif action_number == 4:
                self.change_note()
            elif action_number == 5:
                self.add_new_note()
            elif action_number == 6:
                self.find_and_delete_note()
            elif action_number == 7:
                break
            else:
                print('Некорректный номер действия!')

    def print_all_notes(self):
        pass

    def find_note_by_one_param(self):
        pass

    def find_note_by_several_params(self):
        pass

    def change_note(self):
        pass

    def find_and_delete_note(self):
        pass

    def add_new_note(self):
        self.add_info_in_object()
        self.all_filestrings.append(f'')
        new_note = f'{self.surname:^21}|{self.name:^17}|{self.patronymic:^23}|{self.workplace:^23}|{self.work_phone_number[0]:^17}|{self.personal_phone_number:^17}|\n'
        with open('phonebook.txt', 'a') as phonebook:
            phonebook.write(new_note)
            phonebook.write(BORDERS)
            phonebook.write(COLUMN_SEPARATORS)
        self.choose_the_action_with_phonebook()

    def input_text_info_and_check(self, column, column_name, length):
        while True:
            column = input(f'Введите {column_name} пользователя: ')
            if column.isalpha() and len(column) <= length:
                return column 
            else:
                print(f'Введите конкретно {column_name}. Без пробелов и цифр. Длина меньше или равно {length} знаков.')

    def input_phone_numbers_and_check(self, column, column_name, length):
        while True:
            column = input(f'Введите {column_name} пользователя без пробелов: ')
            if column.isdigit() and len(column) <= length:
                return column
            else:
                print(f'Введите конкретно {column_name}. Без букв. Длина меньше или равно {length} знаков.')


    def run(self):
        self.read_file_and_choose_actions()
