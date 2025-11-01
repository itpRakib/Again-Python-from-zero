try:
    a = int(input("Enter a number: "))
    print(a + 10)
except Exception as e:
    print('Some error occurred:', e)