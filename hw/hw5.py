# Name:
# Login:
# TA:
# Section:
# Q1.

empty_rlist = None

def rlist(first, rest):
    """Construct a recursive list from its first element and the
    rest."""
    return (first, rest)

def first(s):
    """Return the first element of a recursive list s."""
    return s[0]

def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]


def reverse_rlist_iterative(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_iterative(primes)
    (7, (5, (3, (2, None))))
    """
    "*** YOUR CODE HERE ***"
    new_rlist=(first(s),empty_rlist)
    while rest(s) != empty_rlist:
        s=rest(s)
        new_rlist=rlist(first(s),new_rlist)
    return new_rlist

def reverse_rlist_recursive(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_recursive(primes)
    (7, (5, (3, (2, None))))
    """
    "*** YOUR CODE HERE ***"
    def helper(s, new_rlist):
        if rest(s) == empty_rlist:
            new_rlist = rlist(first(s), new_rlist)
            return new_rlist
        else: 
            new_rlist = rlist(first(s), new_rlist)
            return helper(rest(s), new_rlist)
    return helper(s, empty_rlist)
    
# Q2.

def interleave_recursive(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive
    list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_recursive(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_recursive(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_recursive(odds, odds)
    (1, (1, (3, (3, None))))
    """
    "*** YOUR CODE HERE ***"
    def join(list1,list2):
        list1=reverse_rlist_recursive(list1)
        while list1 != empty_rlist:
            list1,list2=rest(list1),rlist(first(list1),list2)
        return list2
        
    def helper(s0,s1,new_rlist):
        if s0 == empty_rlist:
            return join(new_rlist,s1)
        if s1 == empty_rlist:
            return join(new_rlist,s0)
        new_rlist=join(new_rlist,rlist(s0[0],empty_rlist))
        new_rlist=join(new_rlist,rlist(s1[0],empty_rlist))
        return helper(rest(s0),rest(s1),new_rlist)
    return helper(rest(s0), rest(s1), rlist(s0[0], rlist(s1[0], empty_rlist)))

def interleave_iterative(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive
    list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_iterative(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_iterative(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_iterative(odds, odds)
    (1, (1, (3, (3, None))))
    """
    "*** YOUR CODE HERE ***"
    def join(list1,list2):
        list1=reverse_rlist_iterative(list1)
        while list1 != empty_rlist:
            list1,list2=rest(list1),rlist(first(list1),list2)
        return list2
    new_rlist=join(rlist(s0[0],empty_rlist),rlist(s1[0],empty_rlist))
    print(new_rlist)
    s0=rest(s0)
    s1=rest(s1)  
    while s0 != empty_rlist and s1 != empty_rlist:        
        new_rlist=join(new_rlist,rlist(s0[0],empty_rlist))
        new_rlist=join(new_rlist,rlist(s1[0],empty_rlist))
        print(new_rlist,'ccc',s0,s1)
        s0=rest(s0)
        s1=rest(s1)
        print (s0,'aaa',s1,'bbb')
    if s0 != empty_rlist:
        new_rlist=join(new_rlist,s0)
    if s1 != empty_rlist:
        new_rlist=join(new_rlist,s1)
    return new_rlist

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


# Q3.

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return (a,b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

# Q4.

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x
    divided by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert (lower_bound(y)>0 or upper_bound(y)<0),"interval that spans zero"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q5.

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    opposite_y=interval(-upper_bound(y),-lower_bound(y))
    return add_interval(x,opposite_y)

# Q6.

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    "*** YOUR CODE HERE ***"
    return make_center_width(c,abs(c*p/100))

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    "*** YOUR CODE HERE ***"
    upper,lower=upper_bound(x),lower_bound(x)
    return abs((upper-lower)/(upper+lower))*100

# Q7.

def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b,
    and c, for domain interval x.

    This is the less accurate version which treats each instance of t as a
    different value from the interval. See the extra for experts question for
    exploring why this is not _really_ correct and to write a more precise
    version.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-9 to 5'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '-6 to 16'
    """
    "*** YOUR CODE HERE ***"
    tt=mul_interval(x,x)
    lower_tt=min(a*lower_bound(tt),a*upper_bound(tt))
    upper_tt=max(a*lower_bound(tt),a*upper_bound(tt))
    att=interval(lower_tt,upper_tt)
    lower_t=min(b*lower_bound(x),b*upper_bound(x))
    upper_t=max(b*lower_bound(x),b*upper_bound(x))
    bt=interval(lower_t,upper_t)
    attbt=add_interval(att,bt)
    fx=interval(lower_bound(attbt)+c,upper_bound(attbt)+c)
    return fx
    
# Q8.

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))


# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
r1 = interval(1,4)
r2 = interval(2,5)
par1(r1,r2)
par2(r1,r2)
    
# Q9.

def multiple_reference_explanation():
  return """The multiple reference problem..."""

# Q10.

def accurate_quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b,
    and c, for domain interval x.

    >>> str_interval(accurate_quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(accurate_quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        return a*x*x+b*x+c
    extreme_point=-b/(2*a)
    if extreme_point <= lower_bound(x) or extreme_point >= upper_bound(x):
        max_x=max(f(upper_bound(x)),f(lower_bound(x)))
        min_x=min(f(upper_bound(x)),f(lower_bound(x)))
    else:
        max_x=max(f(upper_bound(x)),f(lower_bound(x)),f(extreme_point))
        min_x=min(f(upper_bound(x)),f(lower_bound(x)),f(extreme_point))       
    return interval(min_x,max_x)


