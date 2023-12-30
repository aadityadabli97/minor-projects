BANKER ROULETTE

You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

names_string="Aaditya,Akash,Dinesh,"Aryav"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
i=len(names)
person_selected=random.randint(0,i-1)
person_paying=names[person_selected]
print(f"{person_paying} is going to buy the meal today!")
