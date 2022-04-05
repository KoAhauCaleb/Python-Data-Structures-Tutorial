class CustomSet:
    
    def __init__(self, size = 1000):
        self.size = size
        self.values = [None for i in range(size)]
        self.value_count = 0
    
    '''
    Return the hash of a value.
    '''
    def hash(self, value):
        pass

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
        pass

    '''
    Return true if index of value's hash is has been set, otherwise the function returns false.
    '''
    def conflict(self, value):
        pass