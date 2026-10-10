favourites_chais = [
  "Masala chai",
  "Oolang chai",
  "Green Tea",
  "Lemon Tea", 
  "Elachi Tea",
  "Oolang chai",
  "Pudina Tea",
  "Green Tea",
  "Masala chai"
  
]

unique_items = {tea for tea in favourites_chais}
print(unique_items)


reciepies = {
  "Masala chai": ["water", "milk", "sugar", "tea leaves", "spices"],
  "Oolang chai": ["water", "milk", "sugar", "tea leaves"],
  "Green Tea": ["water", "green tea leaves"],
  "Lemon Tea": ["water", "lemon juice", "sugar", "tea leaves"],
  "Elachi Tea": ["water", "milk", "sugar", "tea leaves", "cardamom"],
  "Pudina Tea": ["water", "milk", "sugar", "tea leaves", "mint leaves"]
}

unique_spicies = {spices for ingrediant in reciepies.values() for spices in ingrediant  }
print(unique_spicies)


"""
In case of the dictionary you will be having the 
keys and the values 

think you have a dctionary 

tea_prieces_inr = {
  "Masala_chai" : 32,
  "Oolang chai" : 453,
  "Cappuchhino" : 321
  }
  
tea+prices_inr = {key : value / 90 for key , value in tea_prices_inr.items()}


"""