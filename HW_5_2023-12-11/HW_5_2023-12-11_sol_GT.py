# დავალება 5

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს მეხუთე ლექციაზე, რომელიც ჩატარდა 20231211-ში
# და დავალების ჩაბარების ბოლო ვადაა 20231218.


## სავარჯიშო 1

# ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის,
# გვარის და ასაკის შესახებ. თითოეული მომხმარებლის ინფორმაცია შეინახე
# ინდივიდუალურ სიაში. შემდეგ კი სამივე სია დაამატე საერთო ცარიელ სიას
# სახელად consumer_info. Input_ის მეშვეობით მომხმარებლის ინდექსის 
# შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე 
# ინფორმაცია შემდეგნაირად:

# Name: Elene
# Lastname: Khardava
# Age: 21

consumer_info = [] # აქ ინახავს ინფორმაციას სამივე მომხმარებლის შესახებ.

for i in range(3):

    consumer = [] # დროებითი სია თითოეული მომხმარებლის ინდივიდუალური
    # ინფორმაციის შესანახად.
    consumer.append(input("Enter Your Name: "))
    consumer.append(input("Enter Your Lastname: "))
    consumer.append(input("Enter Your Age: "))
    consumer_info.append(consumer)

# აქ დავუშვი, რომ ამოცანის ავტორი გულისხმობდა, რომ პროგრამა
# აგრძელემბს მუშაობას და ითხოვს მომხმარებლის ინდექსის შეყვანას, შემდეგ კი
# ააბრუნებს ინფორმაციას ამოცანაში მოყვანილი ფორმით.

consumer_index =  int(input("Enter Consumer Index from 0 to 2: "))

# ეს სამივე ბრზანება შეგვეძლო ერთში გაგვეერთინებინა და ეს ნაჩვენები
# მაქვს მესამე სავარჯიშოში.

print(f"Name: {consumer_info[consumer_index][0]}")
print(f"Lastname: {consumer_info[consumer_index][1]}")
print(f"Age: {consumer_info[consumer_index][2]}")


## სავარჯიშო 2

# მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე
# თუ სახელის ველი არ იქნება ცარიელი,
# ხოლო პაროლი 8 სიმბოლოზე მეტი ან ტოლია. 
# მისი მონაცემები შეინახე ლისთში. 
# შემდეგ მიეცი საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე 
# მის მიერ შემოყვანილი ინფორმაცია სიაში შენახულ ინფორმაციას. 
# დაბეჭდე შესაბამისი მესიჯი.

# პლატფორმაზე რეგისტრაცია

# აქ დავამატე პატარა ფუნქციონალი. კერძოდ, სანამ username-ის და password-ის
# მოთხოვნები არ დაკმაყოფილდება მომხმარებელი ვერ გასცდება რეგისტრაციის 
# პროცესს, ისე როგორც ამას რეალური ვებ გვერდები აკეთებენ. თუ თავის დანებება 
# ენდომება შეიყვანს საკვანძო სიტყვას "exit"და პროგრამა დაასრულებს მუშაობას.

print("To register on the platform set username and password.\n"
      "Username must be non-empty and password must be of at least 8 charachters.\n"
      "If you no longer want to register enter \"exit\" for username or password "
      "and platform will shut down.")

while True:
    
    username = input("Enter Your Username (must be non-empty): ")

    if username == "exit":
        exit()

    password = input("Enter Your Password (must be at least 8 chars): ")

    if password == "exit":
        exit()

    if len(username) > 0 and len(password) >= 8:

        database = [username, password]
        print("Registration completed successfully!")
        break    

# პლატფორმაზე შესვლა

# აქაც დავამატე პატარა ფუნქციონალი. კერძოდ, დავუმატე შეზღუდვა, რომ 
# მომხმარებელმა საიტზე შესვლა შეიძლება სცადოს მხოლოდ 3 ჯერ. 
# მესამედ არასწორად შეყვანილი ინფორმაციის შემთხვევაში მომხმარებელი იბლოკება 
# და იწერება შესაბამისი ტექსტი. 

number_of_log_attempts = 3 # ეს განსაზღვრავს საიტზე შესვლის მცდელობების რაოდენობას.
i = 0

while i < number_of_log_attempts:
    
    username_log = input("Enter Your Username: ")
    password_log = input("Enter Your Password: ")

    i += 1
    
    if username_log == database[0] and password_log == database[1]:
    
        print("You are logged in!")
        break
    
    else:
    
        print(f"Username or Password is wrong. Try again (attempts left: {number_of_log_attempts - i}): ")

else: 

    print(f"Your have attempted to login {number_of_log_attempts} times. Try again later!")


## სავარჯიშო 3 

# შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი 
# მსახიობების შესახებ ინფორმაცია. მომხმარებელს შემოჰყავს მსახიობის სახელი
#  ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდა მის შესახებ
#  არსებული ინფორმაცია რეზუმის სახით.

# ამ შემთხვევაში მნიშვნლოვანია მომარებელმა დიდი ასეთი შეიყვანოს სახელი ან გვარი.
# ვინაიდან პროგრამა ამის მიმართ მგრძნობიარეა. შეგვეძლო დაგვეწერა, რომ 
# არ მიექცია ყურადღება ასოების სიდიდისთვის და უბრალოდ რაც დამეთხვეოდა ის
# ამოეგდო. მაგრამ ვინაიდან საქმე ეხება სახელს და გვარს ორივე უნდა 
# დაიწყოს დიდი ასოთი.


TC = ["Tom", "Cruise", "1962 July 3", "1.7m" ]
KH = ["Katie", "Holmes", "1978 December 3", "1.78m" ]
SC = ["Suri", "Samsone", "1998 January 3", "1.9m" ]
NK = ["Nicole", "Kidman", "1958 January 10", "1.67m" ]

database = [TC, KH, SC, NK]

firstname_or_lastname = input("Enter First or Last Name (must start with capital letter): ")

for act in database:
    if firstname_or_lastname in act:
        print(f"Name: {act[0]}\nLastname: {act[1]}\n"
              f"Date of Birth: {act[2]}\nHeight: {act[3]}")
        break
else:
    print("No match found!")