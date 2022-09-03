class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.check(nums,target,0,len(nums)-1)
    def binarySearch(self,array,key,start,end):
        if start>end:
            return -1
        else:
            mid = (start+end)//2
            if key == array[mid]:
                return mid
            elif key< array[mid]:
                return self.binarySearch(array,key,start,mid-1)
            else:
                return self.binarySearch(array,key,mid+1,end)
    def right(self,array,key,start,end):
        # print("Right :",array[start:end+1])
        index=self.binarySearch(array,key,start,end)
        if index<len(array)-1 and array[index+1]==key:
            return self.right(array,key,index+1,end)
        else:
            return index
    def left(self,array,key,start,end):
        # print("left",array[start:end+1])
        index=self.binarySearch(array,key,start,end)
        if index>0 and array[index-1]==key:
            return self.left(array,key,start,index-1)
        else:
            return index
    def check(self,array,key,start,end):
        index = self.binarySearch(array,key,start,end);
        if index==-1:
            return [-1,-1]
        l = self.left(array,key,start,end)
        r = self.right(array,key,start,end)
        return [l,r]
        