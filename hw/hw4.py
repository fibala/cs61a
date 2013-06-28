# Name:
# Login:
# TA:
# Section:
# Q1.

def pig_latin_original(w):
    """Return the Pig Latin equivalent of a lowercase English word w."""
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin_original(rest(w) + first(w))

def first(s):
    """Returns the first character of a string."""
    return s[0]

def rest(s):
    """Returns all but the first character of a string."""
    return s[1:]

def starts_with_a_vowel(w):
    """Return whether w begins with a vowel."""
    c = first(w)
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


def pig_latin(w):
    """Return the Pig Latin equivalent of a lowercase English word w.

    >>> pig_latin('pun')
    'unpay'
    >>> pig_latin('sphynx')
    'sphynxay'
    """
    "*** YOUR CODE HERE ***"
    def test_vowel(word,length):
        if starts_with_a_vowel(word) or length==0:
            return word + 'ay'
        else:
            return test_vowel(rest(word)+first(word),length-1)
    return test_vowel(w,len(w))
    
# Q2.

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game if we start
    with n disks on the start pole and want to move them all to the end pole.

    The game is to assumed to have 3 poles (which is traditional).

    >>> towers_of_hanoi(1, 1, 3)
    Move 1 disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 1 to rod 2
    Move 1 disk from rod 3 to rod 2
    Move 1 disk from rod 1 to rod 3
    Move 1 disk from rod 2 to rod 1
    Move 1 disk from rod 2 to rod 3
    Move 1 disk from rod 1 to rod 3
    """
    "*** YOUR CODE HERE ***"
    def move(n,start,middle,end):
        if n==1:
            move_disk(start,end)
            return
        else:
            move(n-1,start,end,middle)
            move_disk(start,end)
            move(n-1,middle,start,end)
    move(n,start,2,end)

def move_disk(start, end):
    print("Move 1 disk from rod", start, "to rod", end)

# Q3.

def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    >>> part(10)
    42
    >>> part(15)
    176
    >>> part(20)
    627
    """
    "*** YOUR CODE HERE ***"
    def helper(n,k):
        if n==0:
            return 1
        if k==0 or n<0:
            return 0
        return helper(n,k-1)+helper(n-k,k)
    return helper(n,n)
    
# Q4.

def summation(n, term):
    """Return the sum of the first n terms of a sequence.
  
    >>> summation(5, lambda x: pow(x, 3))
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    use_term= lambda x: odd_term if x==even_term else even_term
    def helper(k,term):
        if k==n:
            return term(k)
        return term(k)+helper(k+1,use_term(term))
    return helper(1,odd_term)
