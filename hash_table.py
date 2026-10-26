# hash_table.py
# implementation of simple hash table
# we'll use separate chaining with Python's built-in 
# list type acting as the chains
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a data structure yourself is the best
# way to learn how it works.
# Modified by: Tristan Crawford
from random import randint

class HashTable:
    MAX_LOAD_FACTOR = 0.7
    GROWTH_FACTOR = 2

    def __init__(self, slots = 10):
        self.slots = slots
        self.num_items = 0
        self.backing_store = [[] for _ in range(slots)]

    def _hash(self, key):
        return hash(key) % self.slots


    def insert(self, key, value):
         chain = self.backing_store[self._hash(key)]
        for pair in chain:
            if pair[0] == key:
                pair[1] = value
                return
         chain.append([key, value])
        self.num_items += 1
        if self.num_items / self.slots > HashTable.MAX_LOAD_FACTOR:
            self._resize()

    def get(self, key):

        for pair in self.backing_store[self._hash(key)]:
            if pair[0] == key:
                return pair[1]   
        return None
        

    def remove(self, key):
         chain = self.backing_store[self._hash(key)]
         for i in range(len(chain)):
            if chain[i][0] == key:
                del chain[i]
                self.num_items -= 1
                return True

         return False       
    
    # update the hash table based on GROWTH_FACTOR
    # make sure to move everything over to the new table
    def _resize(self):
        self.slots = self.slots * HashTable.GROWTH_FACTOR
        self.backing_store = [[] for _ in range(self.slots)]
        for chain in old_store:
            for pair in chain:
               
                self.backing_store[self._hash(pair[0])].append(pair)        

    def __str__(self):
        return str(self.backing_store)
