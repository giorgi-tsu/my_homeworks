# დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted()
# ფუნქციის გამოყენებით (კლებადობით).


# საჭირო ბიბლიოთეკების შემოტანა
import random

# 10 ელემენტიაანი შემთხვევითი სიის დაგენერირება

my_nums = [random.randint(1, 100) for i in range(10)]

print("Original list:", my_nums)

# სიის დახარისხება ზრდადობით

my_nums_sorted = sorted(my_nums, reverse=True)

print("Sorted list:", my_nums_sorted)