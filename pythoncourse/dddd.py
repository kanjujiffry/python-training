# from sys import argv
# script, filename =argv
# txt_file =open(filename)
# print("here is name{}".format(filename))
# print("herw")
# print(txt_file.read())
# txt_file.close()
#
# # last programm
# target.close()
#
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.
And you have a {computer} computer.
""")
