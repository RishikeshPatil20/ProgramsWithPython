str1=input("Enter the first String :")
str2=input("Enter the second String :")

if(len(str1)!=len(str2)):
    print("Two string are not anagrams")
else:
    string1=sorted(str1)#inbuild method to sort 
    string2=sorted(str2)

if(string1==string2):
    print("two string are anagrams")
else:
    print("two string are not anagrams")