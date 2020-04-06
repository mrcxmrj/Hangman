string = "hello"
password = "_____"
for index, character in enumerate(string):
    if character == "l":
        password = password[:index] + "l" + password[index+1:]