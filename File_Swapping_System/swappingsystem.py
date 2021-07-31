# Creating a function.
def swappingSystem():
    # Creating the variables.
    file1 = input('Enter the name of the 1st file you want to swap ')
    file2 = input('Enter the name of the 2nd file you want to swap ')

    # Creating the main functionality of our system.
    with open(file1,'r') as a:
        data_a = a.read()
    with open(file2,'r') as b:
        data_b = b.read()
    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as b:
        b.write(data_a)

print('File data swapping system.')
# Calling the function so that it can work.
swappingSystem()
print('Data swapped successfully!')
print('Thanks for swapping the data.')