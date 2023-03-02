class Solution:
    def compress(self, chars: List[str]) -> int:
        c= 1
        pre = chars[0];
        res = []
        #-------------
        index = 0
        size  = 0
        #----------
        for i in range(1,len(chars)):
            if chars[i]==pre:
                c+=1;
            else:
                this = chars[i]
                if c==1:
                    # res.append(pre)
                    chars[index] = pre
                    index+=1
                    size+=1
                    
                else:
                    # res.append(pre)
                    # res.append(str(c))
                    chars[index] = pre
                    index+=1;
                    size+=1
                    for v in str(c):
                        chars[index] = v
                        index+=1
                        size+=1
                pre = this
                c=1
                
        if c==1:
            chars[index] = pre
            index+=1
            size+=1

        else:
            chars[index] = pre
            index+=1;
            size+=1
            for i in str(c):
                chars[index] = i
                index+=1
                size+=1
        # print(res)
        return size