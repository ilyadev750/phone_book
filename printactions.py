
class PrintActions:

    def print_actions_with_phonebook(self):
        print('\nДоступные действия: ')
        print('1 - Вывести все записи телефонной книги')
        print('2 - Добавить запись в книгу')
        print('3 - Найти запись по одному параметру')
        print('4 - Найти запись по нескольким параметрам')
        print('5 - Закончить работу с телефонной книгой')

    def print_actions_with_finded_notes_before_changing(self):
        print('\nДействия с полученными данными: ')
        print('1 - Добавить изменения в записи')
        print('2 - Удалить полученные записи')
        print('3 - Вернуться в исходное меню')

    def print_actions_with_finded_notes_after_changing(self):
        print('\nЗаписи готовы к сохранению в файл')
        print('1 - Сохранить записи в файл')
        print('2 - Продолжить изменять полученные записи')

    def print_actions_after_deleting(self):
        print('\nФайл готов к сохранению без удаленных записей')
        print('1 - Сохранить обновленный файл')
        print('2 - Внести оставшиеся записи в очередь на удаление')

    def print_actions_with_empty_book(self):
        print('\nК сожалению, телефонная книга пуста. Доступные действия: ')
        print('1 - Добавить новую запись в книгу')
        print('2 - Закончить работу с телефонной книгой')

    def print_actions_find_notes_by_one_param(self):
        print('\nВведите номер параметра, по какому хотите найти записи: ')
        print('1 - по фамилии')
        print('2 - по имени')
        print('3 - по отчеству')
        print('4 - по организации')
        print('5 - по рабочему номеру телефона')
        print('6 - по мобильному номеру телефона')
        print('7 - выйти в исходное меню')

    def print_actions_find_notes_by_several_params(self):
        print('\nВведите несколько параметров для поиска информации'
              'без запятых.')
        print('Например: Иванов Иван Иванович 89158887744')
