import sys
print(sys.getrecursionlimit())  # default recursion limit

sys.setrecursionlimit(3000)  # set recursion limit
print(sys.getrecursionlimit())  # new recursion limit

def hello():
    print("Hello, World!")
    hello()
hello()    