class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = []
        self.flatten(nestedList)
        self.size = len(self.flattened)
        self.index = -1
 
    def flatten(self, lst):
        if type(lst) == list:
            for i in lst:
                self.flatten(i)
        elif lst.isInteger():
            self.flattened.append(lst.getInteger())
        else:
            self.flatten(lst.getList())
 
    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index]
    
    def hasNext(self) -> bool:
        return self.index != self.size - 1
