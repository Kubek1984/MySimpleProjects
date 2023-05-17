import random
from tkinter import *
from tkinter import ttk
import sys

navigation_frame: Frame
asside_frame: Frame
num_list: []
char_list: []
letters_list: []
object_dictionary: {}
generate_password: StringVar
bottom_frame: Frame
frame_global: Frame
select_object_name: StringVar


# select_edit_object

# name_entry_string : StringVar
# psswd_entry_string : StringVar


class PasswordObject:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def as_string(self):
        return f'{self.name} : {self.password}\n'


psswd_object: PasswordObject


def quit():
    sys.exit()


def navigation(root):
    pad_y_value = 15
    pad_x_value = 30
    width_button = 11
    button_color = 'orange'
    button_text_color = 'orange'
    frame = Frame(root, width=200, height=500, bg='black')
    frame.grid_propagate(False)
    add_new_button = Button(frame, text='Add New', width=width_button, bg='black', fg=button_text_color, borderwidth=4,
                            highlightbackground=button_color, command=click_on_add_new)
    add_new_button.grid(padx=pad_x_value, pady=pad_y_value)
    show_list_button = Button(frame, text='Show List', width=width_button, bg='black', fg=button_text_color,
                              borderwidth=4, highlightbackground=button_color, command=click_on_show_list)
    show_list_button.grid(padx=pad_x_value, pady=pad_y_value)
    delete_item_button = Button(frame, text='Delete Item', width=width_button, bg='black', fg=button_text_color,
                                borderwidth=4, highlightbackground=button_color, command=click_on_delete_frame)
    delete_item_button.grid(padx=pad_x_value, pady=pad_y_value)
    edit_item_button = Button(frame, text='Edit Item', width=width_button, bg='black', fg=button_text_color,
                              borderwidth=4, highlightbackground=button_color, command=click_on_edit_frame)
    edit_item_button.grid(padx=pad_x_value, pady=pad_y_value)
    search_button = Button(frame, text='Search', width=width_button, bg='black', fg=button_text_color, borderwidth=4,
                           highlightbackground=button_color, command=click_on_search_frame)
    search_button.grid(padx=pad_x_value, pady=pad_y_value)
    quit_button = Button(frame, text='Quit', width=width_button, bg='black', fg=button_text_color, borderwidth=4,
                         highlightbackground=button_color, command=quit)
    quit_button.grid(padx=pad_x_value, pady=pad_y_value)
    return frame


def show_list():
    pad_y_value = 10
    pad_x_value = 0
    frame = Frame(asside_frame, bg='black')
    show_list_listbox = Listbox(frame, bg='black', fg='white', height=300, width=300)
    for value in object_dictionary.values():
        show_list_listbox.insert(END, value.name)
        show_list_listbox.insert(END, value.password)
        show_list_listbox.insert(END, '')
    show_list_listbox.grid(pady=pad_y_value, padx=pad_x_value)

    return frame


def clear_bottom1():
    for child in bottom_frame.winfo_children():
        child.destroy()


def clear_right_side():
    # add_new_frame(asside_frame).grid_forget()
    for child in asside_frame.winfo_children():
        child.destroy()
    clear_bottom1()
    try:
        show_list().grid_forget()
    except:
        pass


def click_on_show_list():
    clear_right_side()

    frame = show_list()
    frame.grid()


def click_on_add_new():
    clear_right_side()
    add_new_frame().grid()


def click_on_add_save():
    add_save(psswd_object)
    clear_bottom1()
    # label - file was saved
    # reset_function() - for upper menu


def click_on_make_object(letter, digit, char, entry_string):
    global psswd_object, frame_global
    if letter == 0 and digit == 0 and char == 0:
        info = 'Password can\'t be empty'
        generate_password.set(info)
    elif len(entry_string.strip()) == 0:
        info = 'PLease fill in all fields'
        generate_password.set(info)
    else:
        try:
            clear_bottom1()
        except:
            pass
        psswd = make_password(letter, digit, char)
        generate_password.set(psswd)
        psswd_object = PasswordObject(entry_string, psswd)
        frame_global = bottom_option_frame()
        frame_global.grid()


def bottom_option_frame():
    pad_y_value = 10
    pad_x_value = 0
    width_button = 15
    button_color = 'orange'
    button_text_color = 'orange'
    frame = Frame(bottom_frame, bg='black')
    add_button = Button(frame, text='Add & Save', command=click_on_add_save, width=width_button, bg='black',
                        fg=button_text_color, borderwidth=4, highlightbackground=button_color)
    add_button.grid(pady=pad_y_value, padx=pad_x_value)
    reset_button = Button(frame, text='Reset', command=click_on_add_new, width=width_button, bg='black',
                          fg=button_text_color, borderwidth=4, highlightbackground=button_color)
    reset_button.grid(pady=pad_y_value, padx=pad_x_value)
    return frame


