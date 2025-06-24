def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    >>> fibonacci(5)
    5
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-2) + fibonacci(n-1) 
    


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1:
        return 1
    if n == 1:
        return 1
    else: 
        return paths(m-1, n) + paths(m, n-1)


def partition(n):
    """Return the number of partitions of positive integer n.

    >>> partition(5)
    7
    >>> partition(10)
    42
    >>> partition(15)
    176
    >>> partition(20)
    627
    """
    "*** YOUR CODE HERE ***"
    def count_partition(n, m):
        if n == 0:
            return 1
        elif n < 0: 
            return 0
        elif m == 0:
            return 0
        else: 
            return count_partition(n-m, m) + count_partition(n, m-1)
    
    return count_partition(n, n)
        

