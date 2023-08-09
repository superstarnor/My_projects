def calc():
    while True:
        n = float(input("Welcome to MyCalc, please choose a number: "))
        ops = {1: "+", 2: "-", 3: "*", 4: "/", 5: "square", 6: "cube", 7: "square root"}
        print("Choose an operation:\n" + "\n".join([f"{key} - {value}" for key, value in ops.items()]))
        op = int(input())
        
        if op in ops:
            if op in [1, 2, 3, 4]:
                user_input = float(input("Choose another number: "))
                result = n + user_input if op == 1 else n - user_input if op == 2 else n * user_input if op == 3 else n / user_input
            elif op in [5, 6, 7]:
                result = n ** (2 if op == 5 else 3 if op == 6 else 0.5)
                
            print(f"Result: {n} {ops[op]} {user_input if op in [1, 2, 3, 4] else ''} = {result}")
            
            if input("Do you want to perform another calculation? (yes/no): ").lower() != "yes":
                print("Goodbye!")
                break
        else:
            print("Invalid choice")

calc()
