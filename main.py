shopping_dict = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"],
}
print("Lista zakupów")
for key, value in shopping_dict.items(): 
      print(f"Idę do {key.capitalize() } , i kupuję tam {value}.")
print(f'W sumie kupuję {len(shopping_dict.values())} produktów.')



for num in range(1,100):        
            if  num % 5 == 0:
                print(str(num) + " ", end = "")                 
            else:
                pass
for num in range(1,100):       
            if num % 5 == 0:
                 print(str(num**3) + " ", end = "")  
            else:
              pass