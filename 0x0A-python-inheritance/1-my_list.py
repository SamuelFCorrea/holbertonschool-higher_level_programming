#!/usr/bin/python3

'''Class MyList'''


class MyList(list):
    '''print the  list sorted'''
    def print_sorted(self):
        '''Print the list sorted'''
        print(sorted(self))
