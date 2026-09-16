my_list = [1, 2, 3]
print(my_list)

my_list[0]=100
print(my_list)
#список, он изменяемый

my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple[0]=100
print(my_tuple)
#кортеж - неизменяемый вид данных,выдает ошибку
my_string = "cat"
print(my_string)
my_string[0]="b"
print(my_string)
#выдает ошибку,строчку нельзя менять
