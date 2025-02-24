True and 13
13

False or 0
0

not 10
False

not None
True

True and 1 / 0
"ZeroDivisionError: division by zero"

True or 1 / 0
True

-1 and 1 > 0
True

-1 or 5
-1

(1 + 1) and 1
1

print(3) or ""
3
""

def f(x):
     if x == 0:
         return "zero"
     elif x > 0:
         return "positive"
     else:
         return ""
0 or f(1)
"positive"

f(0) or f(-1)
"zero"

f(0) and f(-1)
""

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
chocolate = cake()
"beets"

chocolate
def pie()

chocolate()
"sweets"
"cake"

more_chocolate, more_cake = chocolate(), cake
"sweets"

more_chocolate
"cake"

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y
snake(10, 20)
def pie()

snake(10, 20)()
"sweets"
"cake"

cake = 'cake'
snake(10, 20)
30


lambda x: x  # A lambda expression with one parameter x
<function __main__.<lambda>(x)>

a = lambda x: x  # Assigning the lambda function to the name a
a(5)
5

(lambda: 3)()  # Using a lambda expression as an operator in a call exp.
3

b = lambda x, y: lambda: x + y  # Lambdas can return other lambdas!
c = b(8, 4)
c
<function __main__.<lambda>.<locals>.<lambda>()>
c()
12

d = lambda f: f(4)  # They can have functions as arguments as well.
def square(x):
    return x * x
d(square)
16

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g)  # Which argument belongs to which function call?
TypeError

higher_order_lambda(g)(2)
4

call_thrice = lambda f: lambda x: f(f(f(x)))
call_thrice(lambda y: y + 1)(0)
3

print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
print_lambda
<function __main__.<lambda>(z)>

one_thousand = print_lambda(1000)
1000

one_thousand # What did the call to print_lambda return?


def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    return lambda x: f(g(x)) == g(f(x))


def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    """Return whether positive integer n is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def counter(N):
        count = 0 
        for i in range(1, N + 1):
            if condition(N, i):  
                count += 1  
        return count 
    return counter


def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    return a * b // gcd(a, b)




def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def apply_n_times(n):
        def final_function(x):
            functions = [f1, f2, f3]
            for i in range(n):
                x = functions[i % 3](x)  # Alterner entre f1, f2 et f3
            return x
        return final_function
    return apply_n_times


