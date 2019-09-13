.. pyLINQ documentation master file, created by
   sphinx-quickstart on Fri Sep 13 09:31:00 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyLINQ's documentation!
==================================

This library makes filtering and sorting lists easier.

-----

Here is how easy it is to use

>>> my_list = List([1,-9,5,2,1])
>>> my_list.select("abs(x)").where("x>3") # get all elements where the absolute value is greater than 3.
[9,5]
>>> my_list.first("x % 2 == 0") # get the first even number

Here is a list of functions

============= =========================== ======
   List of Methods for List Object
------------------------------------------------
function name example call with parameter output
============= =========================== ======
any           False                       False
all           False                       True
concat        True                        True
count         True                        True
distinct      True                        True
duplicate     False                       False
element       True                        True
except_set    False                       True
first         True                        True
groupby       True                        True
intersect     True                        True
last          True                        True
max           True                        True
min           True                        True
oftype        True                        True
orderby       True                        True
select        True                        True
skipwhile     True                        True
sum           True                        True
takewhile     True                        True
union         True                        True
where         True                        True
============= =========================== ======

.. toctree::
   :maxdepth: 2

   example
   LINQ

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
