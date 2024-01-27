# დავალება 14

# შემსრულებელი: გიორგი ცუცქირიძე

# ბიბლიოთეკების შემოტანა

import re
import csv

## სავარჯიშო 1

# დაწერე კოდი, რომელიც article.txt _დოკუმენტში იპოვის რიგით
# მეორე ყველაზე ხშირად განმეორებად სიტყვას.


with open(r".\Homeworks\HW_14_2024-01-18\HW_14_2024-01-18_files"
          r"\article.txt", "r") as txt_file:
    txt_file_content_str = txt_file.read()

# ქვემოთ მოცემული ბრძანება ფაილიდან შემოტანილ სტრინგს შლის
# სიტყვებად და მათ ინახავს სიის სახით. სიტყვად კი თვლის ყველა ისეთი
# ანბანურ სიმბოლოს (ლათინური ანბანის ასოები, ციფრები 0-9 და 
# ქვედატირე (_)) თანმიმდევრობას, რომელიც შემოსაზღვრულია
# არაანბანური სიმბოლოებით (ყველა დანარჩენი სიმბოლო ანბანური
# სიმბოლოების გარდა). მაგალითად, "company's" ჩათვლის 2 სიტყვად
# ["company", "s"]. ეს ასეც უნდა იყოს, ვინაიდან ჩვენ თუ გვაქვს
# company და company's, ჩვენ რეალურად ეს სიტყვა 2 ჯერ გვაქვს
# წინადადებაში.
# გარდა ამისა, ქვემოთ მოცემული ბრძანება ანბანური სიმბოლოების
# თანმიმდევრობაში მოქცეულ ტირესაც სიტყვის ნაწილად აღიქვამს. 
# მაგალითად, "Top-Level" და "built-in"-ს ერთ სიტყვად აღიქვამს.
# ესეც წესით ასე უფრო ლოგიკურია.
# გარდა ამისა, სიტყვების ერთმანეთთან შედარებისას დიდ და პატარა 
# ასოებს უგულებელჰყოფს.

txt_file_words_lst = re.findall(r'\b[\w-]+\b', 
                                txt_file_content_str.lower())

word_count_dict = {}
txt_file_words_lst_unique = list(set(txt_file_words_lst))
for word_comp in txt_file_words_lst_unique:
  word_count = 0
  for word in txt_file_words_lst:
    if word == word_comp:
      word_count += 1
  word_count_dict[word_comp] = word_count

word_count_dict_keys_desc = sorted(word_count_dict,
                                   key=word_count_dict.get, 
                                   reverse=True)

word_with_second_max_freq = word_count_dict_keys_desc[1]

print(f"The word \"{word_with_second_max_freq}\" is the second "
      f"most freuqently occuring word in the text and it occurs "
      f"{word_count_dict[word_with_second_max_freq]} times.")


## სავარჯიშო 2

# names.csv ფაილში არსებული ინფორმაცია 
# გადმოაკოპირე names.txt ფაილში.

with open(r".\Homeworks\HW_14_2024-01-18\HW_14_2024-01-18_files"
          r"\names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    csv_content_str = ""
    for line in csv_reader:   
        csv_content_str += (",".join(line) + "\n")     
    
with open(r".\Homeworks\HW_14_2024-01-18"
    r"\HW_14_2024-01-18_files\names.txt", "w") as txt_file:
    txt_file.write(csv_content_str)





#------------------------------------------------------------------#
