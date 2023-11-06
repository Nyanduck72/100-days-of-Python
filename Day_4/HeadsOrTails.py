# Write a virtual coin toss program that will tell the user if it´s Heads or Tails
import random
coin_face = round(random.random())
if coin_face != 1:
    print("Tails")
else:
    print("Heads")
