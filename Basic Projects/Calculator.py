import sympy as sp

def calc():
    while True:
        n = float(input("Welcome to MyCalc, please choose a number: "))
        ops = {
            1: "+", 2: "-", 3: "*", 4: "/",
            5: "square", 6: "cube", 7: "square root",
            8: "derivative", 9: "integral",
            10: "sin", 11: "cos", 12: "tan",
            13: "arcsin", 14: "arccos", 15: "arctan",
            16: "log", 17: "exp",
            18: "factorial", 19: "binomial",
            20: "mean", 21: "median", 22: "mode",
            23: "standard deviation", 24: "variance"
        }
        print("Choose an operation:\n" + "\n".join([f"{key} - {value}" for key, value in ops.items()]))
        op = int(input())
        
        if op in ops:
            if op in [1, 2, 3, 4]:
                user_input = float(input("Choose another number: "))
                result = (
                    n + user_input if op == 1 else
                    n - user_input if op == 2 else
                    n * user_input if op == 3 else
                    n / user_input
                )
            elif op in [5, 6, 7]:
                result = n ** (2 if op == 5 else 3 if op == 6 else 0.5)
            elif op == 8:
                x = sp.symbols('x')
                expr = n * x
                result = sp.diff(expr, x)
            elif op == 9:
                x = sp.symbols('x')
                expr = n * x
                result = sp.integrate(expr, x)
            elif op in [10, 11, 12, 13, 14, 15]:
                angle = n if op in [10, 11, 12] else sp.rad(n)
                result = (
                    sp.sin(angle) if op == 10 else
                    sp.cos(angle) if op == 11 else
                    sp.tan(angle) if op == 12 else
                    sp.asin(angle) if op == 13 else
                    sp.acos(angle) if op == 14 else
                    sp.atan(angle)
                )
            elif op in [16, 17]:
                result = sp.log(n) if op == 16 else sp.exp(n)
            elif op == 18:
                result = sp.factorial(n)
            elif op == 19:
                k = int(input("Enter the value of 'k' for the binomial coefficient: "))
                result = sp.binomial(n, k)
            elif op in [20, 21, 22]:
                data = input("Enter a list of numbers separated by spaces: ").split()
                data = [float(item) for item in data]
                result = (
                    sp.mean(data) if op == 20 else
                    sp.median(data) if op == 21 else
                    sp.mode(data) if op == 22 else
                    0
                )
            elif op in [23, 24]:
                data = input("Enter a list of numbers separated by spaces: ").split()
                data = [float(item) for item in data]
                mean = sp.mean(data)
                result = (
                    sp.sqrt(sp.mean([(x - mean)**2 for x in data])) if op == 23 else
                    sp.mean([(x - mean)**2 for x in data]) if op == 24 else
                    0
                )
                
            print(f"Result: {n} {ops[op]} {user_input if op in [1, 2, 3, 4] else ''} = {result}")
            
            if input("Do you want to perform another calculation? (yes/no): ").lower() != "yes":
                print("Goodbye!")
                break
        else:
            print("Invalid choice")

calc()
