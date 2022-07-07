#made by lulz714#
print("Select a file. (directory)")
file = 0
while True:
    directory = input()
    file_found = False
    try:
        file = open(directory,"r")
        file_found = True
    except FileNotFoundError:
        file_found = False
        print("Invalid directory, please try again.")
    if file_found:
        break
    else:
        continue
print("\n" + file.read())
file.close()
print("Please enter what you want to add to file:")
newtext = input()
file = open(directory,"a")
file.write(newtext)
file.close()
file = open(directory,"r")
print("\nNew file context:\n" + file.read())
file.close()