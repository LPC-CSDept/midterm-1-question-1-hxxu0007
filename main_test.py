import main
import io
import sys
import re
import math


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 5 20 0 40 45 50 55 9 10\n'
    datastr = '1\n2\n17\n9\n15\n2\n4\n1\n10\n12'
    sys.stdin = io.StringIO(datastr)

    evencnt = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    print(f'Your output is {evencnt}')
    assert evencnt == 2


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10 5 20 0 40 45 50 55 9 10\n'
    datastr = '2\n4\n6\n5\n8\n10\n11\n12\n14\n20'
    sys.stdin = io.StringIO(datastr)

    evencnt = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    print(f'Your output is {evencnt}')
    assert evencnt == 3

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '2\n4\n6\n5\n8\n10\n11\n12\n14\n20'
    datastr = '1\n4\n6\n5\n8\n10\n11\n12\n14\n21'
    sys.stdin = io.StringIO(datastr)

    evencnt = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    print(f'Your output is {evencnt}')
    assert evencnt == 3

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)


def test_main_4():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '2\n4\n6\n4\n8\n10\n10\n12\n14\n20'
    sys.stdin = io.StringIO(datastr)

    evencnt = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    print(f'Your output is {evencnt}')
    assert evencnt == 1

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_5():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '1\n3\n4\n7\n9\n1\n3\n4\n7\n9'
    sys.stdin = io.StringIO(datastr)

    evencnt = main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)
    print(f'Your output is {evencnt}')
    assert evencnt == 0
