'''
Run file:
python3 names.py > index.html & firefox index.html
'''

link = r'/home/adrian/Pulpit/GitHub/My Programmes/List_of_name/Names.txt'

#  ver.1
f = open(link, 'r', encoding='UTF-8')
for lines in f:
    lines = lines.strip()
    name = lines.split(',')[0]
    print(f'''
    <html>
        <body>
            <h1>The following people are invited to 12:00 pm: {name}</h1>
            <p>Best Regards, Your Boss</p>
        </body>
    </html>
    ''')
f.close()

#  ver.2
with open(link, 'r', encoding='UTF-8') as f:
    for lines in f:
        lines = lines.strip()
        name = lines.split(',')[0]
        print(f'''
        <html>
            <body>
                <h1>The following people are invited to 12:00 pm: {name}</h1>
                <p>Best Regards, Your Boss</p>
            </body>
        </html>
        ''')
