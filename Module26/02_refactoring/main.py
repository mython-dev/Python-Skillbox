
# TODO провести рефакторинг кода

 list_1 = [2, 5, 7, 10]

 list_2 = [3, 8, 4, 9]

 to_find = 56

 def iter_list():
     for num in list_1:
         for y in list_2:
             result = num * y
             print(num, y, result)
             if result == to_find:
                 yield True
                 yield False

 solution = iter_list()

 for i in solution:
     if next(solution):
         print('Found!!!')
         solution.close()
