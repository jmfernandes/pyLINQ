from pyLINQ import *

def main():
    students = List([
    {"firstname": "terry", "lastname": "adams", "ID": 120, "scores": [99,82,81,79]},
    {"firstname": "fadi", "lastname": "fakhouri", "ID":116, "scores": [99,86,90,94]},
    {"firstname": "john", "lastname": "williamson", "ID":113, "scores": [63,62,80,87]},
    {"firstname": "james", "lastname": "foo", "ID":125, "scores": [90,84,87,81]},
    {"firstname": "steve", "lastname": "smith", "ID":117, "scores": [96,95,94,96]},
    ])
    # using group by
    print("grouping students by first latter of last name: ")
    for item in students.groupby("x['lastname'][0]"):
        print(item)
    # using select to return subset of information
    print(" ")
    print("using select to return subset of information")
    print(students.where("x['ID'] > 116").select("(x['lastname'],x['firstname'])"))
    # same statements as above but using lambda expressions
    print(" ")
    print("===== same thing but using lambda formats =====")
    print(" ")
    for item in students.groupby(lambda x : x['lastname'][0]):
        print(item)
    print(students.where(lambda x : x['ID'] > 116).select(lambda x : (x['lastname'],x['firstname'])))

if __name__ == "__main__":
    main()