def click_on_edit_frame():
    clear_right_side()
    edit_frame().grid()


def edit_frame():
    pad_y_value = 10
    pad_x_value = 0
    width_button = 15
    button_color = 'orange'
    button_text_color = 'orange'
    global dictionary_listbox, edit_button
    frame = Frame(asside_frame, bg='black')
    dictionary_listbox = Listbox(frame, width=280, bg='black', fg='white')
    for value in object_dictionary.values():
        dictionary_listbox.insert(END, value.name)
    dictionary_listbox.bind('<<ListboxSelect>>', on_select_edit)
    dictionary_listbox.grid(pady=pad_y_value, padx=pad_x_value)
    edit_button = Button(bottom_frame, text='Edit', command=click_on_edit, width=width_button, bg='black',
                         fg=button_text_color, borderwidth=4, highlightbackground=button_color)
    edit_button.grid(pady=pad_y_value, padx=pad_x_value)
    return frame


def edit():
    for key, value in object_dictionary.items():
        if value.name == select_edit_object:
            click_on_edit_frame()


def click_on_edit_save(name, psswd):
    obj = select_edit_object
    obj.name = name
    obj.password = psswd
    with open('dataBase.txt', 'w') as fileObject:
        for key, value in object_dictionary.items():
            fileObject.write(f'{key}:::{value.name}:::{value.password}\n')
    click_on_edit_frame()


def bottom_edit_frame():
    pad_y_value = 10
    pad_x_value = 0
    width_button = 15
    button_color = 'orange'
    button_text_color = 'orange'

    frame = Frame(bottom_frame, bg='black')
    edit_button = Button(frame, text='Edit', command=click_on_edit, width=width_button, bg='black',
                         fg=button_text_color, borderwidth=4,
                         highlightbackground=button_color)
    edit_button.grid(pady=pad_y_value, padx=pad_x_value)
    name_entry = Entry(frame, bg='black', fg='white')
    name_entry.insert(0, select_edit_object.name)
    name_entry.grid(pady=pad_y_value, padx=pad_x_value)
    psswd_entry = Entry(frame, bg='black', fg='white')
    psswd_entry.insert(0, select_edit_object.password)
    psswd_entry.grid(pady=pad_y_value, padx=pad_x_value)
    edit_save_button = Button(frame, text='Save changes',
                              command=lambda: click_on_edit_save(name_entry.get(), psswd_entry.get()),
                              width=width_button, bg='black', fg=button_text_color, borderwidth=4,
                              highlightbackground=button_color)
    edit_save_button.grid(pady=pad_y_value, padx=pad_x_value)

    return frame


def click_on_edit():
    clear_bottom1()
    bottom_edit_frame().grid()


def on_select_edit(event):
    global select_edit_object
    selected_item_index = dictionary_listbox.curselection()  # pobieramy indeks zaznaczonego elementu
    if selected_item_index:  # sprawdzamy, czy indeks został pobrany (jeśli użytkownik nie zaznaczył żadnego elementu, to curselection() zwróci pusty tuple)
        selected_item_index = int(
            selected_item_index[0])  # pobieramy pierwszy (i jedyny) indeks z tuple i zamieniamy na int
        selected_item = dictionary_listbox.get(selected_item_index)  # pobieramy wartość zaznaczonego elementu
        object_ = check_object_name(selected_item)
        select_edit_object = object_


def click_on_delete_frame():
    clear_right_side()
    delete_frame().grid()


def delete_frame():
    pad_y_value = 10
    pad_x_value = 0
    width_button = 15
    button_color = 'orange'
    button_text_color = 'orange'
    global dictionary_listbox, object_info_label, delete_button
    frame = Frame(asside_frame, bg='black')
    dictionary_listbox = Listbox(frame, width=280, bg='black', fg='white')
    for value in object_dictionary.values():
        dictionary_listbox.insert(END, value.name)
    dictionary_listbox.bind('<<ListboxSelect>>', on_select)
    dictionary_listbox.grid(pady=pad_y_value, padx=pad_x_value)
    object_info_label = Label(bottom_frame, text='', bg='black', fg='white')
    object_info_label.grid(pady=pad_y_value, padx=pad_x_value)
    delete_button = Button(bottom_frame, text='Delete', command=click_on_delete, width=width_button, bg='black',
                           fg=button_text_color, borderwidth=4, highlightbackground=button_color)
    delete_button.grid(pady=pad_y_value, padx=pad_x_value)
    return frame


