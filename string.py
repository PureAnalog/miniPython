stringVar= "this is a sample string"
print(stringVar)

numOne=2
wordOne="Cats"

print("I have {} {}".format(numOne, wordOne))

print("I have "+ str(numOne)+ " " + wordOne)

wordOne += " ??? "

print(wordOne)

for i in stringVar:
    print i

print("\n")
 
print("Hello \"you\"!")

print(stringVar.find("sample"))

stringVar = stringVar.replace('e', 'a')

print(stringVar)

longString = "                         one two three                 "
string1= stringVar.strip()
print(string1)

print(stringVar.split()) # It is not longer a string, but a list

for i in stringVar.split():
    print i

string1 = ' '.join(string1)
print(string1)

print( len(string1))

string2= r"I don 't want to \n"

print( string2)
