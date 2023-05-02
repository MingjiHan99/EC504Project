 #!/usr/bin/env python3
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


def VEB_min(helper):
    if helper.min == -1:
        return -1
    else:
        return helper.min


def VEB_max(helper):
    if helper.max == -1:
        return -1
    else:
        return helper.max


def insert(helper, key, value):
    if helper.min == -1:
        helper.min = key
        helper.max = key
        helper.minvalue = value
        helper.maxvalue = value
    else:
        if key < helper.min:
            helper.min, key = key, helper.min
            helper.minvalue, value = value, helper.minvalue
        if helper.size > 2:
            if VEB_min(helper.clusters[helper.high(key)]) == -1:
                insert(helper.summary, helper.high(key), value)
                helper.clusters[helper.high(key)].min = helper.low(key)
                helper.clusters[helper.high(key)].max = helper.low(key)
                helper.clusters[helper.high(key)].minvalue = value
                helper.clusters[helper.high(key)].maxvalue = value
            else:
                insert(helper.clusters[helper.high(key)], helper.low(key), value)
        if key > helper.max:
            helper.max = key
            helper.maxvalue = value


def isMember(helper, key):
    if helper.size < key or helper.size == 2:
        return False
    if helper.min == key or helper.max == key:
        return True
    return isMember(helper.clusters[helper.high(key)], helper.low(key))


def lookup(helper, key):
    if isMember(helper, key):
        if helper.min == key:
            return helper.minvalue
        elif helper.max == key:
            return helper.maxvalue
        return lookup(helper.clusters[helper.high(key)], helper.low(key))


def VEB_successor(helper, x):
    if helper.size == 2:
        if x == 0 and helper.max == 1:
            return 1
        else:
            return None
    elif helper.min is not None and x < helper.min:
        return helper.min
    else:
        max_in_cluster = VEB_max(helper.clusters[helper.high(x)])
        if max_in_cluster is not None and helper.low(x) < max_in_cluster:
            offset = VEB_successor(helper.clusters[helper.high(x)], helper.low(x))
            return helper.generate_index(helper.high(x), offset)
        else:
            succ_cluster = VEB_successor(helper.summary, helper.high(x))
            if succ_cluster is None:
                return None
            else:
                offset = VEB_min(helper.clusters[succ_cluster])
                return helper.generate_index(succ_cluster, offset)


# Function to find the predecessor of the given key
def VEB_predecessor(helper, x):
    if helper.size == 2:
        if x == 1 and helper.min == 0:
            return 0
        else:
            return None
    elif helper.max is not None and x > helper.max:
        return helper.max
    else:
        min_in_cluster = VEB_min(helper.clusters[helper.high(x)])
        if min_in_cluster is not None and helper.low(x) > min_in_cluster:
            offset = VEB_predecessor(helper.clusters[helper.high(x)], helper.low(x))
            return helper.generate_index(helper.high(x), offset)
        else:
            pred_cluster = VEB_predecessor(helper.summary, helper.high(x))
            if pred_cluster is None:
                if helper.min is not None and x > helper.min:
                    return helper.min
                else:
                    return None
            else:
                offset = VEB_max(helper.clusters[pred_cluster])
                return helper.generate_index(pred_cluster, offset)


def VEB_delete(helper, key):
    if helper.max == helper.min:
        helper.min = -1
        helper.max = -1
    elif helper.size == 2:
        if key == 0:
            helper.min = 1
        else:
            helper.min = 0
        helper.max = helper.min
    else:
        if key == helper.min:
            first_cluster = VEB_min(helper.summary)
            key = helper.generate_index(
                first_cluster, VEB_min(helper.clusters[first_cluster]))
            helper.min = key
        VEB_delete(helper.clusters[helper.high(key)], helper.low(key))
        if VEB_min(helper.clusters[helper.high(key)]) == -1:
            VEB_delete(helper.summary, helper.high(key))
            if key == helper.max:
                max_insummary = VEB_max(helper.summary)
                if max_insummary == -1:
                    helper.max = helper.min
                else:
                    helper.max = helper.generate_index(
                        max_insummary, VEB_max(helper.clusters[max_insummary]))
        elif key == helper.max:
            helper.max = helper.generate_index(helper.high(
                key), VEB_max(helper.clusters[helper.high(key)]))


n=4
while n<800001:

    veb = VEB(n)
# Inserting keys
    for i in range(n):
        insert(veb, i, "12")

    start_time = time.time()
    for i in range(1000000):
        lookup(veb, i%n)
    end_time = time.time()
    print(math.log(n)," ",  end_time - start_time)
    n = n*n
# print(isMember(veb, 2))
# print(VEB_predecessor(veb, 4), VEB_successor(veb, 1))
# print(VEB_min(veb), VEB_max(veb))

# start = VEB_min(veb)
# while start is not None:
# print(start, lookup(veb, start))
# start = VEB_successor(veb, start)

# if isMember(veb, 2):
# VEB_delete(veb, 2)

# print(isMember(veb, 2))
# print(VEB_predecessor(veb, 4), VEB_successor(veb, 1))
