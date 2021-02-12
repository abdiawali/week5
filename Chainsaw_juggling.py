import sqlite3
db='records.sqlite'
#create table function connects with the database if it doesn't exist 
#create table that contains primary key(record_id), constraint name, country and number of catches
def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (record_id INTEGER PRIMARY KEY, name TEXT UNIQUE, country TEXT, num_of_catches INT)')
    conn.close()

"""adds data to the the database
parameters:name, country, number of catches
"""
def add_record(name, country, num_of_catches):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO records (name, country, num_of_catches) VALUES (?, ?, ?)', (name, country, num_of_catches))
        conn.close()
        return True
    except sqlite3.IntegrityError:
        print('sorry the name already exists')
"""searches data 
parameters:name
returns: none if not in the database or data
"""
def search_record(name):
    conn = sqlite3.connect(db)
    search_name=conn.execute('SELECT * FROM records WHERE name LIKE ?', (name, ))
    name_found=search_name.fetchall()
    conn.close()   

    return name_found
    
"""updates data searches if data exist by calling the search function
parameters:name, new number of catches
updates data or returns error message if name not in the database
"""
def update_record(name, new_PR):
    name_found = search_record(name)
    #conn = sqlite3.connect(db)
    #search_name=conn.execute('SELECT * FROM records WHERE name LIKE ?', (name, ))
    #name_found=name_found.fetchall()
    if name_found:
        with sqlite3.connect(db) as conn:
            conn.execute('UPDATE records SET num_of_catches = ? WHERE name = ?', (new_PR, name))
        conn.close()
        stars='*'*19
        print(stars)
        print('succefully updated!')
        print(stars)
    else:
        print('name not found')
        print('--------------')
"""deletes data 
parameters:name
delets data or returns error message if name not in the database
"""
def delete_record(delete_name):
    name_found = search_record(delete_name)
    if name_found: 
        with sqlite3.connect(db) as conn:
            conn.execute('DELETE FROM records WHERE name= ?', (delete_name, ))
        conn.close()
        stars='*'*19
        print(stars)
        print('succefully deleted!')
        print(stars)    
    else:
        print('name not found')
        print('--------------')

def display_data():
    conn = sqlite3.connect(db)
    data = conn.execute('SELECT * FROM records')
    for datum in data:
        print(datum)
    conn.close()
    
"""displays menu options and calls functions
"""
def main():
    create_table()     #create database
    #print the menu options
    print ("""
    1:ADD new record holder
    2:DISPLAY the table
    3:SEARCH for record holder
    4:UPDATE number of catches of record holder
    5:DELETE record holder
    6:quite the program""")

    while True:
        try:
            option=int(input('Please enter your option: '))
            if option==1:
                name=input('Enter name:')
                country=input('coutry representing: ')
                num_of_catches=int(input(('number of chainsaws caught:')))
                is_name_added = add_record(name, country, num_of_catches)
                if is_name_added:
                    stars='*'*(17+len(name))
                    print(stars)
                    print('succefully added '+ name)
                    print(stars)
                else:
                    print('try again')
            elif option==2:
                display_data()
            elif option==3:
                name=input('enter the name of the contestant: ')
                name_found=search_record(name)
                if name_found: 
                    print(name_found)
                else:
                    print('name not found')
                    print('--------------')
            elif option==4:
                name=input('Enter name you want to update: ')
                new_PR=int(input('Enter the new number of catches: '))
                update_record(name, new_PR)
            elif option==5:
                delete_name=input('Enter the name of the contestant you want to delete: ')
                delete_record(delete_name)
            elif option==6:
                stars='*'*17
                print(stars)
                print('thank you and bye')
                print(stars)
                break
        except ValueError:
            print('Invalid input try again')
            print('please enter integer between ')
            continue

main()

