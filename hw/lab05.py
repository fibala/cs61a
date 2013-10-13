#2
def reverse_iter(tup):
    """Returns the reverse of the given tuple.

    >>> reverse_iter((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    "*** YOUR CODE HERE ***"
    new=()
    for i in range(len(tup)):
        new=(tup[i],)+new
    return new

def reverse_recursive(tup):
    """Returns the reverse of the given tuple.

    >>> reverse_revursive((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    "*** YOUR CODE HERE ***"
    if not tup:
        return ()
    return reverse_recursive(tup[1:])+(tup[0],)

#3
def merge_iter(tup1,tup2):
    """Merges two sorted tuples.

    >>> merge_iter((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge_iter((), (2, 4, 6))
    (2, 4, 6)
    >>> merge_iter((1, 2, 3), ())
    (1, 2, 3)
    """
    "*** YOUR CODE HERE ***"
    new=()
    while tup1 and tup2:
        if tup1[0] < tup2[0]:
            new=new+(tup1[0],)
            tup1=tup1[1:]
        else:
            new=new+(tup2[0],)
            tup2=tup2[1:]
    if tup1:
        new=new+tup1
    else:
        new=new+tup2
    return new

def merge_recursive(tup1,tup2):
    """Merges two sorted tuples.

    >>> merge_recursive((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge_recursive((), (2, 4, 6))
    (2, 4, 6)
    >>> merge_recursive((1, 2, 3), ())
    (1, 2, 3)
    """
    "*** YOUR CODE HERE ***"
    if not tup1 or not tup2:
        return tup1+tup2
    elif tup1[0] < tup2[0]:
        return (tup1[0],)+merge_recursive(tup1[1:],tup2)
    else:
        return (tup2[0],)+merge_recursive(tup1,tup2[1:])

#4
def deep_len(tup):
    """Returns the deep length of the tuple.

    >>> deep_len((1, 2, 3))      # normal tuple
    3
    >>> x = (1, (2, 3), 4)       # deep tuple
    >>> deep_len(x)
    4
    >>> y = ((1, (1, 1)), 1, (1, 1))  # deep tuple
    >>> deep_len(y)
    6
    """
    "*** YOUR CODE HERE ***"
    if not tup:
        return 0
    elif type(tup[0])==tuple:
        return deep_len(tup[0])+deep_len(tup[1:])
    else:
        return 1+deep_len(tup[1:])

#recursive Lists
empty_rlist = None

def rlist(first, rest=empty_rlist):
    return (first, rest)

def first(rlist):
    return rlist[0]

def rest(rlist):
    return rlist[1]

#5
def tup_to_rlist(tup):
    """Converts a tuple to an rlist.

    >>> tup = (1, 2, 3, 4)
    >>> r = tup_to_rlist(tup)
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    3
    >>> r = tup_to_rlist(())
    >>> r is empty_rlist
    True
    """
    "***YOUR CODE HERE ***"
    if not tup:
        return empty_rlist
    return rlist(tup[0],tup_to_rlist(tup[1:]))

def tup_to_rlist_w(tup):
    new=empty_rlist
    while tup:
        new=rlist(tup[-1],new)
        tup=tup[:-1]
    return new

#6
def len_rlist(lst):
    """Returns the length of the rlist.

    >>> lst = tup_to_rlist((1, 2, 3, 4))
    >>> len_rlist(lst)
    4
    >>> lst = tup_to_rlist(())
    >>> len_rlist(lst)
    0
    """
    "*** YOUR CODE HERE ***"
    length=0
    while lst != empty_rlist:
        length+=1
        lst=rest(lst)
    return length

def len_rlist_w(lst):
    if lst == empty_rlist:
        return 0
    return 1+len_rlist_recursive(rest(lst))

def getitem_rlist(i, lst):
    """Returns the ith item in the rlist. If the index exceeds the
    length of the rlist, return 'Error'.

    >>> lst = tup_to_rlist((1, 2, 3, 4))
    >>> getitem_rlist(0, lst)
    1
    >>> getitem_rlist(3, lst)
    4
    >>> getitem_rlist(4, lst)
    'Error'
    """
    "*** YOUR CODE HERE ***"
    if lst == empty_rlist:
        return 'Error'
    elif i==0:
        return first(lst)
    else:
        return getitem_rlist(i-1,rest(lst))

def getitem_rlist_w(i, lst):
    while i >=0 and lst!=empty_rlist:
        if i==0:
            return first(lst)
        else:
            lst=rest(lst)
            i-=1
    return 'Error'

#7
empty_rlist = lambda x: x

def rlist(first, rest=empty_rlist):
    return lambda x: first if x == 'hi' else rest

def first(lst):
    return lst('hi')

def rest(lst):
    return lst('lol')

