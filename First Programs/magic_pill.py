name = input("Type your name: ")
surname = input("Type your surname: ")
age = int(input("Type your age: "))
magic_pill = 10
age -= magic_pill
message_name = "hello" + " " + surname
message_age = " you are " + str(age) + " years old!"
message = message_name + message_age
print(message)