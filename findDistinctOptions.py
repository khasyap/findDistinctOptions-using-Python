def findDistinctOptions(s):

    c1 = s.count('1')
    c2 = s.count('2')
    c3 = s.count('3')

    even = [c1 % 2 == 0, c2 % 2 == 0, c3 % 2 == 0]
    if even.count(True) == 3 or even.count(False) == 3:
        return 1
    else:
        return 2

if __name__ == "__main__":
    s = input()  # Get input from user
    result = findDistinctOptions(s)
    print(str(result))
