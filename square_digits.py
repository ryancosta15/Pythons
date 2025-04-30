def square_digits(num):
    num = str(num)
    array = []
    for i in range (0,len(num)):
        z = int(num[i])
        z = z ** 2
        array.append(z)
    array = int(str(array).replace(",","").replace(" ","").strip("[]"))
    return array
