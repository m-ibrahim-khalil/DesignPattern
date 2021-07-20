import json
import codecs
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson


class TextConverter():
    def textConvert(self,_converter, file):
        _converter.convert(file)


class Iconverter():
    def convert(self, file):
        pass


class Text2csv(Iconverter):
    def convert(self, file):
        output_file = "output.csv"
        num_columns = 5
        file = open(file, 'r', encoding="utf-8")
        new_text = file.readlines()
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



class Text2json(Iconverter):
    def convert(self, file):
        dict1 = {}
        with open(file) as fh:
            for line in fh:
                command, description = line.strip().split(None, 1)
                dict1[command] = description.strip()

        out_file = open("output.json", "w")
        json.dump(dict1, out_file, indent=4, sort_keys=False)
        out_file.close()



class Text2xml(Iconverter):
    def convert(self, file):
        s = ""
        with open("input1.json") as f:
            s+=f.readline()
        data = readfromstring(
            s
        )
        with open("output.xml", 'w') as f:
            f.write(json2xml.Json2xml(data, wrapper="all", pretty=True).to_xml())


class Client:
    def text2csv(self):
        csv_converter = Text2csv()
        textConverter = TextConverter()
        textConverter.textConvert(csv_converter, self.fileName)

    def text2json(self):
        json_converter = Text2json()
        textConverter = TextConverter()
        textConverter.textConvert(json_converter, self.fileName)

    def text2xml(self):
        csv_converter = Text2xml()
        textConverter = TextConverter()
        textConverter.textConvert(csv_converter, self.fileName)

    def setFile(self, fileName):
        self.fileName = fileName


if __name__ == '__main__':

    client = Client()
    app = Tk()
    filename = askopenfilename()
    client.setFile(filename)
    app.title('Composit DP')
    app.geometry('700x350')
    lineButton = Button(app, text='text2csv', width=12, command=client.text2csv())
    lineButton.grid(row=3, column=0, pady=20)
    lineButton = Button(app, text='text2json', width=12, command=client.text2json())
    lineButton.grid(row=4, column=0, pady=20)
    lineButton = Button(app, text='text2xml', width=12, command=client.text2xml())
    lineButton.grid(row=5, column=0, pady=20)

    app.mainloop()


