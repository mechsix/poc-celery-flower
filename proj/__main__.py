import sys
from proj.worker import task1, task2

if __name__ == '__main__':
    target = sys.argv[1]

    if target == 'task1':
        print('run task1')
        task1.delay('mohoho')
    elif target == 'task2':
        print('run task2')
        task2.delay()
    else:
        print('unknown task')
