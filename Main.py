# -*- coding: utf-8 -*-
from timer0 import timer
import timeseqs

def timer0_test():
    print(timer(pow, 2, 1000))
    print(timer(str.upper, 'spam'))

if __name__ == '__main__':
    timeseqs.run()
    #timer0_test()
