import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
from abc import ABC, abstractmethod


filename = 'input.txt'


class IConverter(ABC):
    @abstractmethod
    def convert(self, input_file):
        pass


class Text2csv(IConverter):
    def convert(self, input_file):
        output_file = "output.csv"
        num_columns = 5
        input_file = open(input_file, 'r', encoding="utf-8")
        new_text = input_file.readlines()
        words = []
        line_break = 0
        for x in range(0, len(new_text)):
            for word in new_text[x].split():
                words.append(word + ',')

        f = open(output_file, 'w')
        for x in range(0, len(words)):
            if (line_break == num_columns):
                f.write('\n')
                f.write(words[x])
                line_break = 1
            else:
                f.write(words[x])
                line_break += 1
        f.close()


class Text2json(IConverter):
    def convert(self, input_file):
        dict1 = {}
        with open(input_file) as fh:
            for line in fh:
                command, description = line.strip().split(None, 1)
                dict1[command] = description.strip()

        out_file = open("output.json", "w")
        json.dump(dict1, out_file, indent=4, sort_keys=False)
        out_file.close()


class Text2xml(IConverter):
    def convert(self, input_file):
        s = ""
        with open("input1.json") as f:
            s += f.readline()
        data = readfromstring(s)
        with open("output.xml", 'w') as f:
            f.write(json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml())


class Client:
    def __init__(self, _converter: IConverter):
        self._converter = _converter

    def convert(self, input_file):
        self._converter.convert(input_file)


def select_file():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )


if __name__ == '__main__':
    app = tk.Tk()
    app.title('Strategy Pattern')
    app.geometry('700x350')
    open_button = ttk.Button(
        app,
        text='Open a File',
        command=select_file
    )

    open_button.pack(expand=True)

    lineButton = ttk.Button(app, text='text2csv', width=12, command=Client(Text2csv()).convert(filename))
    lineButton.pack(expand=True)
    lineButton = ttk.Button(app, text='text2json', width=12, command=Client(Text2json()).convert(filename))
    lineButton.pack(expand=True)
    lineButton = ttk.Button(app, text='text2xml', width=12, command=Client(Text2xml()).convert(filename))
    lineButton.pack(expand=True)

    app.mainloop()


