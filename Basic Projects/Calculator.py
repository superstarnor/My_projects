def calc():
    while True: 
    n, ops, op = int(input("Welcome to MyCalc, please choose a number: ")), {1:"+", 2:"-", 3:"*", 4:"/", 5:"quit"}, int(input("Choose an operation: 1 - add, 2 - subtract, 3 - multiply, 4 - divide: "))
    return n + int(input("Choose another number: ")) if op == 1 else n - int(input("Choose another number: ")) if op == 2 else n * int(input("Choose another number: ")) if op == 3 else n / int(input("Choose another number: ")) if op == 4 and n != 0 else print("Invalid choice") else break if op == 5
print(calc())
