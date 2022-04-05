class CustomSet:
    
    def __init__(self, size = 1000):
        self.size = size
        self.values = [None for i in range(size)]
        self.value_count = 0
    
    '''
    Return the hash of a value.
    '''
    def hash(self, value):
        hash = (value % self.size)
        return hash

    '''
    If there is no conflict, add value to set at the index of it's hash. Return false if
    there is a conflict, or value is already in the set.
    '''
    def add(self, value):
        pass
    
    '''
    If the set contains value, return true. If not, return false.
    '''
    def contains(self, value):
        pass

    '''
    Return the value at the same hash as the passed value.
    '''
    def val_at_hash(self, value):
        return self.values[self.hash(value)]

    '''
    Return true if index of value's hash is has been set, otherwise the function returns false.
    '''
    def conflict(self, value):
        if self.val_at_hash(value) is not None:
            return True
        return False


#Test Case:
my_set = CustomSet()

for i in range(0, 6, 2):
    my_set.add(i)

for i in range(7):
    print(my_set.contains(i))
