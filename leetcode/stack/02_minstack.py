class MinStack:

    def __init__(self):
        # maintain two stacks, one for normal operations, one for returning min value
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)

        # check if the val is greater than last val in MinStack, also if empty
        if self.minstack and val > self.minstack[-1]:
            # since minstack val is less, update val and append
            val = self.minstack[-1]
        else:
            val = val
        self.minstack.append(val)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getmin(self):
        return self.minstack[-1]


example_minstack = MinStack()
example_minstack.push(5)
example_minstack.push(1)
example_minstack.push(-1)
print(example_minstack.getmin())
example_minstack.push(2)
print(example_minstack.getmin())
example_minstack.pop()
print(example_minstack.getmin())
print(example_minstack.top())
