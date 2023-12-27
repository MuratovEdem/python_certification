from datetime import datetime
import json


note_list = []

class Note:
    def __init__(self):
        self.note_datetime = datetime.now().strftime('%d.%m.%y / %H:%M')
        self.note_name = input('Введите заголовок заметки: ')
        self.note_text = input('Введите текст заметки: ')

    def save_dict(self):
        data = {'Дата': self.note_datetime, 'Заголовок': self.note_name, 'Текст': self.note_text}
        note_list.append(data)


def save_notes():
    note = Note()
    note.save_dict()
    with open('notes.json', 'w') as file:
        json.dump(note_list, file)
    print(text.note_append)

def del_notes():
    with open('notes.json') as file:
        notes = json.load(file)
    del_name = input(text.note_name)
    for note in notes:
        if note['Заголовок'] == del_name:
            notes.remove(note)
            with open('notes.json', 'w') as file:
                json.dump(notes, file)
            return(print(text.note_del))
    return(print(text.wrong_notes))


def edit_note():
    with open('notes.json') as file:
        notes = json.load(file)
    edit_name = input(text.note_name)
    for note in notes:
        if note['Заголовок'] == edit_name:
            note['Заголовок'] = input(text.new_name_notes)
            note['Текст'] = input(text.edit_text)
            note['Дата'] = datetime.now().strftime('%d.%m.%y / %H:%M')
            with open('notes.json', 'w') as file:
                json.dump(notes, file)
            return (print(text.save_text))
    return (print(text.wrong_notes))

def clear_notes():
    note_list = []
    with open('notes.json', 'w') as file:
        json.dump(note_list, file)
    print(text.text_clear)


class text:
    menu = '''\nГлавное меню:
1. Посмотреть заметки
2. Создать заметку
3. Редактировать заметку
4. Удалить заметку
5. Очистить список заметок
6. Выход\n'''

    input_choice = 'Выберите пункт меню: '
    wrong_choice = 'Введено неверное число. Введите число от 1 до 6'
    note_append = 'Заметка добавлена'
    note_del = 'Заметка удалена'
    edit_text = 'Введите текст заметки: '
    save_text = 'Заметка успешно изменена'
    note_name = 'Введите заголовок: '
    wrong_notes = 'Такой заметки нет'
    text_clear = 'Список заметок очищен'
    new_name_notes = 'Введите новый заголовок: '