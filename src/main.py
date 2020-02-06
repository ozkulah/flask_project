import time
from quart import Quart
from quart import request
from quart import jsonify
from math_functions import MathFunctions
from utilities import Utility
from asgiref.sync import sync_to_async

app = Quart(__name__)


@app.route('/fibonacci', methods=['GET', 'POST'])
async def fibonacci():
    """This service checks the values and calls fibonacci method to calculate result

        parameters: n
    """
    start_time = time.time()
    fib = request.args.get('n')  # Get n value from service
    # Checking values for int or not
    try:
        fib = int(fib)
    except:
        return Utility.not_number
    # Checking the limits for fibonacci
    if fib < 0:
        return Utility.not_suitable
    else:
        math = MathFunctions()
        # It can be take too much time, it is called async
        result = await sync_to_async(math.calculate_fibonacci)(fib)

    # print("Fibonacci result: {}".format(result))
    return jsonify(
        "N : {}, Fibonacci Result: {}, Total Time: {:.4f} sec".format(fib, result, (time.time() - start_time)))


@app.route('/ackermann', methods=['GET', 'POST'])
async def ackermann():
    """This service checks the values and calls ackerman method to calculate  result

        parameters: m ,n
    """
    start_time = time.time()
    m = request.args.get('m')  # Get m value from service
    n = request.args.get('n')  # Get n value from service
    # Checking values for int or not
    try:
        m = int(m)
        n = int(n)
    except:
        return Utility.not_number

    # Checking the limits for ackermann
    if m < 0 or n < 0:
        return Utility.not_positive

    math = MathFunctions()
    # It can be take too much time, it is called async
    result = await sync_to_async(math.calculate_ackermann)(m, n)
    # print("Ackermann result: {}".format(result))
    return jsonify(
        "M : {}, N : {}, Ackermann Result: {}, Total Time: {:.4f} sec".format(m, n, result, (time.time() - start_time)))


@app.route('/factorial', methods=['GET', 'POST'])
async def factorial():
    """This service checks the value and calls factorial method to calculate  result

        parameters: n
    """
    start_time = time.time()
    fact = request.args.get('n')  # Get n value from service
    # Checking values for int or not
    try:
        fact = int(fact)
    except:
        return Utility.not_number

    # Checking the limits for factorial
    if fact < 0:
        return Utility.not_positive

    math = MathFunctions()
    # It can be take too much time, it is called async
    result = await sync_to_async(math.calculate_factorial)(fact)
    # print("Factorial result: {}".format(result))
    return jsonify(
        "N : {}, Factorial Result: {}, Total Time: {:.4f} sec".format(fact, result, (time.time() - start_time)))


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=8000)
