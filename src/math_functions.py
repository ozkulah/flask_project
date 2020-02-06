from utilities import Utility


class MathFunctions:
    """This class have methods to calculate three algorithms ;

        calculate_fibonacci(self, fib):
        calculate_ackermann(self, m, n):
        calculate_factorial(self, fact):
    """

    def calculate_fibonacci_recursive(self, fib):
        """This method take fibonacci number checks it and calculate fibonacci value, recursively

            parameter n
        """
        if fib < 0:
            return Utility.not_positive
        elif fib == 0:  # First Fibonacci number is 0
            return 0
        elif fib == 1:  # Second Fibonacci number is 1
            return 1
        else:
            return self.calculate_fibonacci(fib - 1) + self.calculate_fibonacci(fib - 2)

    def calculate_fibonacci(self, n):
        """This method take fibonacci number checks it and calculate fibonacci value, iteratively

            parameter n
        """
        fib1, fib2 = 0, 1
        for i in range(0, n):
            fib1, fib2 = fib2, fib1 + fib2 #sum and swap values
        return fib1

    def calculate_ackermann(self, m, n):
        """This method take ackerman numbers checks them and calculate ackermann value, iterativey

            parameters m , n
        """
        ackermann_vals = []
        ackermann_vals.append(m)  # add value to stack
        while ackermann_vals:
            m = ackermann_vals.pop()
            if m == 0:
                n = n + 1
            elif n == 0:
                n = 1
                ackermann_vals.append(m - 1)  # add value to stack
            else:
                n = n - 1
                ackermann_vals.append(m - 1)  # add value to stack
                ackermann_vals.append(m)  # add value to stack
        return n

    def calculate_ackermann_recursive(self, m, n):
        """This method take ackerman numbers checks them and calculate ackermann value, recursively

            parameters m , n
        """
        if m == 0:
            return n + 1
        elif m > 0 and n == 0:
            return self.calculate_ackermann(m - 1, 1)
        elif m > 0 and n > 0:
            return self.calculate_ackermann(m - 1, self.calculate_ackermann(m, n - 1))

    def calculate_factorial(self, fact):
        """This method take factorial number checks it and calculate factorial value, iterativey

            parameter n
        """
        factorial = 1
        if fact >= 1:
            for i in range(1, fact + 1):
                factorial = factorial * i  # multiply values with itself
            return factorial
        elif fact == 0:
            return 1
        else:
            return Utility.not_positive
