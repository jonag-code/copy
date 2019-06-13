from Jmodule import jfilename, jstring, Sub_in_main
sbm = Sub_in_main


file_ext = "txt"
file_ext_2 = 'py'
title_str = "this is an amazing title" 


file_namee = jfilename("This is anamazing title", 'csv')
print(file_namee)

file_name = jfilename(title_str, file_ext)
print(file_name)



y = list(range(10)) + list(reversed(range(10)))
print('y =', y)

y_str = jstring(y)
print('y_str = ',y_str)

zero = sbm(0,y_str)
print('location of 0s in y_str:', zero.jfind())
print('number of 0s in y_str:  ', zero.jcount())


nine = sbm(9,y_str)
print('location of 9s in y_str:', nine.jfind())
print('number of 9s in y_str:  ', nine.jcount())




