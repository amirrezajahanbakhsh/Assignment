import sqlite3

data = sqlite3.connect("assignment17/cars_database.db")
c = data.cursor()
data_csv = open("assignment16/cars_dataset.csv", "r")

def csv_to_database(c, data_csv):
    try:
        c.execute("""CREATE TABLE cars (
            Car TEXT,
            MPG TEXT,
            Cylinders TEXT,
            Displacement TEXT,
            Horsepower TEXT,
            Weight TEXT,
            Acceleration TEXT,
            Model TEXT,
            Origin TEXT
        )
    """)
    except:
        pass

    datas = []
    a = 1
    for i in data_csv.readlines():
        if a == 1:
            a = 2
            continue
        i = i.rstrip().split(",")
        datas.append(tuple(i))

    for i in datas:
        c.execute(f"INSERT INTO cars VALUES {i}")

csv_to_database(c, data_csv)
data.commit()

def show_japanese_car(c):
    cars = []
    for i in c.execute("SELECT * FROM cars WHERE Origin == 'Japan'"):
        cars.append(i[0])
    return cars

def show_long_name(c): 
    l = ""
    for i in c.execute("SELECT Car FROM cars"):
        i = i[0]
        if len(i) > len(l):
            l = i
    return l

def show_shortest_name(c):
    l = show_long_name
    for i in c.execute("SELECT Car FROM cars"):
        i = i[0]
        if len(i) < len(l):
            l = i
    return l

def avg_sylinders(c):
    c = []
    for i in c.execute("SELECT Cylinders FROM cars"):
        i = i[0]
        c.append(int(i))

    return sum(c) / len(c)     

def avg_horsepower(c):
    p = []
    for i in c.execute("SELECT Horsepower FROM cars"):
        i = i[0]
        p.append(float(i))

    return sum(p) / len(p)

def light_cars(c):
    l = []
    f = 0
    for i in c.execute("SELECT * FROM cars ORDER BY Weight"):
        i = i[0]
        l.append(i)
        f += 1
        if f == 50:
            return l 
        
while True:
    op = int(input("""1 = show Japanese cars                   
2 = show longest name
3 = show shortest name
4 = show average of Cylinders
5 = show average of Horsepower
6 = show light cars name
7 = exit"""))

    if op == 1:
        print(show_japanese_car(c))

    elif op == 2:
        print(show_long_name(c))

    elif op == 3:
        print(show_shortest_name(c))

    elif op == 4:
        print(avg_sylinders(c))

    elif op == 5:
        print(avg_horsepower(c))

    elif op == 6:
        print(light_cars(c))

    elif op == 7:
        data.close()
        break