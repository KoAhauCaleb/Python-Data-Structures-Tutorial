class CustomSet:
    
    def __init__(self, size = 1000):
        self.size = size
        self.values = [None for i in range(size)]
        self.value_count = 0

    def hash(self, value):
        hash = (value % self.size)
        return hash

    def add(self, value):
        if not self.conflict(value):
            self.values[self.hash(value)] = value
            self.value_count += 1
            return True
        return False

    def contains(self, value):
        if self.conflicting_val(value) == value:
            return True
        return False

    def conflicting_val(self, value):
        return self.values[self.hash(value)]

    def conflict(self, value):
        if self.conflicting_val(value) is not None:
            return True
        return False

#Test Case:
my_set = CustomSet()

for i in range(0, 6, 2):
    my_set.add(i)

for i in range(7):
    print(my_set.contains(i)) 

   
'''
Expected Output:
True
False
True
False
True
False
False
'''