# writing a new file
# Note: When writing a file and if the file doesn't exist then its going to create a new file.
with open("./file_managing/test.txt", "w") as f:
    f.write("testing is part of mastering ssssss.")
    
# appending a new item in the file    
with open("./file_managing/test.txt", "a") as f:
    f.write("\ntesting is part of mastering skills")
    
# Opening a file
with open("./file_managing/test.txt") as f:
    contents = f.read()
    print(contents)