# დავალება 8

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს მერვე ლექციაზე, რომელიც ჩატარდა 20231221-ში
# და დავალების ჩაბარების ბოლო ვადაა 20231228.

#******************************************************************#

## სავარჯიშო 1

# დაწერე პროგრამა, რომელიც გადაამრავლებს სიის ყველა წევრს
# კონკრეტულ რიცხვზე ლამბდას გამოყენებით.

# აქ ვუშვებ, რომ ეს კონკრეტული რიცხვი ტოლია 5-ის, უკვე გაწერილია
# ლამბდა ფუნქციაში და არ იცვლება.

# თავდაპირველი სია

numbers = [1, 2, 6, -5]

# 5 ზე გამრავლებული სია

numbers_by_5 = list(map(lambda n: n * 5, numbers))
print("Original List:", numbers, "\nFinal List:", numbers_by_5)

# შეგვიძლია ეს ყველაფერი შევფუთოთ ფუნქციაში და ამავე დროს,
# რიცხვი რომელზეც სიას ვამრავლებთ სიასთან ერთად მივაწოდოთ 
# ფუნქციას როგორც არგუმენტი

# ფუნქციის გამოცხადება

# თუ არ მივაწოდებთ იმ რიცხვს, რაზეც სიის გამრავლება გვინდა
# დაგვიბრუნებს იგივე სიას

def mul_by_number(numbers, n=1):
    numbers_by_n = list(map(lambda m: m*n, numbers))
    return numbers_by_n

# ფუნქციის გამოძახება

numbers = [1,7,-5]

result = mul_by_number(numbers, n=0)

print("Original List:", numbers, "\nFinal List:", result)
 
#------------------------------------------------------------------#

## სავარჯიშო 2

# დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის
# სიგრძეს დააბრუნებს, მას შემდეგ, რაც წაშლის სიიდან ყველა
# სახელს, რომელიც პატარა სიმბოლოთი იწყება.
# (გამოიყენე .isupper() მეთოდი)

# ჩავამატე და პროგრამა სიგრძესთან ერთად ბეჭდავს გაფილტრულ სიასაც

names = ["Peter", "john", "Zaur", "jack"]

names_upper = list(filter(lambda name: name[0].isupper(), names))
names_upper_length = len(names_upper)
print("Filtered list:", names_upper)
print("Length of filered list:", names_upper_length)

# შეგვეძლო არც დაგვებრუნებინა გაფილტრული სია და პირდაპირ სიის
# სიგრძე დაგვებრუნებინა.

names_upper_length_1 = len(list(filter(lambda name: \
                                       name[0].isupper(), names)))

print("Length of filered list:", names_upper_length_1)

# შეგვიძლია ეს პროგრამა შევფუთოთ ფუნქციაში, რომლის არგუმენტია
# სახელების სია, ხოლო მნიშვნელობა კი არის ლექსიკონი, რომელიც
# შეიცავს სიას მხოლოდ იმ სახელებით, რომელიც დიდი ასოთი იწყება
# და ამ სიის სიგრძეს.

# ფუნქციის გამოძახება

def cap_names(names):
    
    names_upper = list(
        filter(lambda name: name[0].isupper(), names)
        )
    names_upper_length = len(names_upper)

    result_dict = {
        "good names": names_upper,
        "number of good names": 
        names_upper_length
    }

    return result_dict

# ფუნქციის გამოძახება

names = ["Peter", "john", "Zaur", "jack"]

result = cap_names(names)

print("Names starting with capital chars:", 
      result["good names"])
print("Numbers of names starting with captal chars:",
       result["number of good names"])

#------------------------------------------------------------------#

## სავარჯიშო 3

# დაწერე პროგრამა, რომელიც დააჯამებს სიაში არსებულ დადებით და
# უარყოფით რიცხვებს ცალ-ცალკე. გამოიყენე ლამბდა ფუნქცია და filter.

numbers = [1, -2, -3, 7]

sum_of_positives = sum(
    filter(lambda n: True if n > 0 else False, numbers)
    )

