#!/usr/bin/env python

import time

def main():
    i = 1
    while i > 0:
        print ('Working... {}'.format(i))
        time.sleep(1)
        i += 1

if __name__ == '__main__':
    main()
