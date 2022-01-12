# This is a sample Python script.
import sys
import sqlparse

if __name__ == '__main__':
    data = sys.stdin.readlines()
    print(sqlparse.format(*data, reindent=True, keyword_case='upper'))


