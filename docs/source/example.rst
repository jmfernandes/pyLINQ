Example Usage
=============

>>> int_list = List([2,4,6,5])
>>> other_int_list = List([1,2,2,3,4,4,5])
>>> # Sum examples
>>> other_int_list.sum("x > 3") # Sum using conditional statement x > 3
(4 + 4 + 5) = 13
>>> other_int_list.sum("x - 2") # Sum using operation x - 2
(-1 + 0 + 0 + 1 + 2 + 2 + 3) = 7
>>> # chaining expressions example
>>> other_int_list.where("x % 2 != 0").select("x**2").max() # finding the maximum of the square of the odds
max(1,9,25) = 25
>>> # counting
>>> int_list.concat(other_int_list).count("x % 2 == 0") # counting the number of evens in both lists
count(2,4,6,2,2,4,4) = 7
