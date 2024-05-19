import sqlite3

con = sqlite3.connect('dodoo.db')
cursor = con.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT,
    first_name TEXT,
    middle_name TEXT,
    position TEXT,
    employment_date TEXT,
    address TEXT,
    phone_number TEXT)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Ingredient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    availability TEXT)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Pizza(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    ingredient_id INTEGER REFERENCES Ingredient(id),
    price INTEGER)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Order_table(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_id INTEGER REFERENCES Customer(id),
    Pizza_id INTEGER REFERENCES Pizza(id),
    quantity INTEGER,
    total_price INTEGER,
    datetime TEXT)''')

con.commit()

print('Выберите таблицу для добавления данных:')
print('1 - Сотрудник; 2 - Ингредиент; 3 - Пицца; 4 - Клиент; 5 - Заказ')
table_choice = int(input())

if table_choice == 1:
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    position = input('Введите должность: ')
    employment_date = input('Введите дату приема на работу: ')
    address = input('Введите адрес: ')
    phone_number = input('Введите номер телефона: ')
    cursor.execute('''INSERT INTO Employee(last_name, first_name, middle_name, position, employment_date, address, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?);''',
                   (last_name, first_name, middle_name, position, employment_date, address, phone_number))
elif table_choice == 2:
    name = input('Введите название ингредиента: ')
    description = input('Введите описание: ')
    availability = input('Доступность: ')
    cursor.execute('''INSERT INTO Ingredient(name, description, availability) VALUES (?, ?, ?);''',
                   (name, description, availability))
elif table_choice == 3:
    name = input('Введите название пиццы: ')
    description = input('Введите описание: ')
    ingredient_id = input('Введите ID ингредиента: ')
    price = input('Введите цену: ')
    cursor.execute('''INSERT INTO Pizza(name, description, ingredient_id, price) VALUES (?, ?, ?, ?);''',
                   (name, description, ingredient_id, price))
elif table_choice == 4:
    name = input('Введите имя клиента: ')
    cursor.execute('''INSERT INTO Customer(name) VALUES (?);''', (name,))
elif table_choice == 5:
    customer_id = input('Введите ID клиента: ')
    pizza_id = input('Введите ID пиццы: ')
    quantity = input('Введите количество: ')

    total_price = 0  # инициализация переменной total_price для заказа
    customer_id = input('Введите ID клиента: ')
    pizza_id = input('Введите ID пиццы: ')
    quantity = input('Введите количество: ')
    cursor.execute('''SELECT price FROM Pizza WHERE id = ?;''', (pizza_id,))
    price_data = cursor.fetchone()
    if price_data:
        price = float(price_data[0])
        total_price = int(price) * int(quantity)
        datetime = input('Введите дату и время: ')
        cursor.execute(
            '''INSERT INTO Order_table(Customer_id, Pizza_id, quantity, total_price, datetime) VALUES (?, ?, ?, ?, ?);''',
            (customer_id, pizza_id, quantity, total_price, datetime))
    else:
        print('Пицца с указанным ID не найдена.')
    print('Цена пиццы:', total_price)  # вывод цены пиццы при добавлении заказа
else:
    print('Неверный выбор.')
con.commit()
con.close()
