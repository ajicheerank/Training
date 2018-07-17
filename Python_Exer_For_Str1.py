string1 = input("Input a String: ")
string2 = input("input the letter to search in the above string: ")

#1
print(string1.lower().count(string2.lower()))

#2
if string1[-1] == "!": print (string1.upper())
else : print(string1.lower())

#3
data = [str for str in string1 if not str.lower() in ['a','e','i','o','u']]
print ("" .join (data))    

#4
result =""
for x in range (0,len(string1)):
    if x%2 == 0:
        result += string1[x].upper()
    else:
        result += string1[x]
print(result)