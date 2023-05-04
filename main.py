import PySimpleGUI as sg
from zip_extractor import  extract_archive

sg.theme("Black")

file_label = sg.Text("Select Archive:")
file_input = sg.Input()
file_choose_button = sg.FilesBrowse("Choose", key="archive")

folder_label = sg.Text("Select Dest dir:")
folder_input = sg.Input()
folder_choose_button = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="Green")


window = sg.Window("Archive Extractor", layout=[[file_label, file_input, file_choose_button],
                                                [folder_label, folder_input, folder_choose_button],
                                                [extract_button, output_label]])

while True:
    events, values = window.read()
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed")

window.close()
