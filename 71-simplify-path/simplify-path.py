class Solution:
    def simplifyPath(self, path: str) -> str:
        main_path = []
        temp = []
        for i in path:
            if i == '/':
                if temp and ''.join(temp) != '.' and ''.join(temp) != '..':
                    main_path.append(''.join(temp)) #append as single string
                    temp = [] #reset it
                else:
                    if not temp: 
                        continue 
                    elif ''.join(temp) == '.':
                        temp = [] #reset after '.', and don't add in stack
                    else:
                        if main_path: #value must be present
                            main_path.pop() #since encountered '..'
                        temp = [] #reset because the '..'

            elif i == '.':
                temp.append(i)
            else:
                temp.append(i)
        if temp:
            if ''.join(temp) == '..':
                if main_path: #value must be present
                    main_path.pop()
            elif ''.join(temp) == '.':
                pass
            else:
                main_path.append(''.join(temp))
        
        return '/' + '/'.join(main_path)
            