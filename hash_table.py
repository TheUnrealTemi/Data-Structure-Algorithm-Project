class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        
    def _hash(self, key):
        return key % self.size
        
    def insert(self, package):
        bucket_index = self._hash(package.id)
        bucket = self.table[bucket_index]
        
        for i in range(len(bucket)):
            if bucket[i].id == package.id:
                bucket[i] = package
                return
        
        bucket.append(package)
                     
    def lookup(self, id):
        bucket_index = self._hash(id)
        bucket = self.table[bucket_index]
        
        for package in bucket:
            if package.id == id:
                return package
        return None
    
    def __str__(self):
        output = []
        for i in range(len(self.table)):
            bucket = self.table[i]
            bucket_str = ", ".join([f"ID:{pkg.id}" for pkg in bucket])
            output.append(f"Bucket {i}: [{bucket_str}]")
        return "\n".join(output)
            
    def __repr__(self):
        return f"HashTable(size={self.size}, table={self.table})"