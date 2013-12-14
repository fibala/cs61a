class Rlist(object):

    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        "*** YOUR CODE HERE ***"
        return 1+len(self.rest)

    def __getitem__(self, index):
        "*** YOUR CODE HERE ***"
        if index==0:
            return self.first
        elif self.rest is Rlist.empty:
            print('Index out of bounds')
        else:
            return self.rest.__getitem__(index-1)

    def __repr__(self):
        "*** YOUR CODE HERE ***"
        if self.rest is Rlist.empty:
            return 'Rlist({0})'.format(self.first)
        else:
            return 'Rlist({0}, {1})'.format(self.first, self.rest)

def rlist_to_list(rlist):
    """Takes an RLIST and returns a Python list with the same
    elements.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    >>> rlist_to_list(rlist)
    [1, 2, 3, 4]
    >>> rlist_to_list(Rlist.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    save_list=[]
    while rlist is not Rlist.empty:
        save_list.append(rlist.first)
        rlist=rlist.rest
    return save_list

def insert(rlist, value, index):
    """Insert VALUE into the the RLIST at the given INDEX.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> insert(rlist, 9001, 0)
    >>> rlist
    Rlist(9001, Rlist(1, Rlist(2, Rlist(3))))
    >>> insert(rlist, 100, 2)
    >>> rlist
    Rlist(9001, Rlist(1, Rlist(100, Rlist(2, Rlist(3)))))
    """
    "*** YOUR CODE HERE ***"
    if index==0:
        rlist.rest=Rlist(rlist.first,rlist.rest)
        rlist.first=value
    elif rlist.rest is Rlist.empty:
        print('Index out of bounds')
    else:
        return insert(rlist.rest,value,index-1)

def reverse(rlist):
    """Returns an Rlist that is the reverse of the original.

    >>> Rlist(1).rest is Rlist.empty
    True
    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> reverse(rlist)
    Rlist(3, Rlist(2, Rlist(1)))
    >>> reverse(Rlist(1))
    Rlist(1)
    """
    "*** YOUR CODE HERE ***"
    temp=Rlist(rlist.first)
    while rlist.rest is not Rlist.empty:
        temp=Rlist(rlist.rest.first,temp)
        rlist=rlist.rest
    return temp


def type_tag(x):
    return type_tag.tags[type(x)]

# notice that type_tag is kind of unnecessary here
type_tag.tags = {
    list  : 'list',
    Rlist : 'Rlist',
}

def extend(seq1, seq2):
    """Takes the elements of seq2 and adds them to the end of seq1.

    >>> rlist = Rlist(4, Rlist(5, Rlist(6)))
    >>> lst = [1, 2, 3]
    >>> extend(lst, rlist)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    >>> rlist
    Rlist(4, Rlist(5, Rlist(6)))
    >>> extend(rlist, [7, 8])
    >>> rlist
    Rlist(4, Rlist(5, Rlist(6, Rlist(7, Rlist(8)))))
    >>> extend(lst, [7, 8, 9])
    >>> lst
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    "*** YOUR CODE HERE ***"
    types=(type_tag(seq1), type_tag(seq2))
    return extend.impl[types](seq1,seq2)

def ex_Rlist_list(rlist1,list2):
    if list2==[]:
        return
    elif rlist1.rest is Rlist.empty:
        rlist1.rest=Rlist(list2[0])
        list2=list2[1:]
    ex_Rlist_list(rlist1.rest,list2)

def ex_Rlist_Rlist(rlist1,rlist2):
    if rlist1.rest is Rlist.empty:
        rlist1.rest=rlist2
    else:
        ex_Rlist_Rlist(rlist.rest,rlist2)

extend.impl = {
  ('list', 'list')   : lambda list1,list2: list1.extend(list2),
  ('list', 'Rlist')  : lambda list1,rlist2: list1.extend(rlist_to_list(rlist2)), 
  ('Rlist', 'list')  : ex_Rlist_list, 
  ('Rlist', 'Rlist') : ex_Rlist_Rlist, 
}    


if __name__ == '__main__':
    from doctest import run_docstring_examples
    run_docstring_examples(rlist_to_list, globals(), True)
    run_docstring_examples(insert, globals(), True)
    run_docstring_examples(reverse, globals(), True)
    run_docstring_examples(extend, globals(), True)
