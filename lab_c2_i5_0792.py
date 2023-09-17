def bon(w):
    def most_common(lst):
        return max(set(lst), key=lst.count)
    most = most_common(w)
    sc = ord(most) - 96
    sCode = sc * 4
    return sCode
secretCode = input("Enter secret code : ")
secretCode = list(secretCode)
print(bon(secretCode))