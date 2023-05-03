import psycopg2
import time
import re

cur = None
conn = None
mode = 10000


def insert_many():
    names = []
    phones = []
    bad_names = []
    bad_phones = []
    print('Enter number of phones you want to add: ')
    num = int(input())

    for y in range(num):
        print('Enter name ', y + 1, ':', sep='')
        name0 = input()
        print('Enter phone: ')
        phonenum = input()
        good_phone = re.search('^\+[0-9]{11}$', phonenum)
        if good_phone is not None:
            names.append(name0)
            phones.append(phonenum)
        else:
            bad_names.append(name0)
            bad_phones.append(phonenum)

    return [bad_names, bad_phones, names, phones]


def not_bad_phone(phonenum):
    good_phone = re.search('^\+[0-9]{11}$', phonenum)
    if good_phone is not None:
        return True
    else:
        return False


def fetch_all():
    for record in cur.fetchall():
        print(record[0], end='')
        for i in range(12 - len(record[0])):
            print(' ', end='')
        print(record[1])


while mode != 0:
    print('Select option: \n1 - View phonebook, 2 - Add, 3 - Change, \n4 - Delete, '
          '5 - Import from CSV, 6 - Search, \n7 - View several users, 0 - Exit')
    mode = int(input())

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="Phonebook",
            user="postgres",
            password="pikachu26866")
        cur = conn.cursor()

        create_script = ''' CREATE TABLE IF NOT EXISTS phonebook (
                            name varchar,
                            phone varchar) '''
        cur.execute(create_script)

        if mode == 1:
            cur.execute(' SELECT * FROM phonebook ORDER BY name ')
            fetch_all()
            print()
            time.sleep(2)

        elif mode == 2:
            updated_users = []
            inserted_users = insert_many()
            for user in range(len(inserted_users[2])):
                cur.execute('SELECT * FROM phonebook WHERE name = %s', (inserted_users[2][user], ))
                search = cur.fetchone()
                if search is not None:
                    change_script = ''' UPDATE phonebook 
                                        SET phone = %s 
                                        WHERE name = %s '''
                    change_cond = (inserted_users[3][user], inserted_users[2][user])
                    cur.execute(change_script, change_cond)
                    updated_users.append([inserted_users[2][user], inserted_users[3][user]])
                else:
                    insert_script = 'INSERT INTO phonebook (name, phone) VALUES (%s, %s)'
                    insert_value = (inserted_users[2][user], inserted_users[3][user])
                    cur.execute(insert_script, insert_value)

            if len(inserted_users[0]) > 0:
                print("Next users weren't added: ")
                for i in range(len(inserted_users[0])):
                    print(inserted_users[0][i], end='')
                    for u in range(12 - len(inserted_users[0][i])):
                        print(" ", end="")
                    print(inserted_users[1][i])
            time.sleep(1.5)

            if len(updated_users) > 0:
                print('Next users were updated: ')
                for i in range(len(updated_users)):
                    print(updated_users[i - 1][0], end='')
                    for u in range(12 - len(updated_users[i - 1][0])):
                        print(' ', end='')
                    print(updated_users[i - 1][1])
            time.sleep(1.5)

        elif mode == 3:
            print('Select option: 1 - Change name via number, 2 - Change number via name')
            option = int(input())
            if option == 1:
                print('Enter the phone: ')
                phone = input()
                print('Enter new name: ')
                name = input()
                change_script1 = '''UPDATE phonebook 
                                    SET name = %s 
                                    WHERE phone = %s'''
                change_cond1 = (name, phone)
                cur.execute(change_script1, change_cond1)
                print('Name updated.')
            else:
                print('Enter the name: ')
                name = input()
                print('Enter new phone: ')
                phone = input()
                if not_bad_phone(phone):
                    change_script2 = '''UPDATE phonebook 
                                        SET phone = %s 
                                        WHERE name = %s'''
                    change_cond2 = (phone, name)
                    cur.execute(change_script2, change_cond2)
                    print('Phone updated.')
                else:
                    print("That's a bad phone. Try again later.")
            time.sleep(1.5)

        elif mode == 4:
            print('Select option: \n1 - Delete via name, 2 - Delete via phone')
            delete_mode = int(input())
            if delete_mode == 1:
                print('Enter the name: ')
                name = input()
                delete_script = ''' DELETE FROM phonebook
                                    WHERE name = %s '''
                delete_cond = (name, )
                cur.execute(delete_script, delete_cond)
                print('User deleted')
            elif delete_mode == 2:
                print('Enter the phone: ')
                phone = input()
                delete_script = ''' DELETE FROM phonebook
                                    WHERE name = %s '''
                delete_cond = (phone, )
                cur.execute(delete_script, delete_cond)
                print('User deleted')
            else:
                print('Error. Try again.')
            time.sleep(1.5)

        elif mode == 5:
            delete_all_script = ''' DELETE FROM phonebook '''
            copy_script = ''' COPY phonebook (name, phone)
                                     FROM 'D:\Phonebook.csv'
                                     DELIMITER ','
                                     CSV HEADER '''
            cur.execute(delete_all_script)
            cur.execute(copy_script)

            print('\nTable:')
            cur.execute(' SELECT * FROM phonebook ORDER BY name ')
            fetch_all()
            print()
            time.sleep(2)

        elif mode == 6:
            print('Select option:\n1 - Search in names, 2 - Search in phones')
            search_option = int(input())
            if search_option == 1:
                print('Enter name/ part of name: ')
                search_script = 'SELECT * FROM phonebook WHERE name ~ %s'
                search_name = input()
                search_cond = ('.*' + search_name + '.*', )
                print("What was found in the table with '", search_name, "':", sep='')
                cur.execute(search_script, search_cond)
                fetch_all()
            elif search_option == 2:
                print('Enter the phone: ')
                search_script = 'SELECT * FROM phonebook WHERE phone = %s'
                search_phone = input()
                search_cond = (search_phone, )
                print("What was found in the table with '", search_phone, "':", sep='')
                cur.execute(search_script, search_cond)
                fetch_all()
            else:
                print('Error. Try again.')
                time.sleep(1.5)
                continue
            print('\n')
            time.sleep(2)

        elif mode == 7:
            print('Enter starting index: ')
            ind1 = int(input())
            print('Enter last index: ')
            ind2 = int(input())
            order_script = '''SELECT * FROM phonebook
                                ORDER BY name
                                OFFSET %s LIMIT %s'''
            order_cond = (ind1 - 1, ind2 - ind1 + 1)
            cur.execute(order_script, order_cond)
            for i in range(ind2 - ind1 + 1):
                user = cur.fetchone()
                print(user[0], end='')
                for u in range(12 - len(user[0])):
                    print(' ', end='')
                print(user[1])
            print('\n')
            time.sleep(2)

        if mode == 4 or mode == 2 or mode == 3:
            update_file_script = "COPY phonebook TO 'D:\Phonebook.csv' WITH DELIMITER ',' CSV HEADER"
            cur.execute(update_file_script)
            print('\nNew Table:')
            cur.execute('SELECT * FROM phonebook ORDER BY name')
            fetch_all()
            print()
            time.sleep(2)

        conn.commit()

    except:
        print("Some error occurred.")
        time.sleep(1.5)

    finally:
        if conn is not None:
            cur.close()
        if cur is not None:
            conn.close()