sum_of_negatives = sum(
    filter(lambda n: True if n < 0 else False, numbers)
    )

print("Sum of positive numbers:", sum_of_positives)

print("Sum of negative numbers:", sum_of_negatives)

# ეს პროგრამა შეიძლება შეიფუთოს ფუნქციაში, რომლის არგუმენტია
# რიცხვთა სია, ხოლო მნიშვნელობა კი არის ლექსიკონი, რომელიც
# შეიცავს დადებითი და უარყოფითი რიცხვების ჯამებს.

# ფუნქციის გამოცხადება

def sum_pos_neg(numbers):

    sum_of_positives = sum(
    filter(lambda n: True if n > 0 else False, numbers)
    )

    sum_of_negatives = sum(
        filter(lambda n: True if n < 0 else False, numbers)
        )

    dict_out = {
        "Sum of positives": sum_of_positives,
        "Sum of negatives": sum_of_negatives
    }

    return dict_out

# ფუნქციის გამოძახება

sum_dict = sum_pos_neg([1, -2, -3, 7])

print("Sum of positive numbers:", sum_dict["Sum of positives"])
print("Sum of negative numbers:", sum_dict["Sum of negatives"])

#------------------------------------------------------------------#

## სავარჯიშო 4

# დაწერე ბანკის ანგარიშის შექმნის, ანგარიშზე თანხის განთავსების და
# შემდგომ ექაუნთში შესვლის პროგრამა, არასწორი ინფორმაციის შეყვანა
# მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.

# რეგისტრაცია

# ამ ლექსიკონში ვინახავთ მომხმარებლის შესახებ ინფორმაციას

user_dict = {}

try_again = True

# მომხმარებელს არ დაარეგისტრირებს მანამ სანამ არ შეიყვანს დასაშვებ
# სიმბოლოებს

while try_again:

    try_again = False

    user_dict["Username"] = input(
        "Please enter your username"
        "(only latin letters and numbers are allowed.\n"
        "Enter \"stop\" to exit the registration process): "
        )

    for char in user_dict["Username"]:
        if not (char.isalpha() or char.isdigit()):
            try_again = True
            break    

if user_dict["Username"] == "stop":
    exit()

try_again = True

while try_again:

    try_again = False

    user_dict["Password"] = input(
        "Please enter your password"
        "(only latin letters and numbers are allowed.\n"
        "Enter \"stop\" to exit the registration process): "
        )

    for char in user_dict["Password"]:
        if not (char.isalpha() or char.isdigit()):
            try_again = True
            break    

if user_dict["Password"] == "stop":
    exit()

# ანგარიშზე თანხის განთავსება
    
# მომხმარებელს შეაყვანინებს მხოლოდ არაუარყოფით რიცხვს. 
# სხვა შემთხვევაში კიდევ და კიდევ ჰკითხავს დეპოზიტის რაოდენობას, 
# მანამ სანამ არაუარყოფით რიცხვს არ შეიყვანს.
    
acc_balance = input("You account has been successfully created!\n"
                    "Please enter the sum that you want to "
                     "deposit (only non-negatie nubmers are "
                     "allowed): "
                     )


while True:

    try:
        acc_balance = float(acc_balance)
        if acc_balance < 0:
            raise ValueError
        break
    except ValueError:
        acc_balance = input("Please enter the sum that you want to "
                        "deposit (only non-negativve nubmers "
                        "are allowed): "
                        )

user_dict["acc_balance"] = acc_balance

# ანგარიშზე შესვლა

# ითვლის ანგარიშზე შესვლის მცდელობების რაოდენობას

counter = 0

while counter < 3:

    username = input("Please enter username: ")
    password = input("Please enter password: ")

    if user_dict["Username"] == username and\
          password == user_dict["Password"]:
        print("You have sucessfully logged in!\n"
              "Your account balance is: ",
              user_dict["acc_balance"], "GEL"
              )
        break
    else:
        counter += 1 

else:

    print("You have entered wrong credentials 3 times. \n"
          "Your account has been blocked!\nContact our " 
          "customer service!")

#------------------------------------------------------------------#