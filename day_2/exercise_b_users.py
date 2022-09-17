users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])
# 2. Get Erik's hometown
print(users["Erik"]["home_town"])
# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])
# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])
# 5. Get the smallest of Erik's lottery numbers
print(min(users["Erik"]["lottery_numbers"]))
# 6. Return an list of Avril's lottery numbers that are even
def even_numbers(list):
    even_list = []
    for num in list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
avrils_lot_nums = users["Avril"]["lottery_numbers"]    
print(even_numbers(avrils_lot_nums))    
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name": "fluffy"})
# 10. Add another person to the users dictionary
users["Georgi"] = {
    "twitter": "gggtwit", 
    "lottery_numbers": [1, 13, 3, 33, 7, 23],
    "home_town": "Stara Zagora",
    "pets": [
      {
        "name": "lora",
      }
    ]
    }
print(users)    