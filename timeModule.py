# -*- coding: utf-8 -*-
import timeit

if __name__ == '__main__':
    print(str(min(timeit.repeat(stmt = '[x ** 2 for x in range(1000)]',
                      number = 1000, repeat = 5))))
    print(str(timeit.timeit(stmt = '[x ** 2 for x in range(1000)]', number = 1000)))