def reverse(string):
    string = "".join(reversed(string))
    return string


s = input("Nhập vào 1 chuỗi:")

print("Chuỗi đó có phải là palindrome?", s == reverse(s))
