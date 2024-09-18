# cook your dish here
def maxfun(s):
    n = len(s)
    count = 0

    i = 0
    while i < n - 1:
        curr = s[i]
        next_char = s[i + 1]
        if (curr == 'x' and next_char == 'y') or (curr == 'y' and next_char == 'x'):
            count += 1
            i += 1  # Skip the next character as it forms a valid pair
        i += 1

    return count

# Input handling
t = int(input())  # Number of test cases

for _ in range(t):
    s = input()  # Input string
    print(maxfun(s))
