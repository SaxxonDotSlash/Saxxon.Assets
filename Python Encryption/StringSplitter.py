from os.path import split

Message = input('Enter your message: ')
SplitList = []

string = Message
print(string.split())
print("Stringing")

SplitList = split(string)
print('Assigning to a list')



#Use ord to get the ASCII value of a character
#Use chr to get the character from an ASCII value
#ASCII_List = [ord(i) for i in SplitList]
#print(ASCII_List)

