# დავალება 4

# შემსრულებელი: გიორგი ცუცირიძე

# ეს დავალება მოგვცეს მეოთხე ლექციაზე, რომელიც ჩატარდა 20231207-ში
# და დავალების ჩაბარების ბოლო ვადაა 20231214.


## სავარჯიშო 1

# მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე რამდენი რიცხვი,
# ანბანის ასო და სხვა სიმბოლოა მოცემული წინადადებაში. შედეგი დაბეჭდე.
# გამოიყენე for ციკლი, isalpha და isdigit ფუნქციები. 

sentence = input("Enter your sentence : ") # მომხმარებელს შეჰყავს წინდადება ტერმინალიდან
# შეყვანილ წინდადებას პროგრამა იმახსოვრებს sentence ცვლადში

number_of_digits = 0 # წინადადებაში რიცხვების რაოდენობის მთვლელი
number_of_letters = 0 # წინადადებაში ანბანის ასოების რაოდენობის მთვლელი
number_of_other_chars = 0 # წინადადებაში სხვა დანარჩენი სიმბოლოების რაოდენობის მთვლელი

for char in sentence:

    if char.isdigit():
    
        number_of_digits += 1
    
    elif char.isalpha():
    
        number_of_letters += 1
    
    else:

        number_of_other_chars += 1

print("Number of digits = ", number_of_digits)
print("Number of letters = ", number_of_letters)
print("Number of other characters = ", number_of_other_chars)


## სავარჯიშო 2

# მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე
# შემდეგ წესებზე დაყრდნობით. შექმნილი წინადადება უნდა იწყებოდეს
# პირველი წინადადების პირველი სიმბოლოთი, რომელსაც ჯერ მოჰყვება
# მეორე წინადადების ბოლო სიმბოლო, შემდეგ კი პირველი წინადადების
# მეორე სიმბოლო და მეორე წინადადების ბოლოდან მეორე სიმბოლო.

# ეს პირობა გავიგე ორნაირად. 

# პირველ შემთხვევაში გვექნება მხოლოდ 4 სიმბოლოიანი
# წინადადება იმ თანმიმდევრობით როგორც აღწერილია პირობაში. 
# იხილეთ ქვემოთ:

print("Enter any two setences below, each after the corresponding call.")
sentence_1 = input("Enter the first sentence: ")
sentence_2 = input("Enter the second sentence: ")

new_sentence = sentence_1[0] + sentence_2[-1] + \
                sentence_1[1] + sentence_2[-2]

print(new_sentence)

# მეორე შემთხვევაში კი გვექნება სრულად პირველი და მეორე წინადადებებისგან
# შემდგარი ახალი წინადადება, ოღონდ პრველი 4 სიმბოლო იქნება იმ თანმიმდევრობით,
# როგორც აღწერილია პირობაში, ხოლო დანარჩენი სიმბოლოები იქნება ჯერ პირველი
# წინადადებიდან დარჩენილი სიმბოლოები, ხოლო შემდეგ მეორე წინადადებიდან დარჩენილი
# სიმბოლოები თავდაპირველი თანმიმდევრობით.

# იხილეთ ქვემოთ:

print("Enter any two setences below, each after the corresponding call.")
sentence_1 = input("Enter the first sentence: ")
sentence_2 = input("Enter the second sentence: ")

new_sentence = sentence_1[0] + sentence_2[-1] + \
                sentence_1[1] + sentence_2[-2]

for i in range(len(sentence_1)):
    
    if i != 0 and i != 1:
        
        new_sentence +=sentence_1[i]

for i in range(len(sentence_2)):
    
    if i != len(sentence_2)-1 and i != len(sentence_2)-2:
        
        new_sentence +=sentence_2[i]

print(new_sentence)


## სავარჯიშო 3

# მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე, პირველ
# წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორე წინადადებაში
# და პირიქით, მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის
# პირველ წინადადებაში. 
# თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე:
# „Strings are balanced!“
# თუ რომელიმე პირობა დაირღვა, დაბეჭდე:
# „Strings are not balanced!“

# ქვემოთ მოცემულ ამოხსნაში იგულისმება, რომ ცარიელი ადგილი არის სიმბოლო
# და აგრეთვე პატარა და დიდი ასოები არიან ცალ-ცალკე სიმბოლოები. მაგალითად,
# თუ პირველი წინადადებაა "Strings", ხოლო მეორე "strings" დაიბეჭდება: 
# "Strings are not balanced!" 

print("Enter any two setences below, each after the corresponding call.")
sentence_1 = input("Enter the first sentence: ")
sentence_2 = input("Enter the second sentence: ")

Alert_1 = True # თუ საბოლოოდ დარჩა ჭეშმარიტი, მაშინ პირველი წინადადების
    # ყველა სიმბოლო შედის მეორე წინადადებაში.

Alert_2 = True # თუ საბოლოოდ დარჩა ჭეშმარიტი, მაშინ მეორე წინადადების
    # ყველა სიმბოლო შედის პირველ წინადადებაში.

for char in sentence_1:

    if char not in sentence_2:

        Alert_1 = False
        break

for char in sentence_2:

    if char not in sentence_1:

        Alert_2 = False
        break

if Alert_1 and Alert_2:

    print("Strings are balanced!")

else:

    print("Strings are not balanced!")

# გაითვალისწინეთ, რომ ზემოთ მოცემული პროგრამა არ ამოწმებს ორი წინადადების 
# იდენტურობას. მაგალითად, "I am Giorgi" და "I am GGGGGGGiorgi i" 
# არ არის იდენტური, თუმცა ეს პროგრამა დაწერს რომ "Strings are ssbalanced!".