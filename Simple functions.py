#count function userdefined
def countfunction():
    print("Enter the String:")
    str1=input()
    print("Enter the Character to count in the above string:")
    str=input()
    str2=str1.count(str,0,100)
    print(str2)
#swapcase function userdefined
def swapestring():
    print("Enter the String to Swape case:")
    str1=input()
    str2=str1.swapcase()
    print(str2)
#islower function userdefined
def lower():
    print("Enter the String to check whether it is lowercase or not:")
    str1=input()
    str2=str1.islower()
    if(str2==True):
        print("Given string is Lower")
    else:
        print("Its not lower")
#capital function userdefined
def capital():
    print("Enter the string to make capital:")
    str1=input()
    str2=str1.capitalize()
    print(str2)
#title function userdefine
def strtitle():
    print("Enter the String to make capital of each word in a string:")
    str1=input()
    str2=str1.title()
    print(str2)
#replace function userdefine
def strreplace():
    print("Enter string to work on replace:")
    str1=input()
    print("Which word you want to remove:")
    str2=input()
    print("Which word you want to replace:")
    str3=input()
    str4=str1.replace(str2,str3)
    print(str4)
#slice operator function userdefine
def strslice():
     print("Enter the string to work on the slice operation:")
     str1=input()
     print("Start letter you want to slice:")
     str2=int(input())
     print("End letter you want to slice:")
     str3=int(input())
     print(str1[str2:str3])
#len() function userdefine
def strlen():
        print("Enter the String to find Length:")
        str1=input()
        str2=len(str1)
        print(str2)
#max() function userdefine
def strmax():
    print("Enter the string to find maximum character:")
    str1=input()
    print("Maximum character is:",max(str1))
#min() function userdefine
def strmin():
    print("Enter the string to find minimum character:")
    str1=input()
    print("Minimum character is:",min(str1))

""" Getting Choice From User 1 to 10 and call the function according to its order 1 to 10. All the function defined above and called in the another function called main()
after calling the function asking to user whether continue or not if not stop the program otherwise it could be continued """
print("String Functions")
print("\n 1.Count() \n 2.SwapCase() \n 3.islower() \n 4.Capitalize() \n 5.title() \n 6.replace() \n 7.slice() \n 8.length() \n 9.max() \n 10.min()")
def main():
    while True:
        print("Enter the choice for the above string function:")
        choice=input()
        if choice=="1":
            countfunction()  
        elif choice=='2':
            swapestring()
        elif choice=='3':
            lower()
        elif choice=='4':
            capital()
        elif choice=='5':
            strtitle()
        elif choice=='6':
            strreplace()
        elif choice=='7':
            strslice()
        elif choice=='8':
            strlen()
        elif choice=='9':
            strmax()
        elif choice=='10':
            strmin()
        else:
            print("\nEnter the valid choice between 1 to 10..")
        print("Do You want to continue or not(Y/N)")
        con=input()
        if(con=="N" or con=="n"):
            print("Program is stoped")
            break
main()
