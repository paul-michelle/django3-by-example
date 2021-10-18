numbers = [0,1,2,3,4,5,6,7,8,9]
sqr_list_func = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
sqr_list_comp = [x**2 for x in numbers if not x % 2]
print(sqr_list_comp == sqr_list_func)
