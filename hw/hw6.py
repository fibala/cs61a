# Name:
# Login:
# TA:
# Section:
# Q1.

def divide_by_fact(dividend, n):
    """Recursively divide dividend by the factorial of n.

    >>> divide_by_fact(120, 4)
    5.0
    """
    if n < 0:
        return dividend
    return divide_by_fact(dividend / n, n - 1)

# Q2.

def group(seq):
    """Divide a sequence of at least 12 elements into groups of 4 or
    5. Groups of 5 will be at the end. Returns a tuple of sequences, each
    corresponding to a group.

    >>> group(range(14))
    (range(0, 4), range(4, 9), range(9, 14))
    >>> group(tuple(range(17)))
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15, 16))
    """
    num = len(seq)
    assert num >= 12
    "*** YOUR CODE HERE ***"
    newgroup=[]
    while num>15:
        newgroup.append(seq[0:4])
        seq=seq[4:]
        num-=4
    if num==12: temp=(4,4,4)
    if num==13: temp=(4,4,5)
    if num==14: temp=(4,5,5)
    if num==15: temp=(5,5,5)
    for i in temp:
        newgroup.append(seq[0:i])
        seq=seq[i:]
        num-=i
    return tuple(newgroup)
    

"""

   ====
    ==
========== <--- spatula underneath this crust
 ========

    ||
    ||
   \||/
    \/

========== }
    ==     } flipped
   ====    }
 ========

"""

# Q3.

def partial_reverse(lst, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"
    for i in lst[start:]:
        lst.insert(start,i)
        lst.pop()

# Q4.

def index_largest(seq):
    """Return the index of the largest element in the sequence.

    >>> index_largest([8, 5, 7, 3 ,1])
    0
    >>> index_largest((4, 3, 7, 2, 1))
    2
    """
    assert len(seq) > 0
    "*** YOUR CODE HERE ***"
    temp,num=seq[0],0
    for i in range(1,len(seq)):
        if seq[i]>temp:
            temp=seq[i]
            num=i
    return num
        

# Q5.

def pizza_sort(lst):
    """Perform an in-place pizza sort on the given list, resulting in
    elements in descending order.

    >>> a = [8, 5, 7, 3, 1, 9, 2]
    >>> pizza_sort(a)
    >>> a
    [9, 8, 7, 5, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    length=len(lst)
    def helper(lst,first=0):
        if first==length-1:
            return
        largest=index_largest(lst[first:])+first
        lst[largest],lst[first]=lst[first],lst[largest]
        helper(lst,first+1)
    return helper(lst)    
        
def merge_sort(lst):
    if len(lst)<=1:
        return lst
    half=len(lst)//2
    left=pizza_sort(lst[:half])
    right=pizza_sort(lst[half:])
    print ('cc',lst)
    merge(left,right)
def merge(left,right):
    result=[]
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]>=right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right=right[1:]
        elif len(left)>0:
            result.append(left[0])
            left=left[1:]
        elif len(right)>0:
            result.append(right[0])
            right=right[1:]
    print (result)
    return result


# Q6.

def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    sum_n=[]
    def accumulator(n):
        sum_n.append(n)
        all=0
        for i in sum_n:
            all+=i
        return all
    return accumulator


# Q7.

def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"
    sum_n=0
    def accumulator(n):
        nonlocal sum_n
        sum_n+=n
        return sum_n
    return accumulator


# Q8.

# Old version
def count_change(a, coins=(50, 25, 10, 5, 1)):
    if a == 0:
        return 1
    elif a < 0 or len(coins) == 0:
        return 0
    return count_change(a, coins[1:]) + count_change(a - coins[0], coins)

# Version 2.0
def make_count_change():
    """Return a function to efficiently count the number of ways to make
    change.

    >>> cc = make_count_change()
    >>> cc(500, (50, 25, 10, 5, 1))
    59576
    """
    "*** YOUR CODE HERE ***"

