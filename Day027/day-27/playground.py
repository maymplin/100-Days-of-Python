def add(*args):
    print(type(args))   # *args are actually passed in as a tuple
    # nums = [num for num in args]
    # return sum(nums)
    return sum(args)


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))