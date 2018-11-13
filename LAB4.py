import time


# HashTable class using chaining.
class ChainingHashTable:
    total_comparison = 0
    num_words = 0  # Constructor with optional initial capacity parameter.

    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=26):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, item):
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)  # %26
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        ChainingHashTable.num_words += 1
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for i in range(len(bucket_list)):
            if key == bucket_list[i]:
                ChainingHashTable.total_comparison += i
                return i
        # if key in bucket_list:
        #    # find the item's index and return the item that is in the bucket list.
        #    item_index = bucket_list.index(key)
        #    return bucket_list[item_index]
        # else:
        #   # the key is not found.
        #    return None
        ChainingHashTable.total_comparison += len(bucket_list)
        return None


def hash_length(word):
    return len(word)


def hash_base26(word):
    s = 0
    for i in range(len(word)):
        s += ord(word[i]) * 26 ** i
    return s


def hash_sum_char_position(word):
    s = 00
    for ch in word:
        s += ord(ch)
    return s


table = ChainingHashTable()


def load_words(table):
    try:
        with open('words.txt', 'r') as file:
            for word in file:
                table.insert(word.strip())
    except FileNotFoundError:
        print("Sorry, file not found.")
        exit(1)


def print_anagrams(word, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if table.search(str) != None:
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur
            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(before + after, prefix + cur)


def load_factor(table):
    nb_buckets = len(table.table)
    keys = 0;
    for bucket in table.table:
        keys += len(bucket)
    return keys / nb_buckets


def main():
    print("1. Sum position of letters.")
    print("2: English language as a base-26 number.")
    print("3: Word length.")
    hash_selection = input("Select hash function: ")
    if "1" == hash_selection:
        hash = hash_sum_char_position
    elif "2" == hash_selection:
        hash = hash_base26
    else:
        hash = hash_length
    load_words(table)
    print(" ")
    print("Table's load factor is:", load_factor(table))
    word = input("Enter a word (0 for exit): ")
    start_time = time.time()
    while (word != "0"):
        print("Anagrams:")
        print_anagrams(word)
        print(" ")
        print("Average number of comparisions: ", table.total_comparison / table.num_words)
        print("Running time: %s seconds " % (time.time() - start_time))
        print(" ")
        word = input("Enter a word (0 for exit): ")


main()






