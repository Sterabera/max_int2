n = int(input("Enter the length of the sequence: "))  # Do not change this line

for i in range(1, n+1):
    if i == 1:
        new_number = num_1 = i
    elif i == 2:
        new_number = num_2 = i
    elif i == 3:
        new_number = num_3 = i
    else:
        new_number = num_1 + num_2 + num_3
        num_1, num_2, num_3 = num_2, num_3, new_number

    print(new_number, end=" ")
