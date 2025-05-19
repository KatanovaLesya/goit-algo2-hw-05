import hashlib
import math
import bitarray


class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item: str):
        item_bytes = item.encode('utf-8')
        hash1 = int(hashlib.sha256(item_bytes).hexdigest(), 16)
        hash2 = int(hashlib.md5(item_bytes).hexdigest(), 16)
        for i in range(self.num_hashes):
            yield (hash1 + i * hash2) % self.size

    def add(self, item: str):
        if not isinstance(item, str) or not item.strip():
            return  
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1

    def __contains__(self, item: str):
        if not isinstance(item, str) or not item.strip():
            return False
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))
