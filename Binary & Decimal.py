
def binary():
    number=int(input("Enter number in decimal format:"))
    temp=number
    binary=""
    while number>0:
        rem=number%2
        binary+=str(rem)
        number=number//2
    print("The binary equivalent of "+str(temp)+" is "+binary[::-1]+" .")


def decimal():
    binary = input("Enter number in binary Format: ");
    decimal = int(binary, 2);
    print(binary,"in Decimal =",decimal);
 



def start():
    print("Enter '1' to go from binary to decimal.")
    print("Enter '2' to go from decimal to binary.")
    ans = input(">>> ")
    if ans == "1":
        decimal()
    elif ans == "2":
        binary()

        
    
start()
