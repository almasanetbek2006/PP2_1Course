list = [str(i) for i in input().split()]


with open('ako.txt', 'w') as file:
    
    for i in list:
        file.write("%s\n" % i)

print("List has been written to 'ako.txt'")