def delete():
    for key, value in object_dictionary.items():
        if value.name == select_object_name:
            del (object_dictionary[key])
            with open('dataBase.txt', 'w') as fileObject:
                for key, value in object_dictionary.items():
                    fileObject.write(f'{key}:::{value.name}:::{value.password}\n')
            break
    click_on_delete_frame()


def click_on_delete():
    delete()


def on_select(event):
    global select_object_name
    selected_item_index = dictionary_listbox.curselection()  # pobieramy indeks zaznaczonego elementu
    if selected_item_index:  # sprawdzamy, czy indeks został pobrany (jeśli użytkownik nie zaznaczył żadnego elementu, to curselection() zwróci pusty tuple)
        selected_item_index = int(
            selected_item_index[0])  # pobieramy pierwszy (i jedyny) indeks z tuple i zamieniamy na int
        selected_item = dictionary_listbox.get(selected_item_index)  # pobieramy wartość zaznaczonego elementu
        select_object_name = StringVar()
        object_ = check_object_name(selected_item)
        name = object_.name
        select_object_name = name
        psswd = object_.password
        object_info_label.config(text=f'{name}\n{psswd}')  # ustawiamy wartość etykiety na wartość zaznaczonego elementu


def click_on_search_frame():
    clear_right_side()
    search_frame().grid()


def bottom_search_frame(search_list):
    pad_y_value = 10
    pad_x_value = 0
    frame = Frame(bottom_frame, bg='black')
    if len(search_list) == 0:
        empty_list_label = Label(frame, bg='black', fg='white', text='No match found! Try again.')
        empty_list_label.grid(pady=pad_y_value, padx=pad_x_value)
    else:
        for item in search_list:
            item_label = Label(frame, bg='black', fg='white', text=f'Name : {item.name}\nPsswd : {item.password}')
            item_label.grid(pady=pad_y_value, padx=pad_x_value)

    return frame


def click_on_search_button(phrase):
    search_list = []
    for key, value in object_dictionary.items():
        if phrase in value.name:
            search_list.append(value)
    clear_bottom1()
    bottom_search_frame(search_list).grid()


def search_frame():
    pad_y_value = 10
    pad_x_value = 0
    width_button = 15
    button_color = 'orange'
    button_text_color = 'orange'
    frame = Frame(asside_frame, bg='black')
    what_phrase_label = Label(frame, bg='black', fg='white', text='What phrase you looking for ?')
    what_phrase_label.grid(row=0, column=0, pady=pad_y_value, padx=pad_x_value)
    looking_for_entry = Entry(frame, bg='black', fg='white')
    looking_for_entry.grid(row=0, column=1, pady=pad_y_value, padx=pad_x_value)
    search_button = Button(frame, text='Search', command=lambda: click_on_search_button(looking_for_entry.get()),
                           width=width_button, bg='black', fg=button_text_color, borderwidth=4,
                           highlightbackground=button_color)
    search_button.grid(row=1, columnspan=2, pady=pad_y_value, padx=pad_x_value)

    return frame


def make_password(letter, digit, char):
    string = ''
    for i in range(letter):
        rand = random.randint(0, len(letters_list) - 1)
        letter = letters_list[rand]
        string += letter
    for i in range(char):
        rand = random.randint(0, len(char_list) - 1)
        character = char_list[rand]
        string += character
    for i in range(digit):
        rand = random.randint(0, len(num_list) - 1)
        dig = num_list[rand]
        string += dig

    psswd_list = list(string)
    password = ''
    for i in range(0, len(psswd_list)):
        rand = random.randint(0, len(psswd_list) - 1)
        character = psswd_list[rand]
        password += character
        psswd_list.remove(character)
    return password


def add_save(object):
    # ----------------- Add Object ---------------------------

    id_index = 0
    if len(object_dictionary) > 0:
        last_id = []
        for key in object_dictionary.keys():
            last_id.append(key)
        last_key = last_id[-1]
        id_index = int(last_key) + 1
    else:
        id_index = 1

    object_dictionary[id_index] = object

    # -------------------- Save Object ------------------------------

    with open('dataBase.txt', 'w') as fileObject:
        for key, value in object_dictionary.items():
            fileObject.write(f'{key}:::{value.name}:::{value.password}\n')

    # ------------------ Set psswd Label ----------------------------

    info_add_save = 'File saved successfuly'
    generate_password.set(info_add_save)


def check_object_name(name):
    for value in object_dictionary.values():
        if value.name == name:
            return value


