class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res


time_map = TimeMap()
# time_map.set("foo", "bar", 1)
# print(time_map.get("foo", 1))  # bar
# print(time_map.get("foo", 3))  # bar
# time_map.set("foo", "bar2", 4)
# print(time_map.get("foo", 4))  # bar2
# print(time_map.get("foo", 5))  # bar2


# time_map.set("alice", "happy", 1)
# print(time_map.get("alice", 1))  # happy
# time_map.set("alice", "sad", 3)
# print(time_map.get("alice", 3))  # sad

# print(time_map.set("key1", "value1", 10))
# print(time_map.get("key1", 1))
# print(time_map.get("key1", 10))
# print(time_map.get("key1", 11))

print("TimeMap")
time_map = TimeMap()

print("set", ["test", "one", 10])
time_map.set("test", "one", 10)

print("set", ["test", "two", 20])
time_map.set("test", "two", 20)

print("set", ["test", "three", 30])
time_map.set("test", "three", 30)

print("get", ["test", 15])
print(time_map.get("test", 15))

print("get", ["test", 25])
print(time_map.get("test", 25))

print("get", ["test", 35])
print(time_map.get("test", 35))

# [null,null,null,null,"one","two","three"]
