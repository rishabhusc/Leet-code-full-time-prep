'''
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

'''


import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map=collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((value,timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values=self.map[key]
        left=0
        right=len(values)-1
        while left<right:
            mid=int((left+right+1)/2)
            val,time=values[mid]
            if time>timestamp:
                right=mid-1
            else:
                left=mid
        return values[left][0] if values[left][1]<=timestamp else None

'''
["TimeMap","set","get","get","set","get","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
'''

obj = TimeMap()
obj.set("foo","bar",1)
print(obj.get("foo",1))
print(obj.get("foo",3))
obj.set("foo","bar2",4)
print(obj.get("foo",4))
print(obj.get("foo",5))


