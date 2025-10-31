i = 0

while (i<10):
    print(i)
    i += 1

while(False):
    print("Infinite loop")      
    break
print("Loop ended")


while (True):
    num = int (input("Enter a number (0 to exit): "))
    if num == 0:
        break

for j in range(5):
    if j == 3:
        continue
    print(j+10)