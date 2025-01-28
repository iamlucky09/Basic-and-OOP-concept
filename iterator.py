# itrerator in python
# type vaneko duita huncha -1.__iter__
# arko chai -2.__next__
# 1.__iter__->returns the iter object itself
# 2.__next__->returns the next value from the iterator object
class evennum:
    def __init__(self,max_value):
        self.max_value = max_value
        self.current_value = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_value > self.max_value:
          raise StopIteration

        else:
            result=self.current_value
            self.current_value += 2
            return result
        
eve=evennum(10)
for num in eve:
    print(num)

