class QueueWithTwoStacks:
    def __init__(self, length):
        # Enqueue
        self.enqueue_stack = []
        # Dequeue
        self.dequeue_stack = []
        # Max size
        self.len = length

    def enqueue(self, value):
        if len(self.enqueue_stack) < self.len:
            self.enqueue_stack.append(value)
        else:
            # memory가 다 사용되면 dequeue_stack의 메모리를 사용해서 lifo를 유지합니다.
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
            self.enqueue_stack.append(value)

    # dequeue는 enqueue_stack에서 역순으로 pop and append(enqueue)
    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(
                    self.enqueue_stack.pop()
                )  # list의 pop은 overload 돼있습니다. return type => any
        # 이렇게 하면 First-in이 first-out 됩니다.
        if self.dequeue_stack:
            return self.dequeue_stack.pop()
        else:
            raise IndexError("Empty queue")

    def is_empty(self):
        return not (self.enqueue_stack or self.dequeue_stack)

    def __str__(self):
        sample_string = "Queue with Two Stacks. Global class"
        return "{}. The queue itself has {} maximum elements inside of it".format(
            sample_string, str(self.len)
        )
