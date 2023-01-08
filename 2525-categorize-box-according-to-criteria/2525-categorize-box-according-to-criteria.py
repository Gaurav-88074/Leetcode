class Solution:
    def categorizeBox(self, l: int, b: int, h: int, mass: int) -> str:
        v = l*b*h
        bul = max(l,b,h)>=10**4 or v>=10**9
        heavy = mass>=100
        if bul and heavy:
            return "Both"
        if bul and not heavy:
            return "Bulky"
        if not bul and heavy:
            return "Heavy"
        if bul:
            return "Bulky"
        if heavy:
            return "Heavy"
        if bul==False and heavy==False:
            return "Neither"