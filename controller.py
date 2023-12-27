import change_notes
import menu

def start():
    while True:
        choice = change_notes.main_menu()
        match choice:
            case 1:
                change_notes.read_notes()
            case 2:
                menu.save_notes()
            case 3:
                menu.edit_note()
            case 4:
                menu.del_notes()
            case 5:
                menu.clear_notes()
            case 6:
                break