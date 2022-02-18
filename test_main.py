import os


def run_tests():
    print('RUNNING ALL TESTS...')
    os.system('python3 -m unittest tests/test*.py -v')


if __name__ == '__main__':
    run_tests()
