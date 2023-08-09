from flask import Flask, request, jsonify
import sympy as sp

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    n = data.get('number')
    op = data.get('operation')

    if n is None or op is None:
        return jsonify({'error': 'Missing number or operation'}), 400

    ops = {
        1: "+", 2: "-", 3: "*", 4: "/",
        5: "square", 6: "cube", 7: "square root",
        8: "derivative", 9: "integral",
        10: "sin", 11: "cos", 12: "tan",
        13: "arcsin", 14: "arccos", 15: "arctan",
        16: "log", 17: "exp",
        18: "factorial", 19: "binomial",
        20: "mean", 21: "median", 22: "mode",
        23: "standard deviation", 24: "variance",
        25: "lcm", 26: "gcd", 27: "abs",
        28: "floor", 29: "ceil",
        30: "matrix determinant", 31: "matrix inverse",
        32: "matrix transpose", 33: "vector dot product",
        34: "vector cross product", 35: "matrix eigenvalues",
        36: "matrix rank", 37: "matrix trace",
        38: "hypotenuse", 39: "power"
    }

    if op in ops:
        if op in [1, 2, 3, 4]:
            user_input = data.get('user_input')
            if user_input is None:
                return jsonify({'error': 'Missing user_input'}), 400
            result = (
                n + user_input if op == 1 else
                n - user_input if op == 2 else
                n * user_input if op == 3 else
                n / user_input
            )
        elif op in [5, 6, 7]:
            result = n ** (2 if op == 5 else 3 if op == 6 else 0.5)
        elif op in [8, 9]:
            x = sp.symbols('x')
            expr = n * x
            result = sp.diff(expr, x) if op == 8 else sp.integrate(expr, x)
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
            k = data.get('k')
            if k is None:
                return jsonify({'error': 'Missing k for binomial coefficient'}), 400
            result = sp.binomial(n, k)
        elif op in [20, 21, 22]:
            data = data.get('data')
            if data is None:
                return jsonify({'error': 'Missing data for mean/median/mode'}), 400
            data = [float(item) for item in data]
            result = (
                sp.mean(data) if op == 20 else
                sp.median(data) if op == 21 else
                sp.mode(data) if op == 22 else
                0
            )
        elif op in [23, 24]:
            data = data.get('data')
            if data is None:
                return jsonify({'error': 'Missing data for std/variance'}), 400
            data = [float(item) for item in data]
            mean = sp.mean(data)
            result = (
                sp.sqrt(sp.mean([(x - mean)**2 for x in data])) if op == 23 else
                sp.mean([(x - mean)**2 for x in data]) if op == 24 else
                0
            )
        elif op == 25:
            m = data.get('m')
            if m is None:
                return jsonify({'error': 'Missing m for lcm'}), 400
            result = sp.lcm(n, m)
        elif op == 26:
            m = data.get('m')
            if m is None:
                return jsonify({'error': 'Missing m for gcd'}), 400
            result = sp.gcd(n, m)
        elif op in [27, 28, 29]:
            result = (
                sp.Abs(n) if op == 27 else
                sp.floor(n) if op == 28 else
                sp.ceiling(n)
            )
        elif op in [30, 31, 32, 35, 36, 37]:
            matrix_rows = data.get('matrix_rows')
            matrix_cols = data.get('matrix_cols')
            matrix_data = data.get('matrix_data')
            if matrix_rows is None or matrix_cols is None or matrix_data is None:
                return jsonify({'error': 'Missing matrix dimensions or data'}), 400
            matrix_data = [float(item) for item in matrix_data]
            matrix = sp.Matrix(matrix_data).reshape(matrix_rows, matrix_cols)
            if op == 30:
                result = matrix.det()
            elif op == 31:
                result = matrix.inv()
            elif op == 32:
                result = matrix.T
            elif op == 35:
                result = matrix.eigenvals()
            elif op == 36:
                result = matrix.rank()
            elif op == 37:
                result = matrix.trace()
        elif op == 33:
            vector1_data = data.get('vector1_data')
            vector2_data = data.get('vector2_data')
            if vector1_data is None or vector2_data is None:
                return jsonify({'error': 'Missing vector data'}), 400
            vector1_data = [float(item) for item in vector1_data]
            vector2_data = [float(item) for item in vector2_data]
            vector1 = sp.Matrix(vector1_data)
            vector2 = sp.Matrix(vector2_data)
            result = vector1.dot(vector2)
        elif op == 34:
            vector1_data = data.get('vector1_data')
            vector2_data = data.get('vector2_data')
            if vector1_data is None or vector2_data is None:
                return jsonify({'error': 'Missing vector data'}), 400
            vector1_data = [float(item) for item in vector1_data]
            vector2_data = [float(item) for item in vector2_data]
            vector1 = sp.Matrix(vector1_data)
            vector2 = sp.Matrix(vector2_data)
            result = vector1.cross(vector2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result}), 200
    else:
        return jsonify({'error': 'Invalid operation'}), 400

if __name__ == '__main__':
    app.run(debug=True)

