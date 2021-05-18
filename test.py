from stack import Stack

class Test:
    if __name__ == '__main__':
        fifo = Stack()
        
        fifo.push(33)
        fifo.push(12)
        fifo.push('Maria')
        fifo.push(69)
        fifo.push(True)
        fifo.push(88)
        print(fifo)
        print('##########')
        fifo.pop()
        fifo.pop()
        print(fifo)
        print('##########')
        fifo.peek()
        print(fifo)