# დავალება 9

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს მეცხრე ლექციაზე, რომელიც ჩატარდა 20231225-ში
# და დავალების ჩაბარების ბოლო ვადაა 20240101.

#******************************************************************#

## სავარჯიშო 1

# დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort()
# მეთოდის გამოყენებით (ზრდადობით).


# საჭირო ბიბლიოთეკების შემოტანა

import random

# 10 ელემენტიაანი შემთხვევითი სიის დაგენერირება

my_nums = [random.randint(1, 100) for i in range(10)]

print("Original list:", my_nums, "\n")

# სიის დახარისხება ზრდადობით

my_nums.sort()

print("Sorted list:", my_nums, "\n")


#------------------------------------------------------------------#

## სავარჯიშო 2

# დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted()
# ფუნქციის გამოყენებით (კლებადობით).


# საჭირო ბიბლიოთეკების შემოტანა

import random

# 10 ელემენტიაანი შემთხვევითი სიის დაგენერირება

my_nums = [random.randint(1, 100) for i in range(10)]

print("Original list:", my_nums, "\n")

# სიის დახარისხება ზრდადობით

my_nums_sorted = sorted(my_nums, reverse=True)

print("Sorted list:", my_nums_sorted, "\n")

#------------------------------------------------------------------#

## სავარჯიშო 3

# დაწერე პროგრამა, რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას 
# და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით 
# (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის 
# სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია
# მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და 
# გრძელი(3000 ელემენტი) სიის შემთხვევებში.


# რამდენჯერმე ვცადე დახარისხება ორივე ალგორითმით და ხან ერთი
# უფრო ეფექტური აღმოჩნდა ხან მეორე. ამიტომ გადავწყვიტე თითოეული
# ზომის სიისათვის 1000 ჯერ გამემეორებინა დახარისხება და გამომეთვალა 
# დახარისხების საშუალო დრო თითოეული ალგორითმისთვის და 
# ამის საფუძველზე მეთქვა რომელი უფრო ეფექტურია. თითოეულ
# გამეორებაზე ორივე ალგორითმი ახარისხებს ერთსა და იმავე 
# შემთხვევით სიას.
  
# საჭირო ბიბლიოთეკების შემოტანა

import time
import random

# Buble Sort ალგორითმი

def buble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n):
        swapped = True
        for j in range(n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = \
                    sorted_arr[j+1], sorted_arr[j]
                swapped = False
        
        if swapped:
            break

    return sorted_arr

# Selection Sort ალგორითმი

def selection_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j

        if i != min_index:
            sorted_arr[i], sorted_arr[min_index] = \
                sorted_arr[min_index], sorted_arr[i]
    
    return sorted_arr

# დახარისხების ალგორითმებისთვის საჭირო დროის შედარების ფუნქცია

def avg_time_comp(algorithm_1, algorithm_2, arr_length=1000, rep=100):
    sort_time_list_1 = []
    sort_time_list_2 = []
    
    for i in range(rep):
        my_nums = [random.randint(1, arr_length) 
                         for i in range(arr_length)]
        start = time.time()
        algorithm_1(my_nums)
        end = time.time()
        sort_time_list_1.append(end - start)

        start = time.time()
        algorithm_2(my_nums)
        end = time.time()
        sort_time_list_2.append(end - start)
    
    avg_time_1 = sum(sort_time_list_1)/rep
    avg_time_2 = sum(sort_time_list_2)/rep

    print(f"List Length: {arr_length},", 
      f"{algorithm_1.__name__}:", avg_time_1)
    
    print(f"List Length: {arr_length},",
      f"{algorithm_2.__name__}:", avg_time_2)
    
    if avg_time_1 > avg_time_2:

        print(f"List Length: {arr_length},",
        f"{algorithm_1.__name__} is {avg_time_1/avg_time_2}",
        f"slower than {algorithm_2.__name__}:",
        )
        print(f"{algorithm_2.__name__} IS MORE EFFICIENT!")

    elif avg_time_1 < avg_time_2:
        
        print(f"List Length: {arr_length},",
        f"{algorithm_2.__name__} is {avg_time_2/avg_time_1}",
        f"slower than {algorithm_1.__name__}:",
        )
        print(f"{algorithm_1.__name__} IS MORE EFFICIENT!")
    
    else:
    
        print("BOTH ALGORITHMS ARE EQUALLY EFFICIENT!")
        
    print("Done!\n")


# მცირე სია

list_length = 1000

avg_time_comp(buble_sort, selection_sort, list_length)

# Selection Sort უფრო ეფექტურია

# საშუალო სია

list_length = 2000

avg_time_comp(buble_sort, selection_sort, list_length)

# Selection Sort უფრო ეფექტურია

# გრძელი სია

list_length = 3000

avg_time_comp(buble_sort, selection_sort, list_length)

# Selection Sort უფრო ეფექტურია

#------------------------------------------------------------------#