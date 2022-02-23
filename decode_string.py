class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                trs = ''
                tnum = ''
                x = stack.pop()
                while x != '[':
                    trs += x
                    x = stack.pop()

                x = stack.pop()
                while x.isdigit():
                    tnum += x
                    if len(stack)!=0:
                        x = stack.pop()
                    else:
                        break
                if not x.isdigit():
                    stack.append(x)
                
                for i in range(int(str(tnum[::-1]))):
                    stack.extend(trs[::-1])
        return ''.join(stack)
