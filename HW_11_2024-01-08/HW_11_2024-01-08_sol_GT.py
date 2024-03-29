# დავალება 11

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს მეთერთმეტე ლექციაზე, რომელიც ჩატარდა 
# 2024-01-08-ში და დავალების ჩაბარების ბოლო ვადაა 2024-01-15.

#******************************************************************#

print("-------------------- სავარჯიშო 1 --------------------", "\n")

## სავარჯიშო 1

# შექმენი ფუნქცია, რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, 
# თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).

# ფუნქციის გამოცხადება

def unique_list(input_list):
    input_set = set(input_list)  # უნიკალური ელემენტების ამორჩევა
    input_list = list(input_set)  # სიმრავლის სიად გადაქცევა
    return input_list

# ფუნქციის გამოძახება

list_a = [1, 2, 14, 10, 40, 10, 2, 44, 10]
print(list_a, "\n")
list_a_unique = unique_list(list_a)  # უნიკალური სია
print(list_a_unique, "\n")
print(type(list_a_unique), "\n")


#------------------------------------------------------------------#

print("-------------------- სავარჯიშო 2 --------------------", "\n")

## სავარჯიშო 2

# შექმენი ფუნქცია, რომელიც მიიღებს სიას და დააბრუნებს ასევე set
# ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც 
# შეუძლებელი იქნება (გამოიყენე frozenset).

# ფუნქციის გამოცხადება

def immutable_set(input_list):
    input_fz_set = frozenset(input_list)
    return input_fz_set

# ფუნქციის გამოძახება

list_a = [1, 2, 14, 10, 40, 10, 2, 44, 10]
print(list_a, "\n")
frozen_set = immutable_set(list_a)  # უნიკალური სია
print(frozen_set, "\n")
print(type(frozen_set), "\n")


#------------------------------------------------------------------#

print("-------------------- სავარჯიშო 3 --------------------", "\n")

## სავარჯიშო 3

# შექმენი ფუნქცია, რომელიც მიიღებს ორ set ტიპის მონაცემს, 
# გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და
# დააბრუნებს შედეგს.

# ფუნქციის გამოცხადება

def set_to_tuple(input_set_1, input_set_2):
    input_set_union = input_set_1.union(input_set_2)
    input_tuple = tuple(input_set_union)
    return input_tuple

# ფუნქციის გამოძახება

set_1 = {1, 1, 2, 5}
set_2 = {1, 1, 2, 12, 14}
print(set_1)
print(set_2)
return_tuple = set_to_tuple(set_1, set_2)
print(return_tuple)
print(type(return_tuple))


#------------------------------------------------------------------#