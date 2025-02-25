class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
    
    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self._hash(key)
        while self.data_map[index] is not None:
            # If the key already exists, update the value
            if self.data_map[index][0] == key:
                self.data_map[index][1] = value
                return
            # Linear probing: move to the next index
            index = (index + 1) % len(self.data_map)
        # Insert the key-value pair
        self.data_map[index] = [key, value]

    def get_item(self, key):
        index = self._hash(key)
        start_index = index  # To avoid infinite loops
        while self.data_map[index] is not None:
            if self.data_map[index][0] == key:
                return self.data_map[index][1]
            # Linear probing: move to the next index
            index = (index + 1) % len(self.data_map)
            if index == start_index:  # Avoid infinite loop
                break
        return None

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def keys(self):
        keys = []
        for item in self.data_map:
            if item is not None:
                keys.append(item[0])
        return keys


# Test the linear probing hash table
my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("lumber", 70)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("screws", 80)  # To test collisions
my_hash_table.print_table()

print("Keys:", my_hash_table.keys())
print("Value for 'lumber':", my_hash_table.get_item("lumber"))
