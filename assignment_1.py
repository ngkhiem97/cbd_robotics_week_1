#!/usr/bin/env python
# coding: utf-8


import random



questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

# get the answers from user input
answers = {}
for taste in questions:
    answers[taste] = input(questions[taste] + " [Y/n]: ")

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

print("Your ingredients are:")
for taste in ingredients:
    if answers[taste].upper() != "N":
        choice = random.randint(0, 2)
        print(ingredients[taste][choice])

