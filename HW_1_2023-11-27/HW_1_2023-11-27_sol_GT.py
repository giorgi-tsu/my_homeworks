# დავალება 1

# შემსრულებელი: გიორგი ცუცირიძე

## ეს დავალება მოგვცეს პირველ ლექციაზე, რომელიც ჩატარდა 20231127-ში
## და დავალების ჩაბარების ბოლო ვადაა 20231204.

## 1. დაწერე პროგრამა, რომელიც გეკითხება ჯერ სახელს, შემდეგ გვარს და ინფორმაციის
## მიღების შემდეგ ტერმინალში ბეჭდავს ერთმანეთის გვერდით. 

name = input("Enter your name: ")
surname = input("Enter your surname: ")
print(name, surname)

## 2. დაწერე პროგრამა რომელიც ითხოვს ორ რიცხვს, პირველი რიცხვი აჰყავს მეორის
## ხარისხში და შედეგი იბეჭდება ტერმინალში

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(num1**num2)

## 3. დაწერე პროგრამა რომელიც გეკითხება სახელს, გვარს, ასაკს და ქალაქს და ბეჭდავს
## ინფორმაციას შემდეგი სახით:

## Name: Lia

## Surname: Kebadze

## Age: 20

## City: Tbilisi

name = input("What is your name? ")
surname = input("What is your surname? ")
age = input("What is your age? ")
city = input("What is the city you live in? ")

# აქ ახალი ხაზიდან დავაწყებინე ბეჭდვა და ბოლოშიც ახალი ცარიელი ხაზი
# დავაბეჭდინე, რომ მაქსიმალურად მიმემსგავსებინა იმ შედეგისთვის, რაც
# დავალებაში გვაქვს მოცემული.

print(f"\nName: {name}\nSurname: {surname}\nAge: {age}\nCity: {city}\n") 

## 4. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ნებისმიერი სამი სხვადასხვა ხილის
## დასახელება ცალცალკე. რეზულტატი კი იბეჭდება შემდეგი სახით:

## Apple//Peach%%Orange

fruit1 = input("Enter the name of fruit 1: ")
fruit2 = input("Enter the name of fruit 2: ")
fruit3 = input("Enter the name of fruit 3: ")

print(f"{fruit1}//{fruit2}%%{fruit3}")

# იგივე შეიძლება გაკეთდეს შემდეგი ბრძანებითაც:

print(fruit1, '//', fruit2, '%%', fruit3, sep='')

# იგივე შეიძლება გაკეთდეს შემდეგი ბრძანებითაც:

print(fruit1+'//'+fruit2+'%%'+fruit3)

## 5. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული
## სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:

## Number of symbols: 5

txt = input("Enter your text here: ")
# txt = txt.replace(" ", "") # Uncomment if you do not want spaces to be counted.

print(f"Number of symbols: {len(txt)}")

# end.