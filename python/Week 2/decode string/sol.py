def decodeString(s):
    stack = []
    currStr = ''
    currNum = 0

    for c in s:
        if c == '[':
            stack.append(currStr)
            stack.append(currNum)
            currStr = ''
            currNum = 0
        elif c == ']':
            num = stack.pop()
            prevStr = stack.pop()
            currStr = prevStr + num*currStr
        elif c.isdigit():
            currNum = currNum * 10 + int(c)
        else:
            currStr += c        
    
    return currStr