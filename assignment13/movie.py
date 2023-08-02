data = open("assignment13/movie_list.txt", "r")

def add(data_dict, name, IMDB):
    data_dict.update({name : IMDB})
    return data_dict

def read(data):
    dict = {}
    
    for i in data:
        line = i.split("_")
        dict[line[0]] = line[1][0:-1]

    return dict

def show(data_dict):
    print("name", "IMDB")
    for i in data_dict.keys():
        print(f"{i}_{data_dict[i]}")

def show_sort(data_dict):
    print("name", "IMDB")
    for i in sorted(data_dict.keys()):
        print(f"{i}_{data_dict[i]}")

def show_sort_IMDB(data_dict):
    s_dict = sorted(data_dict.values(), reverse=True)  
    for i in range(5):
        for j in data_dict.keys():
            if data_dict[j] == s_dict[i]:
                print(s_dict[i], j)


data_dict = read(data)

while True:
    op = int(input("""1_add
2_show list
3_show sort list
4_show sort IMDB
5_exit and save
"""))
    if op == 1:
        name = input("enter film name: ")
        IMDB = input("enter film IMDB: ")
        data_dict = add(data_dict, name, IMDB)
    
    elif op == 2:
        show(data_dict)

    elif op == 3:
        show_sort(data_dict)

    elif op == 4:
        show_sort_IMDB(data_dict)

    elif op == 5:
        data = open("assignment13/movie_list.txt", "w")
        for i in data_dict.keys():
            data.write(i + "_" + data_dict[i] + "\n")
        data.close()
        break