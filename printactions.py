
class PrintActions:

    def print_actions_with_phonebook(self):
        print('1 - Вывести все записи телефонной книги')
        print('2 - Добавить запись в книгу')
        print('3 - Найти запись по одному параметру')
        print('4 - Найти запись по нескольким параметрам')
        print('5 - Закончить работу с телефонной книгой')

    def print_actions_with_finded_notes_before_changing(self):
        print('1 - Добавить изменения в записи')
        print('2 - Удалить полученные записи')
        print('3 - Вернуться в исходное меню')

    def print_actions_with_finded_notes_after_changing(self):
        print('1 - Добавить изменения в записи')
        print('2 - Сохранить записи в файл')
        print('3 - Отменить изменения и вернуться в исходное меню')

    def print_actions_with_empty_book(self):
        print('1 - Добавить новую запись в книгу')
        print('2 - Закончить работу с телефонной книгой')

    def print_actions_find_notes_by_one_param(self):
        print('Введите номер параметра, по какому хотите найти записи: ')
        print('1 - по фамилии')
        print('2 - по имени')
        print('3 - по отчеству')
        print('4 - по организации')
        print('5 - по рабочему номеру телефона')
        print('6 - по мобильному номеру телефона')
        print('7 - выйти в исходное меню')