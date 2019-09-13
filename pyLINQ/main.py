from collections.abc import MutableSequence
from functools import reduce, singledispatch, update_wrapper, wraps
from inspect import getsource
from types import LambdaType

def handle_inputs(conditional_statement=True):
    def decorator(func):
        @wraps(func)
        def wrapper(self, expression=None, *args, **kwargs):
            # Return empty list if empty
            if len(self._list) == 0:
                return self.__class__()
            funcname = "List.{}".format(func.__name__)
            expressionType = type(expression)
            # Get type and check that it's proper.
            if conditional_statement:
                if expressionType == str:
                    if not any(operator for operator in self.operators if operator in expression):
                        raise TypeError("{}('expression') requires a conditional expression.".format(funcname))
                elif expressionType == LambdaType:
                    if not any(operator for operator in self.operators if operator in getsource(expression)):
                        raise TypeError("{}('expression') requires a conditional expression.".format(funcname))
            # Convert str to lambda expression, else raise error.
            if expressionType == str:
                expression = eval("lambda x: {}".format(expression))
            elif expressionType == type(None):
                expression = eval("lambda x : x")
            elif expressionType != LambdaType:
                raise NotImplementedError("Unsupported type: {}. {}('expression') requires {} or {}.".format(expressionType, funcname, str, LambdaType))
            return func(self, expression, *args, **kwargs)
        return wrapper
    return decorator

def enforce_list_input(func):
    @wraps(func)
    def wrapper(self, other):
        if other.__class__ != self.__class__:
            raise TypeError("parameter must be type {}.".format(self.__class__))
        return func(self, other)
    return wrapper

def element_error(item, message):
    print("Element '{}' produced the following {}: {}".format(item, message.__class__.__name__, message))

