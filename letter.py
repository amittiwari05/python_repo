#name = input("Enter your name:")
#print("good night" + name)
letter = ''' Dear <|NAME|>,
greatings from us. You are selected in our company.
You are selected!
Have a nice day ahead!
Thanks and regards.
google
<|DATE|>'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)
