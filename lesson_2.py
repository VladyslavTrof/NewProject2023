#box_number_1 = 1 #snake case

#a = 1
#b = 2
#c = a + b


#months_in_year =12 #

#value_str

#value_1 = "2"
#value_2 = "4"
#result = value_1 + value_2
#print(result)

number = int(input("Eneter any four digits"))

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10

print(thousands)
print(hundreds)
print(tens)
print(ones)