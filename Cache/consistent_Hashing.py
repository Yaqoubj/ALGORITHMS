import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self,replicas=150):
        self.replicas = replicas
        self.ring = {}
        self.sorted_hashes = []

    def _hash(self,key):
            #md5 understand bytes only so we turn key to string then to bytes
            hex_str = hashlib.md5(str(key).encode("utf-8")).hexdigest()
            # transform the key to a number
            big_int = int(hex_str,16)
            return big_int % (2**32)
    
    def add_node(self,node):
        for i in range(self.replicas):
             virtual = f"{node}"#"{i}"
             pos = self._hash(virtual)
             self.ring[pos] = node
             self.sorted_hashes.append(pos)
        self.sorted_hashes.sort()

    def remove_node(self,node):
         to_remove = []
         for i in range(self.replicas):
              virtual = f"{node}"#"{i}"
              pos = self._hash(virtual)
              to_remove.append(pos)
         for pos in to_remove:
              del self.ring[pos]
              self.sorted_hashes.remove(pos)
    def get_node(self,key):
        if not self.sorted_hashes:
              return None
        pos = self._hash(key)
        idx = bisect.bisect_right(self.sorted_hashes, pos)
        if idx == len(self.sorted_hashes):
            idx =0
        return self.ring[self.sorted_hashes[idx]]