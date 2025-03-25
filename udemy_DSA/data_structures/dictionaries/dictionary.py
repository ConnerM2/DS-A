student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for key in student_scores:
    score = student_scores[key]
    print(score)
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print (student_grades)

print(student_scores)


# Making own hash table (dictionary)

class HashTable:
    def __init__(self, size):
        self.data = [None] * size  # Initialize an array of given size

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []  # Create a new bucket if empty
        self.data[address].append([key, value])  # Store the key-value pair
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for pair in current_bucket:
                if pair[0] == key:
                    return pair[1]  # Return the value if key matches
        return None  # Return None if key is not found

# Example usage
hash_table = HashTable(10)
hash_table.set("name", "Conner")
hash_table.set("age", 20)

print(hash_table.get("name"))  # Output: Conner
print(hash_table.get("age"))   # Output: 20
print(hash_table.get("city"))  # Output: None (not found)
print(hash_table.data)

