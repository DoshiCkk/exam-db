import psycopg2

def connect():
    conn = psycopg2.connect(database = "exam",
                            user = "postgres",
                            password = "postgres",
                            host = "localhost",
                            port = 5432)
    return conn
connection = connect()
cursor = connection.cursor()

def creation_user():
    print("But we friends thoooo");
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    query = f"insert into users(name, age) values('{name}', {age})"
    cursor.execute(query)
    connection.commit()

def creation_mag():
    titlee = input("Enter yours Titles name: ")
    descriptione = input("Write about your magazine: ")
    q_m = f"insert into magazines(title, description) values('{titlee}', '{descriptione}')"
    cursor.execute(q_m)
    connection.commit()

def update_user():
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    q = f"update users set name = '{name}', age = {age}"
    cursor.execute(q)
    connection.commit()

def update_mag():
    titlee = input("Enter New Title: ")
    descriptione = int(input("Enter New Description: "))
    q = f"update set magazines title = '{titlee}', description = '{descriptione}'"
    cursor.execute(q)
    connection.commit()

