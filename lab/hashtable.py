class HashTable:
    def __init__(self, size=7):  # Corrected to use double underscores
        self.data_map = [None] * size
    
    def _hash(self, key):  # Renamed to avoid conflict with built-in __hash__
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys


# Test the corrected code
my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("lumber", 70)
my_hash_table.set_item("washers", 50)
my_hash_table.print_table()
