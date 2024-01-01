def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        stacklist=[]
        address=[]
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                stacklist.append(s[i])
                address.append(i)
                # print("yes")
        newstr=""
        print(stacklist,address)
        for i in range(len(s)):

            tempind=address.pop()
            tempchar=stacklist.pop()
            if(s[i] in ['a','e','i','o','u','A','E','I','O','U']):
                 newstr=newstr+tempchar
            # if tempind==i:
                # newstr=newstr+tempchar
            else:
                newstr=newstr+s[i]
                stacklist.append(tempchar)
                address.append(tempind)

        print(newstr)
reverseVowels("hello")


