immutable_var = 2.9, 8, True, "Orang"
print(immutable_var)
print(immutable_var[3])
#immutable_var[3] = False #кортеж не поддерживает пбращение по элементам
immutable_var_1 = (2.9, 8, [True, "Orang"])
print(immutable_var_1)
immutable_var_1[-1] [-1] = "red"
print(immutable_var_1)

multitable_list = ["red", "orange", "yellow", "green", "light", "blue", "purple"]
print(multitable_list)
multitable_list[0] = "apple"
multitable_list[2] = "lemon"
multitable_list[4] = "blackberry"
multitable_list[6] = "plum"
print(multitable_list)