class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            arr = image[i][::-1]
            for j in range(len(arr)):
                arr[j]^=1
            image[i]=arr
        return image