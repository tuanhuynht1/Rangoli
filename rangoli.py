def print_rangoli(size):
    if (size == 1):
        print('a')
        return
    n = chr(size+96)
    l=[n]
    log = []
    num = ord(n)-97
    dashes = ['-']*num
    print(*dashes,l[0],*dashes, sep = '-')
    while(True):
        num -= 1
        dashes = ['-']*num
        r=l[::-1]
        m= [chr(ord(l[-1])-1)]
        buff = l + m + r
        log.append(dashes+buff+dashes)
        print(*dashes,*buff,*dashes, sep = "-")
        l.extend(m)
        if m[0] == 'a':
            break
    log.reverse()
    for i in log[1:]:
        print(*i, sep ="-")
    num = ord(n)-97
    dashes = ['-']*num
    print(*dashes,l[0],*dashes, sep = '-')

if __name__ == '__main__':
    n = int(input("Number of Rangoli's: "))
    for i in range(1,n+1):
        print_rangoli(i)
        print()
