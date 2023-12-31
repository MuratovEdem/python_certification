from menu import text
import json

def input_choice():
    while True:
        number = input(text.input_choice)
        if number.isdigit() and 0 < int(number) < 7:
            return int(number)
        else:
            print(text.wrong_choice)


def main_menu():
    print(text.menu)
    return input_choice()

def read_notes():
    with open('notes.json') as file:
        notes = sorted(json.load(file), key=lambda d: d['Дата'])
        count = 1
        for note in notes:
            print()
            print(f'Заметка {count}')
            for value in note.values():
                print(value)
            count += 1
            print()