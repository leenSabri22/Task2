class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


feed_items = ["post1", "ad1", "suggested1", "post2"]


test_iter = Iterator(feed_items)

for letter in test_iter:
    print(letter)
