'''
Run file:
ls
python3 names.py > index.html - writing code from Python to html
python3 names.py > index.html & firefox index.html - run app
cat index.html - display in the console the contents of the index.html file
@AdrianSzklarski, 09.2023
'''

import sys

class Txt:

    def __init__(self):
        self.help_doc = "It's very important to give examples of program usage! " \
                   "Displays on 'stdout' the line where it found the searched text. " \
                   "Usage: python3 names_ver2.py Names.txt Wera"

        self.link = r'/home/adrian/Pulpit/GitHub/My_Programmes/List_of_name/Names.txt'

    def get_txt(self):

        # I give a list of arguments (what I am looking for), such as the name of the directory I am looking for
        print('Name of file: ', sys.argv, '\n'
                                          'Len of list: ', len(sys.argv), '\n')
        if len(sys.argv) != 3:
            print(self.help_doc)
            sys.exit(1)

        path = sys.argv[1]
        search = sys.argv[2]

        f = open(self.link, 'r', encoding='UTF-8')
        for lines in f:
            lines = lines.strip()
            self.name = lines.split(',')[0]
        f.close()

        print('Path to file: ', path, '\n'
                                      'Search: ', search)
        return self.name

    def __str__(self):
        return f'{self.get_txt()}'

if __name__=='__main__':
    file = Txt()
    print(file)
