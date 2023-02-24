"""Implementation of a hash table"""


class HashTable:
    """
    A class to represent a Node in a hash table
    """
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        """Hash function"""
        my_hash = 0
        for letter in key:
            # this is going to be number between 0 and size due to the modulo operation
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        """Set item in the hash table"""
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """Get item from the hash table"""
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]
        return None

    def delete_item(self, key):
        """Delete key-value pair based on key from the hash table"""
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i, j in enumerate(self.data_map[index]):
                if j[0] == key:
                    removed_item = self.data_map[index].pop(i)
                    if not self.data_map[index]:
                        self.data_map[index] = None
                    return removed_item
        return None

    def keys(self):
        """Get all the keys of the hash table"""
        all_keys = []
        for ht_address in self.data_map:
            if ht_address is not None:
                for i in ht_address:
                    all_keys.append(i[0])
        return all_keys

    def print_hash_table(self):
        """Print hash table"""
        for k, v in enumerate(self.data_map):
            print(k, ":", v)
