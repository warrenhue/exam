class FlattenIterator:
    def __init__(self, nested_list):
        self.nested = nested_list

    def __iter__(self):
        stack = [self.nested]
        while stack:
            current = stack.pop()
            if isinstance(current, list):
                stack.extend(reversed(current))
            else:
                yield current


nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)

for num in flat:
    print(num)