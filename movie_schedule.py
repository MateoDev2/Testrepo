the_grinch = {"first showing" : "12:00pm", 
              "second showing" : "1:45pm",
              "third showing" : "3:30pm",
              "fourth_showing" : "5:15pm"} 
santa_clause_2 = {"first showing" : "12:45pm", 
              "second showing" : "1:45pm",
              "third showing" : "3:45pm",
              "fourth_showing" : "5:20pm"} 
elf = {"first showing" : "12:00pm", 
              "second showing" : "1:00pm",
              "third showing" : "3:00pm",
              "fourth_showing" : "5:00pm"} 
the_nightmare_before_christmas = {"first showing" : "12:00pm", 
              "second showing" : "1:55pm",
              "third showing" : "3:10pm",
              "fourth showing" : "5:30pm"} 

showings = ["The Grinch", "Santa Clause 2", "elf", "The Nightmare Before Christmas"]

print("Welcome to the theater!!! ")
print("Currenting showing: ")
for x in showings:
    print(x)
users_choice = input("what movie woud you like to watch: ")

    
if users_choice == "The Grinch":
    print("Here are the times for The Grinch: ")
    for x, y in the_grinch.items():
        print(x, y)
elif users_choice == "Santa Clause 2":
    print("Here are the times for Santa clause2: ")
    for x, y in santa_clause_2.items():
        print(x, y)
elif users_choice == "elf":
    print("Here are the times for elf: ")
    for x, y in elf.items():
        print(x, y)
elif users_choice == "The Nightmare Before Christmas":
    print("Here are the times for The Nightmare Before Christmas")
    for x, y in the_nightmare_before_christmas.items():
        print(x, y)
else:
    print("Sorry we currntly are not showing that right now ")

