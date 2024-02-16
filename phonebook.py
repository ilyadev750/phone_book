import re
import tabulate
from printactions import PrintActions

COLUMN_SEPARATORS = '                     |                 |                       |                       |                 |                 |\n'    
# COLUMNS =         '       Фамилия       |       Имя       |       Отчество        |     Организация       | Телефон рабочий | Телефон сотовый |\n'
BORDERS =           '_ _ _ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _ | _ _ _ _ _ _ _ _ _ _ _ |_ _ _ _ _ _ _ _ _ _ _ _|_ _ _ _ _ _ _ _ _| _ _ _ _ _ _ _ _ |\n'

COLUMNS = f"{'Фамилия':^21}|{'Имя':^17}|{'Отчество':^23}|{'Организация':^23}|{'Рабочий телефон':^17}|{'Телефон сотовый':^17}|\n" 
TABLE_TOP = [COLUMN_SEPARATORS, COLUMNS, BORDERS, COLUMN_SEPARATORS]
INPUT_MESSAGE_1 = 'Пожалуйста, введите номер действия: '
INPUT_MESSAGE_2 = 'Введите номер записи, которую хотите изменить. Введите 0, чтобы вернуться обратно '
INPUT_MESSAGE_3 = 'Номер параметра: '
INPUT_MESSAGE_4 = 'Введите номер записи, которую хотите удалить. Введите 0, чтобы вернуться обратно '

