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

