# WRITE YOUR FUNCTIONS HERE
from ast import Num


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,cash):
    total = pet_shop["admin"]["total_cash"]
    if cash >= 0:
        total += cash 
    return get_total_cash(pet_shop)       





    
         





    

