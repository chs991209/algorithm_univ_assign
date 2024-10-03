# import sys
#
# sys.path.append(r'C:\Users\chs99\PycharmProjects\algorithm-assignments')


from queue_with_two_stacks import QueueWithTwoStacks


class Josephus(object):
    def __init__(self, input_sequence_data):
        self._input_sequence_data = input_sequence_data

    def josephus_algorithm_death_sequence_output(self, n, k):
        sequence_queue = QueueWithTwoStacks(n)
        for el in self._input_sequence_data:
            sequence_queue.enqueue(el)

        elimination_sequence_result = []

        while not sequence_queue.is_empty():

            # k - 1 번 element까지 dequeue후에 해당 원소를 enqueue_stack(선입순 stack)에 enqueue하고,
            # dequeue_stack에서 (후입순 stack) pop해서 선입순으로 k 번째를 날려서 result에 넣습니다. (k번째 원소를 지속적으로 dequeue로 pop하고 result로 이동)
            # => 지속적으로 k번째 element만 queue data에서 삭제되고 result로 이동됩니다.
            for _ in range(0, k - 1):
                sequence_queue.enqueue(sequence_queue.dequeue())

            # 여기가 k번째 element를 dequeue해서 result로 이동하는 부분
            elimination_sequence_result.append(sequence_queue.dequeue())

        # result = sequence_queue.dequeue()

        return elimination_sequence_result

    def josephus_algorithm_survivor_output(self, n, k):
        sequence_queue = QueueWithTwoStacks(n)
        for el in self._input_sequence_data:
            sequence_queue.enqueue(el)

        elimination_sequence_result = []

        while not sequence_queue.is_empty():

            # k - 1 번 element까지 dequeue후에 해당 원소를 enqueue_stack(선입순 stack)에 enqueue하고,
            # dequeue_stack에서 (후입순 stack) pop해서 선입순으로 k 번째를 날려서 result에 넣습니다. (k번째 원소를 지속적으로 dequeue로 pop하고 result로 이동)
            # => 지속적으로 k번째 element만 queue data에서 삭제되고 result로 이동됩니다.
            for _ in range(0, k - 1):
                sequence_queue.enqueue(sequence_queue.dequeue())

            # 여기가 k번째 element를 dequeue해서 result로 이동하는 부분
            elimination_sequence_result.append(sequence_queue.dequeue())

        return elimination_sequence_result.pop()