class PhoneBook:

    def __init__(self, filename):
        self.filename = filename
        self.all_filestrings = []
        self.surname = None
        self.name = None
        self.patronymic = None
        self.workplace = None
        self.work_phone_number = None
        self.personal_phone_number = None
        self.actions = PrintActions()
        self.line_number = 5
        self.note_number = 1
        self.finded_notes = []
        self.key_word = None
        self.columns_for_printing = ['Номер', 'Фамилия', 'Имя', 'Отчество', 'Организация', 'Телефон рабочий', 'Телефон сотовый']

    def read_file_and_choose_actions(self):
        """Функция считывает файл phonebook.txt и сохраняет данные в атрибуте self.all_filestrings, игнорируя 
        шапку таблицы и пробельные строки. После предлагает выбор действия пользователю. Если файл не существует,
        то создается новый. """
        print('Начало работы с телефонной книгой')
        try:
            with open(self.filename, 'r') as phonebook:
                for i, line in enumerate(phonebook, 1):
                    if i == self.line_number:
                        self.all_filestrings.append(line)
                        self.line_number += 3
                    else:
                        continue
            if self.all_filestrings:
                self.choose_the_action_with_phonebook()
            else:
                self.choose_the_action_with_empty_book()
        except FileNotFoundError as exc:
            with open(self.filename, 'w') as phonebook:
                for row in TABLE_TOP:
                    phonebook.write(row)
            self.choose_the_action_with_empty_book()

    def check_user_action_input(self, message):
        """Проверка введеных данных со 
        стороны пользователя."""
        try:
            action_number = int(input(message))
        except ValueError as exc:
            action_number = 1000
        return action_number

    def choose_the_action_with_empty_book(self):
        """Выбор действий в случае, 
        если файл пустой."""
        while True:
            self.actions.print_actions_with_empty_book()
            action_number = self.check_user_action_input(message=INPUT_MESSAGE_1)
            if action_number == 1:
                self.add_new_note()
                self.choose_the_action_with_phonebook()
                break
            elif action_number == 2:
                break
            else:
                print('Некорректный номер действия!')

    def choose_the_action_with_phonebook(self):
        """Выбор действий в случае, если 
        файл содержит хотя бы одну запись."""
        while True:
            self.actions.print_actions_with_phonebook()
            action_number = self.check_user_action_input(message=INPUT_MESSAGE_1)
            if action_number == 1:
                self.print_all_notes()
            elif action_number == 2:
                self.add_new_note()
            elif action_number == 3:
                self.find_notes_by_one_param()
            elif action_number == 4:
                self.find_note_by_several_params()
            elif action_number == 5:
                print('Работа с телефонной книгой закончена!')
                break
            else:
                print('Некорректный номер действия!')

    def find_notes_by_one_param(self):
        """Функция в начале производит сброс параметров. Далее пользователь выбриает критерий, по которому
        хочет найти записи. Запускается поиск информации с проверками вводимых данных"""
        self.reset_params()
        self.actions.print_actions_find_notes_by_one_param()
        action_number = self.check_user_action_input(message=INPUT_MESSAGE_3)
        if 1 <= action_number <= 3:
            self.key_word = self.input_text_info_and_check(column=self.key_word, column_name='выбранный параметр', length=23)
            self.prepare_finded_lines_and_choose_action()
        elif action_number == 4:
            self.key_word = self.input_company_info_and_check(column=self.key_word, column_name='выбранный параметр', length=23)
            self.prepare_finded_lines_and_choose_action()
        elif 5 <= action_number <= 6:
            self.key_word = self.input_phone_numbers_and_check(column=self.key_word, column_name='номер телефона', length=17)
            self.prepare_finded_lines_and_choose_action()
        elif action_number == 7:
            return
        else:
            print('Некорректный номер действия! Возврат в предыдущее меню')

    def find_note_by_several_params(self):
        """Запуск поиска информации  по нескольким критериям
        со сбросом параметров и проверками вводимых данных"""
        self.reset_params()
        self.actions.print_actions_find_notes_by_several_params()
        query = input('Строка запроса: ')
        query = self.prepare_query_list(query=query)
        number_of_matches = 0
        for line in self.all_filestrings:
            for param in query:
                if param in line:
                    number_of_matches += 1
            if number_of_matches == len(query):
                self.finded_notes.append(line)
            number_of_matches = 0
        if self.finded_notes:
            self.print_beautiful_notes(lines=self.finded_notes)
            self.choose_the_action_with_finded_notes()
        else:
            print('По вашему запросу записи не найдены!')

    def choose_the_action_with_finded_notes(self):
        """Выбор действий после успешного поиска записей. Найденные записи сохраняются в атрибуте self.finded_notes"""
        while True:
            self.actions.print_actions_with_finded_notes_before_changing()
            action_number = self.check_user_action_input(message=INPUT_MESSAGE_1)
            if action_number == 1:
                self.change_note()
                break
            elif action_number == 2:
                self.delete_note()
                break
            elif action_number == 3:
                print('Возврат в предыдущее меню')
                break
            else:
                print('Номер записи некорректен')

    def delete_note(self):
        """Выбор записи из self.finded_notes, которую нужно удалить"""
        while True:
            note_number = self.check_user_action_input(message=INPUT_MESSAGE_4)
            if note_number == 0:
                break
            elif note_number <= len(self.finded_notes):
                self.all_filestrings.remove(self.finded_notes[note_number - 1])
                del self.finded_notes[note_number - 1]
                if self.finded_notes:
                    self.print_beautiful_notes(lines=self.finded_notes)
                self.choose_the_action_after_deleting()
                break
            else:
                print('Некорректный номер записи!')

    def choose_the_action_after_deleting(self):
        """Перезаписать файл phonebook.txt или внести оставшиеся записи из self.finded_notes
        в очередь на удаление"""
        if not self.finded_notes:
            self.sort_notes_and_rewrite_file()
        else:
            while True:
                self.actions.print_actions_after_deleting()
                action_number = self.check_user_action_input(message=INPUT_MESSAGE_1)
                if action_number == 1:
                    self.sort_notes_and_rewrite_file()
                    break
                elif action_number == 2:
                    self.delete_note()
                    break
                else:
                    print('Некорректный номер записи!')

    def change_note(self):
        """Выбрать запись, которую нужно изменить."""
        while True:
            note_number = self.check_user_action_input(message=INPUT_MESSAGE_2)
            if note_number == 0:
                break
            elif note_number <= len(self.finded_notes):
                print('Добавьте поочередно данные согласно их типу')
                self.add_info_in_object()
                self.all_filestrings.remove(self.finded_notes[note_number - 1])
                self.all_filestrings.append(f'{self.surname:^21}|{self.name:^17}|{self.patronymic:^23}|{self.workplace:^23}|{self.work_phone_number[0]:^17}|{self.personal_phone_number:^17}|\n')
                self.finded_notes[note_number - 1] = f'{self.surname:^21}|{self.name:^17}|{self.patronymic:^23}|{self.workplace:^23}|{self.work_phone_number[0]:^17}|{self.personal_phone_number:^17}|\n'
                self.print_beautiful_notes(lines=self.finded_notes)
                self.choose_the_action_after_changing()
                break
            else:
                print('Некорректный номер записи!')

    def choose_the_action_after_changing(self):
        """Сохранить новые записи в файле или продолжить изменение записей"""
        while True:
            self.actions.print_actions_with_finded_notes_after_changing()
            action_number = self.check_user_action_input(message=INPUT_MESSAGE_1)
            if action_number == 1:
                self.sort_notes_and_rewrite_file()
                break
            elif action_number == 2:
                self.change_note()
                break
            else:
                print('Номер записи некорректен')

    def prepare_finded_lines_and_choose_action(self):
        """Поиск информации из содержимого файла"""
        for line in self.all_filestrings:
            if self.key_word in line:
                self.finded_notes.append(line)
                self.note_number += 1
        if self.finded_notes:
            print('Найденные данные')
            self.print_beautiful_notes(lines=self.finded_notes)
            self.choose_the_action_with_finded_notes()
        else:
            print('Записи на выбранному параметру не найдены')

    def prepare_query_list(self, query):
        """Подготовка списка query, который содержит ключевые слова для поиска"""
        query = query.strip()
        query = re.sub('\s+', ' ', query)
        query = list(query.split())
        return query

    def reset_params(self):
        """Сброс параметров"""
        self.key_word = None
        self.finded_notes = []
        self.note_number = 1

    def print_beautiful_notes(self, lines):
        """Красивый вывод найденных записей на консоль"""
        printing_filestrings = [self.columns_for_printing]
        for i, line in enumerate(lines, 1):
            line = line.replace('|', ' ')
            line = re.sub('\s{2,}', '  ', line)
            line = list(line.split("  "))
            line[0] = i
            printing_filestrings.append(line)
        results = tabulate.tabulate(printing_filestrings)
        print(results)

    def add_info_in_object(self):
        """Добавление информации о новой записи в атрибуты экземпляра класса"""
        self.surname = self.input_text_info_and_check(column=self.surname, column_name='фамилию', length=19)
        self.name = self.input_text_info_and_check(column=self.name, column_name='имя', length=17)
        self.patronymic = self.input_text_info_and_check(column=self.patronymic, column_name='отчество', length=21)
        self.workplace = self.input_company_info_and_check(column=self.workplace, column_name='компанию работодателя', length=21)
        self.work_phone_number = self.input_phone_numbers_and_check(column=self.work_phone_number, column_name='рабочий телефон', length=15),
        self.personal_phone_number = self.input_phone_numbers_and_check(column=self.personal_phone_number, column_name='мобильный телефон', length=17)

    def add_new_note(self):
        """Добавление записи в атрибут self.all_filestrings с сортировкой. 
        Новая перезапись файла для сохранения алфавитного порядка записей"""
        print('Добавьте поочередно данные согласно их типу')
        self.add_info_in_object()
        new_note = f'{self.surname:^21}|{self.name:^17}|{self.patronymic:^23}|{self.workplace:^23}|{self.work_phone_number[0]:^17}|{self.personal_phone_number:^17}|\n'
        self.all_filestrings.append(new_note)
        self.sort_notes_and_rewrite_file()

    def print_all_notes(self):
        """Вывод всех записей из телефонной книги"""
        print('\nВсе записи телефонной книги: ')
        self.print_beautiful_notes(lines=self.all_filestrings)
        print('Возврат в предыдущее меню')

    def input_text_info_and_check(self, column, column_name, length):
        """Ввод и проверка ФИО записей"""
        while True:
            column = input(f'Введите {column_name} пользователя: ')
            if column.isalpha() and len(column) <= length:
                return column.capitalize() 
            else:
                print(f'Введите конкретно {column_name}. Без пробелов и цифр. Длина меньше или равно {length} знаков.')

    def input_company_info_and_check(self, column, column_name, length):
        """Ввод и проверка компании"""
        while True:
            column = input(f'Введите {column_name} пользователя: ')
            if column and not column.isdigit():
                return column.capitalize() 
            else:
                print(f'Введите конкретно {column_name}. Без пробелов и цифр. Длина меньше или равно {length} знаков.')

    def input_phone_numbers_and_check(self, column, column_name, length):
        """Ввод и проверка телефонных номеров"""
        while True:
            column = input(f'Введите {column_name} пользователя без пробелов: ')
            if column.isdigit() and len(column) <= length:
                return column
            else:
                print(f'Введите конкретно {column_name}. Без букв. Длина меньше или равно {length} знаков.')

    def sort_notes_and_rewrite_file(self):
        """Сортировка записей и запись в файл"""
        self.all_filestrings = sorted(self.all_filestrings, key=lambda x: x.strip().split()[0])
        with open(self.filename, 'w') as phonebook:
            for row in TABLE_TOP:
                phonebook.write(row)
            for row in self.all_filestrings:
                phonebook.write(row)
                phonebook.write(BORDERS)
                phonebook.write(COLUMN_SEPARATORS)
        print('Файл успешно обновлен!')

    def run(self):
        """Запуск программы"""
        self.read_file_and_choose_actions()
