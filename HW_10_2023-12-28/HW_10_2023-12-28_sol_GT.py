# დავალება 10

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს მეათე ლექციაზე, რომელიც ჩატარდა 20231228-ში
# და დავალების ჩაბარების ბოლო ვადაა 20230106.

#******************************************************************#

## სავარჯიშო 1

# დაწერე ფუნქცია, რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას.


# საჭირო ბიბლიოთეკების შემოტანა

import random

# ფუნქციის გამოცხადება

def rand_list_gen(start, end, length):
    random__list = []
    for i in range(length):
        random__list.append(random.randint(start, end))
    return random__list


#------------------------------------------------------------------#

## სავარჯიშო 2

# დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით


# ფუნქციის გამოძახება

# შევქმნათ სია, რომელიც შეიცავს 1 დან 100-მდე შემთხვევით შერჩეულ
# 30 მთელ რიცხვს.

random_list_1_100_30 = rand_list_gen(1, 100, 30) 
print("Original list:", random_list_1_100_30) # დავბეჭდოთ
print("Original list length:", len(random_list_1_100_30)) # შევამოწმოთ სიგრძე

# დავალაგებ Buble Sort-ის გამოყენებით.

# დავწეროთ Buble Sort ფუნქცია

# ფუნქციის გამოცხადება

def buble_sort(input_list):
    max_index = len(input_list) - 1
    sorted_flag = False # როცა დალაგდება გახდება True

    while not sorted_flag:
        sorted_flag = True
        for i in range(max_index):
            if input_list[i] > input_list[i+1]:
                sorted_flag = False
                input_list[i], input_list[i+1] = \
                    input_list[i+1], input_list[i]
    
    return input_list

# დაიბეჭდება დალაგებული სია
print("Buble sorted list:", buble_sort(random_list_1_100_30))


#------------------------------------------------------------------#

## სავარჯიშო 3

# დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე
# ხაზობრივი და ბინარული ძიება.

# შევქმნათ ხაზობრივი ძიების ფუნქცია

# ფუნქციის გამოცხადება

def linear_search(input_list, element):
    for i in range(len(input_list)):
        if input_list[i] == element:
            print(f"Linear Search: Index of {element} is {i}!") 
            return i
        
    return print(f"Linear Search: {element} is not in the list!")

# შევქმნათ ბინარული ძიების ფუნქცია

# ფუნქციის გამოცხადება

def binary_search(input_list, element):
    low, high = 0, len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]

        if mid_value == element:
            print(f"Binary Search: Index of {element} is {mid}!")
            return mid
        elif mid_value < element:
            low = mid + 1
        else:
            high = mid - 1

    return print(f"Binary Search: {element} is not in the list!")


# ჩვენს მიერ ზემოთ შექმნილ სიაში მოვძებნოთ 1 ხაზობრივად

# ფუნქციის გამოძახება

linear_search(random_list_1_100_30, element=1)

# ჩვენს მიერ ზემოთ შექმნილ სიაში მოვძებნოთ 1 ბინარულად

# ფუნქციის გამოძახება

binary_search(random_list_1_100_30, element=1)


#------------------------------------------------------------------#

## სავარჯიშო 4

# დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო 
# (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას 
# მცირე, საშუალო და გრძელი სიის შემთხვევებში.

# შევქმნათ მცირე, საშუალო დ გრძელი სია

# მცირე სია, შეიცავს 1000 ელემენტს

random_list_short = rand_list_gen(1, 1000, 1000)
print("Original short list", random_list_short, "\n")

# საშუალო სია, შეიცავს 2000 ელემენტს

random_list_medium = rand_list_gen(1, 2000, 2000)
print("Original medium list", random_list_medium, "\n")

# გრძელი სია, შეიცავს 3000 ელემენტს.

random_list_long = rand_list_gen(1, 3000, 3000)
print("Original long list", random_list_long, "\n")

# დავახარისხოთ თითოეული სია

print("Buble sorted short list:", "\n", 
      buble_sort(random_list_short), "\n")
print("Buble sorted medium list:", "\n",
      buble_sort(random_list_medium), "\n")
print("Buble sorted long list:", "\n",
      buble_sort(random_list_long), "\n")


# შევქმნათ დეკორატორი დროის გამოსათვლელად

# საჭირო მოდულის შემოტანა

import time

# დროის დეკორატორის გამოცხადება

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds to execute.")
        return result

    return wrapper

# ხაზობრივი მეთოდით საპოვნელად საჭირო დრო მცირე სიისთვის

@timing_decorator
def linear_search(input_list, element):
    for i in range(len(input_list)):
        if input_list[i] == element:
            print(f"Linear Search: Index of {element} is {i}!") 
            return i
        
    return print(f"Linear Search: {element} is not in the list!")


linear_search(random_list_short, element=1)

# ბინარული მეთოდით საპოვნელად საჭირო დრო მცირე სიისთვის

@timing_decorator
def binary_search(input_list, element):
    low, high = 0, len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]

        if mid_value == element:
            print(f"Binary Search: Index of {element} is {mid}!")
            return mid
        elif mid_value < element:
            low = mid + 1
        else:
            high = mid - 1

    return print(f"Binary Search: {element} is not in the list!")

binary_search(random_list_short, element=1)

# დროში სხვაობა უმცირესია. რამდენჯერად ვცადე ბინარული სჯობს!
# ზუსტად, რომ შევადარო ალბათ ბერჯერ უნდა გავაკეთო ეს შედარების
# იტერაციები, მერე გამოვთვალოთ საშუალო დრო თითოეულისთვის და 
# იმის მხიედვით გადავწყვითოთ რომელი სჯობს. ეს ცხადია მარტივი 
# გასაკეთებელია უბრალოდ დედლაინამდე დრო აღარ მყოფნის ამის 
# დასაწერად.


