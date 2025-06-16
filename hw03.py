from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


HW_SOURCE_FILE=__file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    result = 1
    for n in range(1, n + 1):
        result *= term(n)
    return result


def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    result = start
    for n in range(1, n + 1):
        result = fuse(result, term(n))
    return result
        


def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square) # square(1) + square(2) + ... + square(4) + square(5)
    55
    >>> summation_using_accumulate(5, triple) # triple(1) + triple(2) + ... + triple(4) + triple(5)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square) # square(1) * square(2) * square(3) * square()
    576
    >>> product_using_accumulate(6, triple) # triple(1) * triple(2) * ... * triple(5) * triple(6)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)


def funception(func1, begin):
    """ Takes in a function (func1) and a begin value.
    Returns a function (func2) that will find the product of
    func1 applied to the range of numbers from
    begin (inclusive) to end (exclusive)

    >>> def increment(num):
    ...     return num + 1
    >>> def double(num):
    ...     return num * 2
    >>> g1 = funception(increment, 0)
    >>> g1(3)    # increment(0) * increment(1) * increment(2) = 1 * 2 * 3 = 6
    6
    >>> g1(0)    # Returns 1 because begin >= end
    1
    >>> g1(-1)   # Returns 1 because begin >= end
    1
    >>> g2 = funception(double, 1)
    >>> g2(3)    # double(1) * double(2) = 2 * 4 = 8
    8
    >>> g2(4)    # double(1) * double(2) * double(3) = 2 * 4 * 6 = 48
    48
    >>> g3 = funception(increment, -3)
    >>> g3(-1)   # increment(-3) * increment(-2) = -2 * -1 = 2
    2
    """
    def func2(end):
        if begin >= end:
            return 1
        result = 1
        for i in range(begin, end):
            result *= func1(i)
        return result
    return func2

