def match_ends(words):
    '''return the count of the number of strings 
    where the string length is 2 or more and the 
    first and last chars of the string are the same.'''
    count = 0
    for x in words:
        if len(x) >= 2:
            if x[0] == x[-1]:
                count+=1
    return count

def front_x(words):
    '''eturn a list with the strings in sorted 
    in alphabetical order, except group all the strings 
    that begin with 'x' at he beginning of the list'''
    words = sorted(words)
    words_x = []
    words_nox = sorted(words)
    #strings begin with 'x' at he beginning of the list
    for z in words:
        if z[0] == "x":
            words_nox.remove(z)
            words_x.append(z)
    words_res =  words_x + words_nox
    return words_res

def sort_last(tuples):
    '''return a list of the same tuples, in 
    increasing order of the last item in each tuple'''
    s_list = sorted(tuples, key=lambda x: x[-1])
    return s_list

def remove_adjacent(nums):
    '''return a list where all equal elements 
    reduce to a single element if they are 
    adjacent (next to each other)'''
    s= [nums[0]]
    x = 0
    for y in nums:
        if y != s[x]:
            s.append(y)
            x += 1
    return s

def linear_merge(list1, list2):
    '''create and return a merged list of all the 
    elements in sorted order'''
    new_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            new_list.append(list1[0])
            list1.pop(0)
        else:
            new_list.append(list2[0])
            list2.pop(0)

    if len(list1) == 0:
        new_list = new_list + list2
    if len(list2) == 0:
        new_list = new_list + list1
    return new_list

def rotate(list1,number):
    '''rotate the elements in the list to 
    the right the amount of times given by the integer.'''
    while number != 0:
        list1.insert(0,list1[-1])
        list1.pop(-1)
        number -= 1
    return list1
