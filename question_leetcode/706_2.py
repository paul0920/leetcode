class MyHashMap:

    def __init__(self):
        self.k = 1009
        self.buckets = [[] for i in range(0, self.k)]

    def put(self, key, value):
        bucket = self.buckets[key % self.k]
        item = next((item for item in bucket if item[0] == key), None)
        if item:
            item[1] = value
        else:
            bucket.append([key, value])

        # for item in bucket:
        #     if item[0] == key:
        #         item[1] = value
        #         exit()
        #
        # bucket.append([key, value])

    def get(self, key):
        bucket = self.buckets[key % self.k]
        item = next((item for item in bucket if item[0] == key), None)
        if item:
            return item[1]
        else:
            return -1

    def remove(self, key):
        bucket = self.buckets[key % self.k]
        item = next((item for item in bucket if item[0] == key), None)
        if item:
            bucket.remove(item)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

hashobj = MyHashMap()
hashobj.put(1, 27)
print hashobj.get(2)
print hashobj.get(1)
