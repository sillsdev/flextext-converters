from conversion_operations import convert
from file_picker_operations import file_picker
from json_operations import load_map_from_json, save_map_to_json
from marker_operations import define_markers, read_markers
from output_operations import output_flextext
from toolbox_operations import toolbox_data_parser, toolbox_file_reader
import tkinter as tk
from tkinter import messagebox

# method to turn a marker filename into a json marker filename
def make_json_filename(marker_filename):
    name_list = marker_filename.split(".")
    name = "".join(name_list[:-1]).split("/")
    return f"json_marker_files/{name[-1]}.json"


def ask_custom_question():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Create a new top-level window for the custom dialog
    dialog = tk.Toplevel(root)
    dialog.title("Custom Question")

    # Add a label with the question
    question_label = tk.Label(dialog, text="Input name of Fieldworks file to create (to fieldworks_files folder):")
    question_label.pack(pady=20)

    # Add an Entry widget for text input
    user_input = tk.Entry(dialog)
    user_input.pack(pady=10)

    # Variable to store the user's response
    response = tk.StringVar()

    def on_custom_yes():
        response.set(user_input.get())
        dialog.destroy()

    def on_custom_no():
        response.set("no")
        dialog.destroy()

    # Create a frame to hold the buttons
    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=5)

    # Add custom buttons with custom text
    custom_yes_button = tk.Button(button_frame, text="Submit",
                                  command=on_custom_yes)
    custom_yes_button.pack(side=tk.LEFT, padx=5)

    custom_no_button = tk.Button(button_frame, text="Cancel",
                                 command=on_custom_no)
    custom_no_button.pack(side=tk.LEFT, padx=5)

    # Wait for the dialog window to close
    dialog.wait_window()

    return response.get()


def ask_question():

    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show a pop-up message with Yes/No choices
    response = messagebox.askquestion(
        "Question",
        "Is there a previously defined JSON marker file you want to use?"
    )

    # Check the user's response
    if response == 'yes':
        print("Select a defined JSON marker file")
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        messagebox.showinfo("Popup Title", "Select a defined JSON marker file")

        json_marker_filename = file_picker()

        while json_marker_filename == "" or not json_marker_filename.endswith(
                ".json"):

            messagebox.showinfo("Popup Title",
                                "Error, invalid file. Select a defined JSON marker file")
            print("Error; invalid file. Select a defined JSON marker file")
            json_marker_filename = file_picker()
    else:
        print("Select a marker file")
        marker_filename = file_picker()

        while marker_filename == "" or not marker_filename.endswith(".typ"):

            messagebox.showinfo("Popup Title",
                                "Error; invalid file. Select a marker file")

            print("Error; invalid file. Select a marker file")
            marker_filename = file_picker()

        # get raw markers
        raw_markers = read_markers(marker_filename)

        # ask user about markers
        defined_markers = define_markers(raw_markers)

        # output json markers
        json_marker_filename = make_json_filename(marker_filename)
        save_map_to_json(defined_markers, json_marker_filename)

    # read in json markers
    json_markers = load_map_from_json(json_marker_filename)

    # toolbox filename

    messagebox.showinfo("Popup Title", "Select a Toolbox file to convert")

    print("Select a Toolbox file to convert")
    toolbox_filename = file_picker()
    while toolbox_filename == "":

        messagebox.showinfo("Popup Title", "Error, invalid file. Select a Toolbox file to convert")
        print("Error; invalid file. Select a Toolbox file to convert")
        toolbox_filename = file_picker()

    rsp = ask_custom_question()
    fieldworks_filename = f"fieldworks_files/{rsp}"

    # fieldworks filename
    # fieldworks_filename = f"fieldworks_files/{input('Input name of FieldWorks file to create (to fieldworks_files folder): ')}"

    # get toolbox data
    toolbox_data = toolbox_data_parser(
        toolbox_file_reader(toolbox_filename))

    # convert data
    converted_xml = convert(toolbox_data, json_markers)

    # output the converted data
    output_flextext(fieldworks_filename, converted_xml)

    print(
        f'Converter successful\nFieldWorks file located at: "{fieldworks_filename}"')
    print("\n<<< Converter Termination >>>")

def main():

    print("<<< Toolbox to FieldWorks File Converter >>>\n")

    ask_question()

    # marker filename
    # answer = input(
    #     "Is there a previously defined JSON marker file you want to use? Y/N: "
    # )
    #
    # if answer.upper() == "Y":
    #     print("Select a defined JSON marker file")
    #     json_marker_filename = file_picker()
    #
    #     while json_marker_filename == "" or not json_marker_filename.endswith(".json"):
    #         print("Error; invalid file. Select a defined JSON marker file")
    #         json_marker_filename = file_picker()
    # else:
    #     print("Select a marker file")
    #     marker_filename = file_picker()
    #
    #     while marker_filename == "" or not marker_filename.endswith(".typ"):
    #         print("Error; invalid file. Select a marker file")
    #         marker_filename = file_picker()
    #
    #     # get raw markers
    #     raw_markers = read_markers(marker_filename)
    #
    #     # ask user about markers
    #     defined_markers = define_markers(raw_markers)
    #
    #     # output json markers
    #     json_marker_filename = make_json_filename(marker_filename)
    #     save_map_to_json(defined_markers, json_marker_filename)
    #
    # # read in json markers
    # json_markers = load_map_from_json(json_marker_filename)
    #
    # # toolbox filename
    # print("Select a Toolbox file to convert")
    # toolbox_filename = file_picker()
    # while toolbox_filename == "" or not toolbox_filename.endswith(".sfm"):
    #     print("Error; invalid file. Select a Toolbox file to convert")
    #     toolbox_filename = file_picker()
    #
    # # fieldworks filename
    # fieldworks_filename = f"fieldworks_files/{input('Input name of FieldWorks file to create (to fieldworks_files folder): ')}"
    #
    # # get toolbox data
    # toolbox_data = toolbox_data_parser(toolbox_file_reader(toolbox_filename))
    #
    # # convert data
    # converted_xml = convert(toolbox_data, json_markers)
    #
    # # output the converted data
    # output_flextext(fieldworks_filename, converted_xml)
    #
    # print(f'Converter successful\nFieldWorks file located at: "{fieldworks_filename}"')
    # print("\n<<< Converter Termination >>>")


if __name__ == "__main__":
    main()
