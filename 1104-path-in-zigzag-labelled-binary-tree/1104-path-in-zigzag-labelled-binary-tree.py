class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        #-----------------------------------
        d = defaultdict(list)
        nodeValueDictIndex = defaultdict(int)
        nodeValueDictListIndex = defaultdict(int)
        #------------------------------------
        maxValue = label
        p=1
        index=1
        currentValue=1
        while currentValue<maxValue:
            ii=1
            for nodeValue in range(currentValue,pow(2,p)):
                d[index].append(nodeValue)
                #===================================
                nodeValueDictIndex[nodeValue]=index
                nodeValueDictListIndex[nodeValue] =ii
                #===================================
                ii+=1
            #-----------------------
            currentValue = pow(2,p)
            index+=1
            p+=1
            #-----------------------
        res = []
        
        #1 -> sidha
        #0 -> reversed
        direction = 1 if (nodeValueDictIndex[label]&1)==1 else 0
        res.append(label)
        label//=2
        direction=0
        while label>0:
            #labelDictIndex
            a = nodeValueDictIndex[label]
            #labelActualIndexInList
            b = nodeValueDictListIndex[label]
            l = d[a]
            # print("list",l)
            if direction==1:
                res.append(label)
            else:
                res.append(l[ -b ])
            #------------
            label//=2
            #------------
            direction^=1
        # print(res)
        
        return reversed(res)