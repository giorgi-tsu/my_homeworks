## 5. დაწერე პროგრამა, რომელიც გთხოვს შეიყვანო ტექსტი, დათვლის მასში არსებული
## სიმბოლოების რაოდენობას და გამოიტანს შედეგს შემდეგნაირად:

## Number of symbols: 5

txt = input("Enter your text here: ")
# txt = txt.replace(" ", "") # Uncomment if you do not want spaces to be counted.

print(f"Number of symbols: {len(txt)}")