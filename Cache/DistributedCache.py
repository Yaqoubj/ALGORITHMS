from consistent_Hashing import *
from LRU_Production import *

class DistributedCahce:
    def __init__(self,capacity_per_node):
        self.ring = ConsistentHashRing(replicas=150)
        self.caches= {}
        self.capacity_per_node = capacity_per_node
    
    def add_server(self,node_name):
        self.ring.add_node(node_name)
        self.caches[node_name] = LRUCache(self.capacity_per_node)
    
    def remove_server(self,node_name):
        self.ring.remove_node(node_name)
        del self.caches[node_name]
    
    def get(self,key):

        node = self.ring.get_node(key)
        if node is None:
            raise RuntimeError("No servers available")
        return self.caches[node].get(key)
    
    def put(self,key,value):
        node = self.ring.get_node(key)
        if node is None:
            return None
        self.caches[node].put(key,value)