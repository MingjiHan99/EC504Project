import math
import time
import random


class VEB:
    # size n
    def __init__(self, n):
        self.round = 1
        self.size = n
        self.min = -1
        self.max = -1
        self.minvalue = -1
        self.maxvalue = -1
        if n <= 2:
            self.summary = None
            self.clusters = [None] * 0
        else:
            self.summary = VEB(math.ceil(math.sqrt(self.size)))
            self.clusters = [VEB(math.ceil(math.sqrt(self.size))) for i in range(math.ceil(math.sqrt(self.size)))]

    def high(self, x):
        div = math.ceil(math.sqrt(self.size))
        return x // div

    def low(self, x):
        mod = math.ceil(math.sqrt(self.size))
        return x % mod

    def generate_index(self, x, y):
        ru = math.ceil(math.sqrt(self.size))
        return (x or 0) * ru + (y or 0)


def VEB_min(veb):
    if veb.min == -1:
        return -1
    else:
        return veb.min


def VEB_max(veb):
    if veb.max == -1:
        return -1
    else:
        return veb.max


def insert(veb, key, value):
    if veb.min == -1:
        veb.min = key
        veb.max = key
        veb.minvalue = value
        veb.maxvalue = value
    else:
        if key < veb.min:
            veb.min, key = key, veb.min
            veb.minvalue, value = value, veb.minvalue
        if veb.size > 2:
            if VEB_min(veb.clusters[veb.high(key)]) == -1:
                insert(veb.summary, veb.high(key), value)
                veb.clusters[veb.high(key)].min = veb.low(key)
                veb.clusters[veb.high(key)].max = veb.low(key)
                veb.clusters[veb.high(key)].minvalue = value
                veb.clusters[veb.high(key)].maxvalue = value
            else:
                insert(veb.clusters[veb.high(key)], veb.low(key), value)
        if key > veb.max:
            veb.max = key
            veb.maxvalue = value


def isMember(veb, key):
    if veb.size < key or veb.size == 2:
        return False
    if veb.min == key or veb.max == key:
        return True
    return isMember(veb.clusters[veb.high(key)], veb.low(key))


def lookup(veb, key):
    if isMember(veb, key):
        if veb.min == key:
            return veb.minvalue
        elif veb.max == key:
            return veb.maxvalue
        return lookup(veb.clusters[veb.high(key)], veb.low(key))


def VEB_successor(veb, x):
    if veb.size == 2:
        if x == 0 and veb.max == 1:
            return 1
        else:
            return None
    elif veb.min is not None and x < veb.min:
        return veb.min
    else:
        if VEB_max(veb.clusters[veb.high(x)]) is not None and veb.low(x) < VEB_max(veb.clusters[veb.high(x)]):
            return veb.generate_index(veb.high(x), VEB_successor(veb.clusters[veb.high(x)], veb.low(x)))
        else:
            if VEB_successor(veb.summary, veb.high(x)) is None:
                return None
            else:
                cluster_next = VEB_successor(veb.summary, veb.high(x))
                offset = VEB_min(veb.clusters[cluster_next])
                return veb.generate_index(cluster_next, offset)


def delete(veb, key):
    # clear the saved value
    insert(veb, key, -1)
    if veb.max == veb.min:
        veb.min = -1
        veb.max = -1
    elif veb.size == 2:
        if key == 0:
            veb.min = 1
        else:
            veb.min = 0
        veb.max = veb.min
    else:
        if key == veb.min:
            key = veb.generate_index(VEB_min(veb.summary), VEB_min(veb.clusters[VEB_min(veb.summary)]))
            veb.min = key
        delete(veb.clusters[veb.high(key)], veb.low(key))
        if VEB_min(veb.clusters[veb.high(key)]) == -1:
            delete(veb.summary, veb.high(key))
            if key == veb.max:
                if VEB_max(veb.summary) == -1:
                    veb.max = veb.min
                else:
                    veb.max = veb.generate_index(VEB_max(veb.summary), VEB_max(veb.clusters[VEB_max(veb.summary)]))
        elif key == veb.max:
            veb.max = veb.generate_index(veb.high(key), VEB_max(veb.clusters[veb.high(key)]))

#test basic functions
veb = VEB(10)
insert(veb, 1, "a")
insert(veb, 8, "b")
insert(veb, 2, "c")
insert(veb, 6, "d")


print(isMember(veb, 6))
print(lookup(veb, 6))

delete(veb, 6)
insert(veb, 6, "f")
print(lookup(veb, 6))

delete(veb, 2)
print(isMember(veb, 2))
print(VEB_successor(veb, 1))





n = 4
while n < 800001:
    veb = VEB(n)
    # Inserting keys

    for i in range(n):
        insert(veb, i, "12")

    start_time = time.time()
    for i in range(1000000):
        lookup(veb, i % n)
    end_time = time.time()
    print(math.log(n), " ", end_time - start_time)
    n = n * n
# print(isMember(veb, 2))
# print(VEB_predecessor(veb, 4), VEB_successor(veb, 1))
# print(VEB_min(veb), VEB_max(veb))

# start = VEB_min(veb)
# while start is not None:
# print(start, lookup(veb, start))
# start = VEB_successor(veb, start)

# if isMember(veb, 2):
# delete(veb, 2)

# print(isMember(veb, 2))
# print(VEB_predecessor(veb, 4), VEB_successor(veb, 1))
