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
