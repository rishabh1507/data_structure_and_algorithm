#code
def Print(ip):
    if(ip == 1):
        print(ip, end=" ")
        return

    Print(ip-1)
    print(ip, end=" ")


t = int(input())

for i in range(t):
    ip = int(input())
    Print(ip)
    print("")