# ხაზობრივი მეთოდით საპოვნელად საჭირო დრო საშუალო სიისთვის

@timing_decorator
def linear_search(input_list, element):
    for i in range(len(input_list)):
        if input_list[i] == element:
            print(f"Linear Search: Index of {element} is {i}!") 
            return i
        
    return print(f"Linear Search: {element} is not in the list!")


linear_search(random_list_medium, element=1)

# ბინარული მეთოდით საპოვნელად საჭირო დრო საშუალო სიისთვის

@timing_decorator
def binary_search(input_list, element):
    low, high = 0, len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]

        if mid_value == element:
            print(f"Binary Search: Index of {element} is {mid}!")
            return mid
        elif mid_value < element:
            low = mid + 1
        else:
            high = mid - 1

    return print(f"Binary Search: {element} is not in the list!")

binary_search(random_list_medium, element=1)


# აქ დროში სხვაობა ცოტათი გაიზარდა. 
# რამდენჯერად ვცადე აქაც ბინარული სჯობს!
# ზუსტი გიანოზისთვის აქაც ბევრი ცდა იქნება საჭირო, რაც გაკეთებადია,
# მაგრამ გასაწერად დროა რ მყოფნის.


# ხაზობრივი მეთოდით საპოვნელად საჭირო დრო გრძელი სიისთვის

@timing_decorator
def linear_search(input_list, element):
    for i in range(len(input_list)):
        if input_list[i] == element:
            print(f"Linear Search: Index of {element} is {i}!") 
            return i
        
    return print(f"Linear Search: {element} is not in the list!")


linear_search(random_list_long, element=1)

# ბინარული მეთოდით საპოვნელად საჭირო დრო გრძელი სიისთვის

@timing_decorator
def binary_search(input_list, element):
    low, high = 0, len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]

        if mid_value == element:
            print(f"Binary Search: Index of {element} is {mid}!")
            return mid
        elif mid_value < element:
            low = mid + 1
        else:
            high = mid - 1

    return print(f"Binary Search: {element} is not in the list!")

binary_search(random_list_long, element=1)

# აქაც ბინარული სჯობს. 
# ზუსტი დიაგნოზზისთვის საჭიროა მეტი იტერაცია.


#------------------------------------------------------------------#

# შევნიშნოთ, რომ ზოგჯერ ნაპოვნი ელემენტის იდნექსი ხაზობრივი და
# ბინარული ძებნის შემთხვევაში ერთმანეთისგან განსხვავედება. ეს ხდება
# ვინაიდან ხაზობრივი ძიება ყოველთვის აბრუნებს საძიებელი ელემენტის
# პირველ შემხვედრ მდებარეობას, ხოლო ბინარული კი ზოგჯერ პირველს
# აბრუნებს ზოგჯერ ბოლოს და ზოგჯერ შუას. ასე ხდება, ვინაიდან
# ბინარული ძიებისთვის მთავარია იპოვოს ელემენტი და ამას აკეთებს
# სიის შუაზე დაყოფით იმდენჯერ რამდენჯერაც საჭიროა, ხოლო 
# ხაზობრივი ძიება კი მიყვება თავიდან და როგორც კი იპოვის ელემენტს
#  მაშინვე აბრუნებს იდნექსს. 

# მაგალითად, თუ საძიებელი სიაა
# list_a = [1, 1, 1, 3, 4] ხაზოვრივი ძიება იპოვის 1 იანს, რომელიც
#  დგას 0 ინდექსზე, ხოლო ბინარული იპოვის ერთიანს, რომელიც დგას 2
# ინდექსზე. ამ შემთხვევაში, ორივეს ერთი იტერაცია დასჭირდება.

list_a = [1, 1, 1, 3, 4]

def linear_search(input_list, element):
    for i in range(len(input_list)):
        if input_list[i] == element:
            print(f"Linear Search: Index of {element} is {i}!") 
            return i
        
    return print(f"Linear Search: {element} is not in the list!")

linear_search(list_a, element=1)

def binary_search(input_list, element):
    low, high = 0, len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]

        if mid_value == element:
            print(f"Binary Search: Index of {element} is {mid}!")
            return mid
        elif mid_value < element:
            low = mid + 1
        else:
            high = mid - 1

    return print(f"Binary Search: {element} is not in the list!")

binary_search(list_a, element=1)


# მაგალითად, თუ საძიებელი სიაა
# list_a = [1, 1, 4, 3, 4] ხაზოვრივი ძიება იპოვის 1 იანს, რომელიც
#  დგას 0 ინდექსზე, ხოლო ბინარული იპოვის ერთიანს, რომელიც დგას 0
# ინდექსზე. ამ შემთხვევაში, ხაზობრივს დასჭირდება 1 იტერაცია, ხოლო
# ბინარულს 2.

list_a = [1, 1, 4, 3, 4]

def linear_search(input_list, element):
    for i in range(len(input_list)):
        if input_list[i] == element:
            print(f"Linear Search: Index of {element} is {i}!") 
            return i
        
    return print(f"Linear Search: {element} is not in the list!")

linear_search(list_a, element=1)

def binary_search(input_list, element):
    low, high = 0, len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]

        if mid_value == element:
            print(f"Binary Search: Index of {element} is {mid}!")
            return mid
        elif mid_value < element:
            low = mid + 1
        else:
            high = mid - 1

    return print(f"Binary Search: {element} is not in the list!")

binary_search(list_a, element=1)


#------------------------------------------------------------------#