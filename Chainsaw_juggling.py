import sqlite3
db='records.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (record_id INTEGER PRIMARY KEY, name TEXT UNIQUE, country TEXT, num_of_catches INT)')
    conn.close()


def add_record(name, country, num_of_catches):
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO records (name, country, num_of_catches) VALUES (?, ?, ?)', (name, country, num_of_catches))
    conn.close()

def search_record(name):
    conn = sqlite3.connect(db)
    search_name=conn.execute('SELECT * FROM records WHERE name LIKE ?', (name, ))
    name_found=search_name.fetchall()
    conn.close()   

    return name_found
    

def update_record(name, new_PR):
    conn = sqlite3.connect(db)
    search_name=conn.execute('SELECT * FROM records WHERE name LIKE ?', (name, ))
    name_found=search_name.fetchall()
    if name_found: 
         with sqlite3.connect(db) as conn:
            conn.execute('UPDATE records SET name = ? WHERE num_of_catches = ?', (name, new_PR))
    else:
        print('name not found')
    conn.close()

def delete_record(delete_name):
    name_found=search_record(delete_name)
    if name_found: 
        with sqlite3.connect(db) as conn:
            conn.execute('DELETE FROM records WHERE name= ?', (delete_name, ))
    else:
        print('name not found')
    conn.close()

def menu():
    print ("""
    1:ADD new record holder
    2:SEARCH for record holder
    3:UPDATE number of catches of record holder
    4:DELETE record holder
    5:quite the program""")
    while True:
        option=int(input('Please enter your option:'))
        try:
            if option==1:
                name=input('Enter name:')
                country=input('coutry representing: ')
                num_of_catches=int(input(('number of chainsaws caught:')))
                add_record(name, country, num_of_catches)
                print('succefull added')
            elif option==2:
                name=input('enter the name of the contestant: ')
                name_found=search_record(name)
                if name_found: 
                    print(name_found)
                else:
                    print('name not found')
            elif option==3:
                name=input('enter name you want to update:')
                new_PR=int(input('enter the new number of catches'))
                update_record(name, new_PR)
            elif option==4:
                delete_name=input('Enter the name of the contestant you want to delete: ')
                delete_record(delete_name)
            elif option==5:
                print('thank you and bye')
                break
        except ValueError:
            print('Invalid input try again')
            continue



def main():
    create_table()
    menu()        
main()

