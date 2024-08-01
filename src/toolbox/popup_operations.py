import pycountry
import tkinter as tk
from tkinter import ttk


def closed_resp(question, button_list, key_list):
    root = root_init(question)
    response = tk.StringVar()
    message = tk.Message(root, text="Enter the corresponding number on "
                                    "the button or click it", width=400)
    message.pack(pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    def on_submit(index, btn):
        response.set(index)
        btn.event_generate("<Button-1>")
        root.after(100, root.destroy)

    for idx in range(len(button_list)):
        button = ttk.Button(button_frame, text=button_list[idx],
                            underline=button_list[idx].find(key_list[idx]))
        button.config(command=lambda i=idx, b=button: on_submit(i+1, b))
        button.grid(row=idx//5, column=idx % 5, padx=5, pady=5)
        root.bind(f'<KeyPress-{key_list[idx].lower()}>',
                  lambda event, i=idx, b=button: on_submit(i+1, b))

    root_geometry(root)
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
    return response.get()


def open_resp(question):
    root = root_init(question)
    response = tk.StringVar()

    # Make user input
    user_input = tk.Entry(root, width=27)
    user_input.pack(pady=10, padx=45)
    user_input.focus_set()

    def on_submit():
        button.event_generate("<Button-1>")
        response.set(user_input.get())
        if user_input.get() == '':
            response.set("default")
        root.after(100, root.destroy)

    # Make submit button
    button = ttk.Button(root, text="Submit", command=on_submit)
    button.pack(pady=10)
    root.bind('<Return>', lambda event: on_submit())

    root_geometry(root)
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
    return response.get()


def dropdown_resp(question, drop_menu):
    root = root_init(question)

    # Make submit button
    button = tk.Button(root, text="Submit", state=tk.DISABLED)
    button.pack(side=tk.BOTTOM, padx=10, pady=10)

    # Create Dropdown
    response = create_dropdown(root, drop_menu, button)

    # Run the application
    root_geometry(root)
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
    return response.get()


def create_dropdown(root, drop_menu, button):
    def on_input_change(*args):
        input_text = response.get()
        if response.get() in drop_menu:
            button['state'] = tk.NORMAL
        else:
            button['state'] = tk.DISABLED
        # Filter the dropdown menu based on what has been typed
        dropdown['values'] = [option for option in drop_menu if any(
            word.lower().startswith(input_text.lower()) for word in
            option.split()) or option.lower().startswith(input_text.lower())]
        dropdown.event_generate('<Down>')
        dropdown.focus_set()

    def on_submit(*args):
        if button['state'] == tk.NORMAL:
            button.config(fg="blue")
            root.after(100, root.destroy())
        else:
            dropdown.event_generate('<Escape>')
            dropdown.event_generate('<Down>')
            dropdown.event_generate('<Return>')

    button.config(command=on_submit)
    response = tk.StringVar()
    dropdown = ttk.Combobox(root, textvariable=response, values=drop_menu)
    dropdown.pack(padx=10, pady=10)
    dropdown.focus_set()
    response.trace("w", on_input_change)
    root.bind('<Return>', on_submit)
    return response


def first_screen():
    root = root_init("Select appropriate files")


def table(question, mkr_map, headings):
    global edit_window
    edit_window = None

    def edit_cell(event):
        def save_changes(*args):
            # Update the Treeview item with the new values
            values[column_idx] = user_input.get()
            tree.item(selected_item, values=values)
            mkr_map[values[0]][markers[column_idx - 1]] = values[column_idx]
            # print(f"Marker: {values[0]}\nValues: {mkr_map[values[0]]}")
            edit_window.destroy()

        column_id = tree.identify_column(event.x)
        if column_id == "#1" or column_id == "#2":
            return
        column_idx = int(column_id[1:]) - 1
        selected_item = tree.focus()
        values = list(tree.item(selected_item, 'values'))
        global edit_window
        if edit_window is not None and edit_window.winfo_exists():
            edit_window.destroy()
        edit_window = tk.Toplevel(window)
        text = headings[column_idx]
        edit_window.title(f"Edit {text} for marker {values[0]}")
        label = tk.Label(edit_window, text=text)
        label.grid(row=0, column=0)

        save_button = ttk.Button(edit_window, text="Save", command=save_changes)
        save_button.grid(row=3, column=0, columnspan=2, pady=10)
        user_input = ttk.Entry(edit_window)
        user_input.grid(row=0, column=1, padx=5, pady=5)
        user_input.insert(0, values[column_idx])
        user_input.focus_set()
        edit_window.bind('<Return>', lambda evnt: save_changes())

    def on_submit():
        button.event_generate("<Button-1>")
        window.after(100, window.destroy)

    markers = ["Count", "\\nam", "\\lng"]
    window = root_init(question)
    tree = ttk.Treeview(window, columns=headings, show="headings")
    for heading in headings:
        tree.heading(heading, text=heading, anchor=tk.W)

    for idx, key in enumerate(mkr_map.keys()):
        vals = ['' for _ in range(len(headings))]
        vals[0] = key
        for mkr_idx in range(len(markers)):
            if markers[mkr_idx] in mkr_map[key]:
                vals[mkr_idx + 1] = mkr_map[key][markers[mkr_idx]]
            else:
                vals[mkr_idx + 1] = ""
        if idx % 2 == 0:
            tree.insert("", "end", tags='color', values=vals)
        else:
            tree.insert("", "end", values=vals)

    tree.bind("<Double-1>", edit_cell)
    tree.tag_configure('color', background='#282828')

    # Add a submit button
    button_frame = ttk.Frame(window)
    button_frame.pack(fill='x', side='bottom')  # Pack it at the bottom
    button = ttk.Button(button_frame, text="Submit", command=on_submit)
    button.pack(pady=10)
    window.bind('<Return>', lambda evt: on_submit())

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.pack(expand=True, fill=tk.BOTH)

    root_geometry(window)
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()
    return mkr_map


def on_close():
    quit()


def root_init(question):
    root = tk.Tk()
    root.title("<<< Toolbox to FieldWorks File Converter >>>")

    # Question or command
    question_label = tk.Label(root, text=question)
    question_label.pack(padx=10, pady=10)

    return root


def window_init(base_root, title, label):
    new_window = tk.Toplevel(base_root)
    new_window.title(title)

    question_label = tk.Label(new_window, text=label)
    question_label.pack(pady=10)

    return new_window


def root_geometry(root):
    # Set the root towards the middle of the screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x_offset = (root.winfo_screenwidth() // 2) - (width // 2)
    y_offset = (root.winfo_screenheight() // 3) - (height // 2)
    root.geometry(f"{width + 20}x{height + 20}+{x_offset}+{y_offset}")


def language_list():
    lang_list = ["English: eng"]
    for lang in pycountry.languages:
        # if hasattr(lang, 'alpha_2'):
        #     lang_list.append(lang.alpha_2 + " ( " + lang.name + ")")
        if hasattr(lang, 'alpha_3') and lang.alpha_3 != "eng":
            lang_list.append(lang.name + ": " + lang.alpha_3)
        # if hasattr(lang, 'terminology'):
        #     lang_list.append(lang.terminology + " ( " + lang.name + ")")
        # if hasattr(lang, 'bibliographic'):
        #     lang_list.append(lang.bibliographic + " ( " + lang.name + ")")
    return lang_list


def name_list():
    return ["Word", "Morphemes", "Lex. Entries", "Lex. Gloss",
            "Lex. Gram. Info", "Word Gloss", "Word Cat.", "Free Translation",
            "Literal Translation", "Note"]
