# Kovas Jeleniauskas - Platform Based Computing Section 002
# Cite any sources you used to help with the homework including TAs and classmates

def string3(string):
    new_string = string[-2:]*3
    return new_string
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """


def has123(nums):
    for i in range(len(nums)):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere. 1,2,3 must occur in order.
    """


def hascode(string):
    count = 0
    for i in range(len(string)-3):
        if string[i] == 'c' and string[i+1] == 'o' and string[i+3] == 'e':
            count+=1       
    return count
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """


def samecatdog(string):
    cat_count = 0
    dog_count = 0
    for i in range(len(string)-2):
        if string[i:i+3] == "cat":
            cat_count += 1
        if string[i:i+3] == "dog":
            dog_count += 1
    if cat_count == dog_count:
        return True
    else:
        return False
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python string method ***
    """


def centered_avg(nums):
    largest = nums[0]
    smallest = nums[0]
    for i in nums:
        if largest < i:
            largest = i
        if smallest > i:
            smallest = i
    sum = 0
    for ii in nums:
        sum += ii
    diff = (largest + smallest)
    sum -= diff
    avg = sum//(len(nums)-2)
    return avg
    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """


# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")
print()

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1, 3]) is False, '[1, 1, 2, 4, 1, 3] does not have sequence 123'
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")
print()

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")
print()

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct")
print()

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")


# Problems found on https://codingbat.com/python
