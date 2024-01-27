# დავალება 13

# შემსრულებელი: გიორგი ცუცქირიძე

# ბიბლიოთეკების შემოტანა

import os

## სავარჯიშო 1

# დაწერე ფუნქცია, რომელიც მომხმარებელს ტექსტურ ფაილში ინფორმაციას
# ჩააწერინებს Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი 
# არ შეიყვანს სიტყვას _ “enough”.

# ფუნქციის გამოცხადება

def text_to_file():
    
    while True:
        input_str = input("Enter Information (Enter \"Enoguh\" if "
          "you want to stop entering information): "
           )
        if input_str.lower() == "enough":
            break
        else:
           with open("client_generated_info.txt", "a") as file:
               file.write(input_str + "\n")

# ფუნქციის გამოძახება

text_to_file()

# შევამოწმოთ ჩაწერა თუ არა ყველაფერი ფაილში.

with open("Client_generated_info.txt", "r") as file:
   print(file.read())


## სავარჯიშო 2
   
# დაწერე ფუნქცია, რომელიც input ფუნქციის დახმარებით
# მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი 
# ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს
# და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

# ფუნქციის გამოცხადება

def main_func():
    folder_path = input("Enter folder path: ")
    file_name = input("Enter file name with extension "
                      "(e.g. textfile.txt): ")
    try:
        with open(f"{folder_path}\{file_name}", "x") as file:
            pass
    except FileExistsError:
        print("File already exists!")
    
    for f in os.listdir(folder_path):
        print(f)


# ფუნქციის გამოძახება

main_func()
    