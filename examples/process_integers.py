from pyLINQ import *

def main():
    int_list = List([2,4,6,5])
    other_int_list = List([1,2,2,3,4,4,5])
    # Sum examples
    print("Sum using conditional statement x > 3 : ", other_int_list.sum("x > 3"))
    print("Sum using operation x - 2 : ", other_int_list.sum("x - 2"))
    # chaining expresions example
    print("finding the maximum of the square of the odds: ", other_int_list.where("x % 2 != 0").select("x**2").max())
    # counting
    print("counting the number of evens in both lists: ", int_list.concat(other_int_list).count("x % 2 == 0"))

if __name__ == "__main__":
    main()
