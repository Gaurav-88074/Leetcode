class Solution:
    def maximumTime(self, time: str) -> str:
        arr = list(time)
        # print(arr)
        if arr[0]=="?":
            if arr[3]=="0" and arr[4]=="0":
                arr[0]="2"
            if arr[1]=="?" or int(arr[1])<4:
                arr[0]="2"
            else:
                arr[0]="1"
        if arr[1]=="?":
            if arr[0]!="2":
                arr[1]="9"
            elif arr[3]=="0" and arr[4]=="0":
                arr[1]="4"
            else:
                arr[1]="3"
        
        if arr[3]=="?":
            arr[3]="5"
        
        if arr[4]=="?":
            arr[4]="9"
        
        return "".join(arr)