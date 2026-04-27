from consistent_Hashing import *
from LRU_Production import *

def test_remap_rate():
    ring = ConsistentHashRing(replicas=150)
    
    # Add 4 nodes
    for n in ['A', 'B', 'C', 'D']:
        ring.add_node(n)
    
    # Map 10,000 keys
    keys = [f"key:{i}" for i in range(10000)]
    before = {k: ring.get_node(k) for k in keys}
    
    # Add 5th node
    ring.add_node('E')
    after = {k: ring.get_node(k) for k in keys}
    
    # Count changed assignments
    changed = sum(1 for k in keys if before[k] != after[k])
    print(f"Keys remapped: {changed}/10000 ({changed/100:.2f}%)")
    # Expect ~20% (1/5 of keys), often less with good virtual node distribution

test_remap_rate()