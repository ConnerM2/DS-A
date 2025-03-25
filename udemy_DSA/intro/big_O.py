fish = ["not nemo", "nemo", "not nemo", "not nemo", "not nemo", "not nemo", "not nemo", "not nemo"]

def find_nemo(array):
    for i in array:
        if i == "nemo":
            print("Found nemo!")
            break

find_nemo(fish) # O(n) --> linear time: num of inputs = num of calculations

def first_fish(array):
    print(array[0])

first_fish(fish) # O(1) --> Constant time

box = ["a","b","c","d"]

def pair_each_item(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])

pair_each_item(box) # O(n^2) --> Quadratic time

# Space Complexity

def boo(n):
    for num in n:
        print("Booo!")

boo([1,2,3,4,5,]) # Space Complexity O(1)

def hi_n_times(n):
    hi_array = []
    for i in range(n):
        hi_array.append("hi")
    return hi_array

print(hi_n_times(6)) # Space complexity O(n)

# Twitter exercise
# find 1st and nth

array = [
    {"tweet": 'hi',"date": 2012},
    {"tweet": 'my', "date": 2014},
    {"tweet": 'person', "date": 2018}
]

print(array[0]["date"])
