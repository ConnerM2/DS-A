class Cookie:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color

cookie1 = Cookie("Red")
cookie2 = Cookie("Green")

print(cookie1.get_color(), cookie2.get_color())

cookie2.set_color("Brown")

print(cookie1.get_color(), cookie2.get_color())

# Pointers
num1 = 1
num2 = num1

print(id(num1), id(num2))

dict1 = {"value": 10}
dict2 = dict1

print(dict1, dict2)

dict2["value"] = 20

print(dict1, dict2)
print(id(dict1), id(dict2))
