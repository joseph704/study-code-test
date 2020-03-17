hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data,value):
    # Linear Probing 기법
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address,len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
        else:
            hash_table[hash_address] = [index_key, value]

def read_data(data):
    # Linear Probing 기법
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address,len(hash_table)):
            # 없을 시
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None




save_data('dk','0101012031023')
save_data('da','3333333333333')
save_data('dc','3333333333333')
print(read_data('dk'))
print(read_data('da'))