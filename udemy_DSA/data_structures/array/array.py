# data structures are a collection of values, organize data
strings = ["a", "b", "c", "d"]

for i, n in enumerate(strings):
    print(i, n)
# lookup
index2 = strings[2] # O(1)

# append
strings.append("e") # O(1)

# pop
strings.pop() # O(1)

# insert
strings.insert(0, "z") # O(n)
strings.insert(2, "alien") # O(n)

print(strings)

# Static arrays - Set num of items in list. Dynamic arrays - Freedom to add or remove from array
# Python arrays are already dynamic

# Making your own array
class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data.get(index)

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length-1]
        del(self.data[self.length-1])
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


new_array = MyArray()
new_array.push("Hi")
new_array.push("Bye")
print(new_array.data)
new_array.pop()
new_array.delete(1)
print(new_array.data)