def solve(ip, op):
    global count
    if(len(ip) == 0):
        if(len(op)>1 and (op[0] in cap)):
            k.add(op)
            return
        return
    op1 = op
    op2 = op

    op2 = op2 + ip[0]
    ip = ip[1:]
    solve(ip, op1)
    solve(ip, op2)
    return

global cap
count = 0
k = set()
cap = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
ip = input()
op = ""
solve(ip, op)
print(k)