def load():
    object_dictionary.clear()
    with open('dataBase.txt', 'r') as fileObject:
        for line in fileObject:
            mk_list = line.split(':::')
            id = mk_list[0]
            name = mk_list[1]
            psswd = mk_list[2].strip()
            object = PasswordObject(name, psswd)
            object_dictionary[id] = object


def add_new_frame():
    # ---------------------- Front Settings ---------------------
    pad_y_value = 10
    pad_x_value = 0
    width_button = 15
    button_color = 'orange'
    button_text_color = 'orange'

    frame = Frame(asside_frame, bg='black')
    global generate_password, psswd_label
    generate_password = StringVar()
    # --------------Letters Field---------------------------------

    letters_nr_label = Label(frame, bg='black', fg='white', text='How many letters : ')
    letters_nr_label.grid(row=0, column=0, pady=pad_y_value, padx=pad_x_value)
    letters_nr = StringVar()
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    letters_nr_combobox = ttk.Combobox(frame, textvariable=letters_nr, values=numbers_list, width=10)
    letters_nr_combobox.set('0')
    letters_nr_combobox.grid(row=0, column=1, pady=pad_y_value, padx=pad_x_value)

    # -------------Digits Field---------------------------------------

    digits_nr_label = Label(frame, bg='black', fg='white', text='How many digits : ')
    digits_nr_label.grid(row=1, column=0, pady=pad_y_value, padx=pad_x_value)
    digits_nr = StringVar()
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digits_nr_combobox = ttk.Combobox(frame, textvariable=digits_nr, values=numbers_list, width=10)
    digits_nr_combobox.set('0')
    digits_nr_combobox.grid(row=1, column=1, pady=pad_y_value, padx=pad_x_value)

    # --------------- Characters Field -------------------------------

    characters_nr_label = Label(frame, bg='black', fg='white', text='How many characters : ')
    characters_nr_label.grid(row=2, column=0, pady=pad_y_value, padx=pad_x_value)
    characters_nr = StringVar()
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    characters_nr_combobox = ttk.Combobox(frame, textvariable=characters_nr, values=numbers_list, width=10)
    characters_nr_combobox.set('0')
    characters_nr_combobox.grid(row=2, column=1, pady=pad_y_value, padx=pad_x_value)

    # --------------- Website Name Field ---------------------------
    website_name_label = Label(frame, bg='black', fg='white', text='This password is for : ')
    website_name_label.grid(row=3, column=0, pady=pad_y_value, padx=pad_x_value)
    entry_string = StringVar()
    website_name_entry = Entry(frame, bg='black', fg='white', textvariable=entry_string)
    # entry_string.set('https://')
    website_name_entry.grid(row=3, column=1, pady=pad_y_value, padx=pad_x_value)
    # --------------- Generate Button -------------------------------

    generate_button = Button(frame, text='Generate Password',
                             command=lambda: click_on_make_object(int(letters_nr.get()), int(digits_nr.get()),
                                                                  int(characters_nr.get()), entry_string.get()),
                             width=width_button, bg='black', fg=button_text_color, borderwidth=4,
                             highlightbackground=button_color)
    generate_button.grid(row=4, columnspan=2)

    # ---------------Password Label ---------------------------------

    psswd_label = Label(frame, bg='black', fg='white', textvariable=generate_password)
    psswd_label.grid(row=5, columnspan=2)
    return frame


def main():
    global navigation_frame, asside_frame, bottom_frame, num_list, char_list, letters_list, object_dictionary

    # ----------Generating Dictionary----

    alphabet = 'abcdefghijklmnoprstuqwxyz'
    digits = '0 1 2 3 4 5 6 7 8 9'
    lower_list = list(alphabet)
    upper_list = []
    for i in lower_list:
        item = i.upper()
        upper_list.append(item)
    num_list = digits.split(' ')
    characters = '@ # £ _ & -'
    char_list = characters.split(' ')
    letters_list = lower_list + upper_list
    object_dictionary = {}
    load()

    # ----------Settings------------------

    root = Tk()
    root.geometry('500x500')
    root.resizable(width=False, height=False)
    root.title('Password Manager')

    # ----------Layout--------------------

    navigation_frame = navigation(root)
    navigation_frame.grid(row=0, column=0, rowspan=2)
    asside_frame = Frame(root, bg='black', width=300, height=250)
    asside_frame.grid_propagate(False)
    asside_frame.grid(row=0, column=1)
    bottom_frame = Frame(root, bg='black', width=300, height=250)
    bottom_frame.grid_propagate(False)
    bottom_frame.grid(row=1, column=1)
    root.mainloop()


main()
