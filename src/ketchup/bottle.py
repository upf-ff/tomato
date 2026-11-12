import random

def squeeze(food="fries"):
    coin = random.random() > 0.5
    if coin:
        print("too much ketchup on", food)
    else:
        print("a little ketchup on", food)