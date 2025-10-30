def input_number(print):
    while True:
        try:
            num = int(input(f"enter your {print} number"))
        except:
            print("error peek only number")
            continue

        if num >= 1 and num <= 3:
            return num

def check_if_new(table,row,column):
    if table[row][column] == "$":
        return True

def round_play(table):
    while True:
        row = input_number("row")
        column = input_number("column")

        if check_if_new(table,row,column):
            break





















