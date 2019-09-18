.. pyLINQ documentation master file, created by
   sphinx-quickstart on Fri Sep 13 09:31:00 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyLINQ's documentation!
==================================

This library extends regular python lists to make them easier to filter and sort. Typical list comprehensions
such as [x for x in list] can quickly grow out of control for complicated behaviors. pyLINQ solves this
by replacing all features of list comprehensions with a series of methods that act on a list.

-----

Here is how easy it is to use:

>>> my_list = List([1,-9,5,2,1])
>>> my_list.select("abs(x)").where("x>3") # Get elements where the absolute value is greater than 3.
[9,5]
>>> my_list.first("x % 2 == 0") # Get the first even number
2
>>> nameList = List(['harry','tina','jeff','hank','john','tom','steve'])
>>> nameList.groupby("x[0]") # Group list elements by first letter in name.
[{'h': ['harry', 'hank']}, {'t': ['tina', 'tom']}, {'j': ['jeff', 'john']}, {'s': ['steve']}]
>>> nameList.orderby("x[0]").takewhile("x[0] < 'm'") # Get all names that come before letter 'm'.
['harry', 'hank', 'jeff', 'john']

============= ========================================================= =========
   List of Methods for List Object
---------------------------------------------------------------------------------
Method Name   Description                                                Output
============= ========================================================= =========
any           Returns true if any elements matches expression            bool
all           Returns true if all elements matches expression            bool
concat        Combines two lists into a single list                      List
count         Returns the number of elements that match expression       int
distinct      Returns all elements that are not duplicates               List
duplicate     Returns all elements that are duplicates                   List
element       Returns the element at a specific index                    element
except_set    Returns all elements except if they are in a second list   List
first         Returns the first element that matches an expression       element
groupby       Groups all value by a certain key                          List
intersect     Returns all elements common between two lists              List
last          Returns the last element that matches an expression        element
max           Returns the max element of the list                        element
min           Returns the min element of the list                        element
oftype        Returns all elements that match a certain type             List
orderby       Sort the elements                                          List
select        Perform an operation/function on list elements             List
skipwhile     Return all elements after an expression is true            List
sum           Return the sum of all elements                             float
takewhile     Return all elements before an expression is false          List
union         Return the combination of two lists                        List
where         Return all elements that meet an expression                List
============= ========================================================= =========

.. toctree::
   :maxdepth: 2

   example
   LINQ

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
