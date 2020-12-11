import hashlib

def my_generator(file):
    with open(file , "rb") as f:
        content = f.readlines()
        for line in content:
            try:
                hash_object = hashlib.md5(line)
                yield hash_object.hexdigest()

            except:
                yield "Error"

if __name__ == '__main__':
    generator1 = my_generator('result.txt')
    for item in generator1:
        print(item)
