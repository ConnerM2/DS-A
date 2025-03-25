# Create a function that reverses a string
text = "testing"

# Solution 1
def reverse_string(user_input):
    new_arr = list(user_input)
    rev_str = []

    i = len(new_arr) - 1

    while i >= 0:
        rev_str.append(new_arr[i])
        i -= 1

    return "".join(rev_str)

print(reverse_string(text))

# Solution 2
def reverse_string2(user_input):
    return user_input[::-1]

print(reverse_string2("testing"))