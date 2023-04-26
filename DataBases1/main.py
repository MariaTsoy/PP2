import psycopg2

cur = None
conn = None

print("Select option: \n1 - View phonebook, 2 - Add, \n3 - Change, 4 - Delete,"
      "\n5 - Import from CSV")
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

    if mode == 5:
        delete_all_script = ''' DELETE FROM phonebook '''
        copy_script = ''' COPY phonebook (name, phone)
                                 FROM 'D:\Phonebook.csv'
                                 DELIMITER ','
                                 CSV HEADER '''
        cur.execute(delete_all_script)
        cur.execute(copy_script)

    if mode == 1:
        print('\n')
        cur.execute(' SELECT * FROM phonebook ')
        for record in cur.fetchall():
            leng = 12 - len(record[0])
            print(record[0], end='')
            for i in range(leng):
                print(' ', end='')
            print(record[1])

    if mode == 2:
        print('Enter the name: ')
        name = input()
        print('Enter the phone: ')
        phone = input()
        insert_script = ' INSERT INTO phonebook (name, phone) VALUES (%s, %s) '
        insert_value = (name, phone)
        cur.execute(insert_script, insert_value)

    if mode == 3:
        print('Select option: 1 - Change name via number, 2 - Change number via name')
        option = int(input())
        if option == 1:
            print('Enter the phone: ')
            phone = input()
            print('Enter new name: ')
            name = input()
            change_script1 = ''' UPDATE phonebook 
                                    SET name = %s 
                                    WHERE phone = %s'''
            change_cond1 = (name, phone)
            cur.execute(change_script1, change_cond1)
        else:
            print('Enter the name: ')
            name = input()
            print('Enter new phone: ')
            phone = input()
            change_script2 = ''' UPDATE phonebook 
                                    SET phone = %s 
                                    WHERE name = %s'''
            change_cond2 = (phone, name)
            cur.execute(change_script2, change_cond2)

    if mode == 4:
        print('Enter the name: ')
        name = input()
        delete_script = ''' DELETE FROM phonebook
                                WHERE name = %s '''
        delete_cond = (name,)
        cur.execute(delete_script, delete_cond)

    if mode != 1:
        print('\nNew Table:')
        cur.execute(' SELECT * FROM phonebook ')
        for record in cur.fetchall():
            leng = 12 - len(record[0])
            print(record[0], end='')
            for i in range(leng):
                print(' ', end='')
            print(record[1])

    conn.commit()

except:
    print("Error")

finally:
    if conn is not None:
        cur.close()
    if cur is not None:
        conn.close()
