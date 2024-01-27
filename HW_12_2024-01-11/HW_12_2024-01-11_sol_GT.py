# დავალება 12

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს მეთორმეტე ლექციაზე, რომელიც ჩატარდა 
# 2024-01-11-ში და დავალების ჩაბარების ბოლო ვადაა 2024-01-18.

#******************************************************************#

print("\n",
      "-------------------- სავარჯიშო 1 --------------------", "\n")

## სავარჯიშო 1

# დაწერე ფუნქცია, რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და
# ყველა უნიკალური value_ს მქონე ელემენტს დააბრუნებს.

# ფუნქციის გამოცხადება

def dict_filter(input_dict):
    value_filter = set()
    result_dict = {}

    for key, value in input_dict.items():
        if value not in value_filter:
            value_filter.add(value)
            result_dict[key] = value  
    
    return result_dict

# ფუნქციის გამოძახება

dict_w_duplictes = {
    "Name": "Noe",
    "Last Name": "Noe",
    "Age": 30,
    "Height": 30,
    "Wage": 100
}

print(dict_w_duplictes)
dict_unique = dict_filter(dict_w_duplictes)
print(dict_unique)


#------------------------------------------------------------------#

print("\n",
      "-------------------- სავარჯიშო 2 --------------------", "\n")

## სავარჯიშო 2

# დაწერე ფუნქცია, რომელიც შეამოწმებს გადაცემული ლექსიკონი
# ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.

# ფუნქციის გამოცხადება

def check_empty_dict(input_dict):

    if len(input_dict) == 0:
        print(f"{input_dict} is empty!")
    else:
        print(f"{input_dict} is NOT empty!")

# ფუნქციის გამოძახება

non_empty_dict = {
    "a": 1,
    "b": 2
    }

empty_dict = {}

check_empty_dict(non_empty_dict)

check_empty_dict(empty_dict)


#------------------------------------------------------------------#

print("\n",
      "-------------------- სავარჯიშო 3 --------------------", "\n")

## სავარჯიშო 3

# დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს 
# შექმნის და დააბრუნებს. ვთქვათ გადავეცით ფუნქციას სტრიქონი,
# უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა 
# value_ს ადგილას. მაგალითად, გადავეცით სტრიქონი : 'racoon'
# უნდა დააბრუნოს ლექსიკონი:
# {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}

# აქ ორი ვარიანტი დავწერე პირველი იყნებს 2 ლუპს, ხოლო მეორე 
# get() მეთოდს. მერე ვარიანტი უფრო ჯობია სავარაუდოდ. უფრო
# ელეგანტურია და დიდი ალბათობით უფრო სწრაფიც იქნება

# ფუნქციის გამოცხადება

def char_count(input_str):
    result_dict = {}

    for char_0 in input_str:
        char_count = 0
        for char_1 in input_str:
            if char_1 == char_0:
                char_count += 1
        result_dict[char_0] = char_count
    
    return result_dict

# ფუნქციის გამოძახება

test_str_1 = "racoon"

result = char_count(test_str_1)

print(result)

test_str_2 = "bamboo and racoon"

result = char_count(test_str_2)

print(result)

# ფუნქციის გამოცხადება

def count_characters(input_str):
    result_dict = {}
    
    for char in input_str:
        result_dict[char] = result_dict.get(char, 0) + 1

    return result_dict

# ფუნქციის გამოძახება

test_str_1 = "racoon"

result = char_count(test_str_1)

print(result)

test_str_2 = "bamboo and racoon"

result = char_count(test_str_2)

print(result)


#------------------------------------------------------------------#