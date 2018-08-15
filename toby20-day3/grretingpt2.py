name = input("What is your name?")
print("Hello there " + name.capitalize())
num_let = len(name)
print("Your name is " + str(len(name)) + " letters long!")
print("The first letter of your name is " + name[0].capitalize() + " and the last letter in your name is " + name[len(name) - 1].capitalize())
q_mood = input("How are you?")
mood = q_mood.lower()
if mood == "good":
    print("Nice man")
