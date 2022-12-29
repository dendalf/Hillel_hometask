def calculate_data():
    avg_height = 0
    avg_weight = 0
    with open("hw.csv", "r") as f:
        f.readline()  # пропускаем первую строку
        for line in f:
            if line.split(", ")[0] == 1:
                avg_height = float(line.split(", ")[1])
                avg_weight = float(line.split(", ")[2])
            if line != '\n':  # пропускаем пустые строки в файле
                avg_height = (avg_height + float(line.split(", ")[1])) / 2
                avg_weight = (avg_weight + float(line.split(", ")[2])) / 2
        avg_height *= 2.54
        avg_weight /= 2.205
    return f'средний рост = {round(avg_height, 2)} средний вес = {round(avg_weight, 2)}'
