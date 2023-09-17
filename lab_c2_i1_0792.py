class translator:
    def deciToRoman(self, num):
        result = ""
        roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        for reNum,ro in roman:
            q,r = divmod(num,reNum)
            result += ro * q
            num = r
        return result
    def romanToDeci(self, s):
        roman = dict({"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1})
        result = 0
        i = 0
        while(i < len(s)):
            if(s[i:i+2] in roman and i+1 is not len(s)):
                result += roman[s[i:i+2]]
                i += 2
            else:
                result += roman[s[i]]
                i += 1
        return result
num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
