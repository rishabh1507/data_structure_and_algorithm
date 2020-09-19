def solve(ip, op):
    if(len(ip) == 0):
        print(op, end=",")
        return
    op1 = op
    op2 = op

    op2 = op2 + ip[0]
    ip = ip[1:]
    solve(ip, op1)
    solve(ip, op2)
    return


ip = input()
op = ""
solve(ip, op)
