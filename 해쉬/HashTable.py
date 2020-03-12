hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data,value):
    key_address = hash_function(get_key(data))
    hash_table[key_address] = value

def read_data(data):
    key_address = hash_function(get_key(data))
    return hash_table[key_address]