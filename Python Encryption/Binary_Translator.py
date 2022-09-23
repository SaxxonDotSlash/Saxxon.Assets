##Dont use this in finished project. This will be used as an example and testing area.


#def decimalToBinary(dec):
#    decimal = int(dec)
#    print(decimal, "in Binary: ", bin(ord(decimal)))

#def decimalToOctal(dec):
#    decimal = int(dec)
#    print(decimal, "in Octal: ", oct(ord(decimal)))

def decimalToHex(dec):
    decimal = int(dec)
    print(decimal, "in Hex:", hex(decimal))


print("Enter a number:")
dec = input()
#decimalToBinary(dec)
decimalToHex(dec)
#decimalToOctal(dec)