class List(MutableSequence):
    """Object which extends python list object to include LINQ style queries."""
    #region Class fields
    operators = ["==","!=","<",">", "<=",">="]
    #endregion
    #region Extended List methods
    def __init__(self, data=None):
        super().__init__()
        if data:
            self._list = list(data)
        else:
            self._list = list()

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.__dict__ == other.__dict__)

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, ii):
        return self._list[ii]

    def __delitem__(self, ii):
        del self._list[ii]

    def __setitem__(self, ii, val):
        self._list[ii] = val

    def __str__(self):
        return str(self._list)

    def __add__(self, other):
        return self.__class__(self._list + other._list)

    def __iadd__(self, val):
        self.insert(len(self._list), val)
        return self

    def __sub__(self, other):
        for item in other._list:
            try:
                self._list.remove(item)
            except:
                pass
        return self.__class__(self._list)

    def __isub__(self, val):
        try:
            self._list.remove(val)
        except:
            pass
        return self

    def append(self, val):
        self._list.append(val)

    def clear(self):
        self._list.clear()

    def insert(self, ii, val):
        self._list.insert(ii, val)

    def pop(self, ii):
        self._list.pop(ii)

    def remove(self, val):
        self._list.remove(val)
    #endregion
    #region Custom LINQ style methods
    @handle_inputs(conditional_statement=True)
    def any(self, expression):
        """ Checks to see if any items in a list meet a conditional criteria. E.g. List.any("x > 0")

        :param expression: The expression to apply to the List object. Can either take a string "x > 0" or a lambda expression lambda x : x > 0.
        :type expression: str or LambdaType.
        :returns: a new List object that results from the applied expression.

        """
        newresult = False
        for item in self._list:
            try:
                if expression(item):
                    newresult = True
                    break
            except Exception as message:
                element_error(item, message)
        return newresult

    @handle_inputs(conditional_statement=True)
    def all(self, expression):
        newresult = True
        for item in self._list:
            try:
                if not expression(item):
                    newresult = False
                    break
            except Exception as message:
                element_error(item, message)
                newresult = False
                break
        return newresult

    @handle_inputs(conditional_statement=True)
    def count(self, expression=None):
        newcount = 0
        for item in self._list:
            try:
                if expression(item):
                    newcount += 1
            except Exception as message:
                element_error(item, message)
        return newcount

    @handle_inputs(conditional_statement=True)
    def distinct(self, expression=None):
        newlist = []
        for item in self._list:
            try:
                if expression(item) and item not in newlist:
                    newlist.append(item)
            except Exception as message:
                element_error(item, message)
        return self.__class__(newlist)

    @handle_inputs(conditional_statement=True)
    def duplicate(self, expression=None):
        corelist = []
        newlist = []
        for item in self._list:
            try:
                if expression(item) and item not in corelist:
                    corelist.append(item)
                elif expression(item) and item in corelist and item not in newlist:
                    newlist.append(item)
            except Exception as message:
                element_error(item, message)
        return self.__class__(newlist)

    @handle_inputs(conditional_statement=True)
    def first(self, expression=None):
        result = None
        for item in self._list:
            try:
                if expression(item):
                    result = item
                    break
            except Exception as message:
                element_error(item, message)
        return result

    @handle_inputs(conditional_statement=False)
    def groupby(self, expression):
        newdict = {}
        for item in self._list:
            try:
                expression_key = expression(item)
                if not (expression_key in newdict):
                    newdict[expression_key] = [item]
                else:
                    newdict[expression_key].append(item)
            except Exception as message:
                element_error(item, message)

        newlist = [{k:v} for k,v in newdict.items()]
        return self.__class__(newlist)

    @handle_inputs(conditional_statement=True)
    def last(self, expression=None):
        result = None
        for item in self._list[::-1]:
            try:
                if expression(item):
                    result = item
                    break
            except Exception as message:
                element_error(item, message)
        return result

    @handle_inputs(conditional_statement=False)
    def max(self, expression=None):
        newlist = []
        for item in self._list:
            try:
                if isinstance(expression(item),bool) and expression(item) and item not in newlist:
                    newlist.append(item)
                elif not isinstance(expression(item),bool) and item not in newlist:
                    _ = expression(item) > 0 # make sure that all elements can be operated on with > sign.
                    newlist.append(expression(item))
            except Exception as message:
                element_error(item, message)
        if not newlist:
            return None
        return reduce(lambda a,b : a if a > b else b, newlist)

    @handle_inputs(conditional_statement=False)
    def min(self, expression=None):
        newlist = []
        for item in self._list:
            try:
                if isinstance(expression(item),bool) and expression(item) and item not in newlist:
                    newlist.append(item)
                elif not isinstance(expression(item),bool) and item not in newlist:
                    _ = expression(item) < 0 # make sure that all elements can be operated on with < sign.
                    newlist.append(expression(item))
            except Exception as message:
                element_error(item, message)
        if not newlist:
            return None
        return reduce(lambda a,b : a if a < b else b, newlist)

    @handle_inputs(conditional_statement=False)
    def orderby(self, expression=None, reverse=False):
        newlist = self._list.copy()
        newlist.sort(key=expression, reverse=reverse)
        return self.__class__(newlist)

    @handle_inputs(conditional_statement=False)
    def select(self, expression):
        newlist = []
        for item in self._list:
            try:
                newlist.append(expression(item))
            except Exception as message:
                newlist.append(item)
                element_error(item, message)
        return self.__class__(newlist)

    @handle_inputs(conditional_statement=True)
    def skipwhile(self, expression):
        skiplist = []
        for item in self._list:
            try:
                if expression(item):
                    skiplist.append(item)
                else:
                    break
            except Exception as message:
                element_error(item, message)
                break
        newlist = [x for x in self._list if x not in skiplist]
        return self.__class__(newlist)

    @handle_inputs(conditional_statement=False)
    def sum(self, expression=None):
        newlist = []
        for item in self._list:
            try:
                if isinstance(expression(item),bool) and expression(item):
                    newlist.append(item)
                elif not isinstance(expression(item),bool):
                    _ = expression(item) + 0 # make sure that all elements can be operated on with + sign.
                    newlist.append(expression(item))
            except Exception as message:
                element_error(item, message)
        if not newlist:
            return(None)
        return reduce(lambda a,b : a+b, newlist)

    @handle_inputs(conditional_statement=True)
    def takewhile(self, expression):
        newlist = []
        for item in self._list:
            try:
                if expression(item):
                    newlist.append(item)
                else:
                    break
            except Exception as message:
                element_error(item, message)
                break
        return self.__class__(newlist)

    @handle_inputs(conditional_statement=True)
    def where(self, expression):
        """Produces where statement"""
        newlist = []
        for item in self._list:
            try:
                if expression(item):
                    newlist.append(item)
            except Exception as message:
                element_error(item, message)
        return self.__class__(newlist)
    #endregion
    #region Set Methods
    @enforce_list_input
    def concat(self, other):
        return (self._list + other._list)

    @enforce_list_input
    def except_set(self, other):
        newlist = []
        for item in self._list:
            if  item not in newlist and item not in other._list:
                newlist.append(item)
        return self.__class__(newlist)

    @enforce_list_input
    def intersect(self, other):
        newlist = []
        for item in self._list:
            if  item not in newlist and item in other._list:
                newlist.append(item)
        return self.__class__(newlist)

    @enforce_list_input
    def union(self, other):
        newlist = []
        for item in self._list:
            if  item not in newlist:
                newlist.append(item)
        for item in other._list:
            if item not in newlist:
                newlist.append(item)
        return self.__class__(newlist)
    #endregion
    #region Methods without handle_input
    def oftype(self, elementType):
        """ Checks to see if any items in a list are of a certain type. E.g. List.oftype(int)

        :param elementType: The expression to apply to the List object. Can either take a string "int","dict","List", etc. or a type.
        :type elementType: str or type.
        :returns: a new List object that contains only items of the specified type.

        """
        try:
            if isinstance(elementType, str):
                elementType = eval(elementType)
        except:
            raise NameError("'{}' is not a valid python type, or a valid class name.".format(elementType))
        newlist = []
        for item in self._list:
            if isinstance(item, elementType):
                newlist.append(item)
        return self.__class__(newlist)

    def element(self, number):
        try:
            result = self._list[ii]
        except:
            result = None
        return result
    #endregion
