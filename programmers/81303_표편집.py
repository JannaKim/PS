def solution(n, k, cmds):
    node = {}
    node[0], node[n - 1] = [n - 1, 1], [n - 2, 0]
    for i in range(1, n - 1):
        node[i] = [i - 1, i + 1]
            
    cache = []
    ptr = k
    for cmd in cmds:
        if len(cmd) > 1:
            c, x = cmd.split()
            x = int(x)
            if c == 'D':
                while x:
                    ptr = node[ptr][1]
                    x -= 1
            else:
                while x:
                    ptr = node[ptr][0]
                    x -= 1
        else:
            if cmd == 'C':
                node[node[ptr][0]][1] = node[ptr][1]
                node[node[ptr][1]][0] = node[ptr][0]
                cache.append([ptr, node[ptr]])
                
                tmp = node[ptr]
                del node[ptr]
                
                if tmp[1] == 0:
                    ptr = tmp[0]
                else:
                    ptr = tmp[1]
            else:
                cur, [prv, nxt] = cache.pop()
                node[cur] = [prv, nxt]
                node[prv][1], node[nxt][0] = cur, cur
        
    answer = ['X'] * n
    for i in range(n):
        if i in node:
            answer[i] = 'O'
            
    return ''.join(answer)