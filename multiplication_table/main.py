# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def multiplication_table():
    for i in range(11, 111):

        a = int(i / 10)
        b = int(i % 10)

        if b == 0:
            yield (i - 10, '\n')
        else:
            yield (a * b, '')


for i, o in multiplication_table():
    print(i, ' ', end=o)

# 0 --0/9 +1 ==1
# 1 -- int.floor(1/9) 1 + 2
# 2    2/9 +2
#
# 28 (28/9) (3) +1 {4}
# 32 (32/9)
#
# 21= {3} * 7
#
# 29 = 2* 9 = 18 -- 19
# 31 = 3 * 1 = 3 --  3
#
# 11-|-111
#
#
# 1 2 3 4 5 6 7 8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
# 2 4 6 8 10 12 14 16 18 20 3  6  9  12 15 18 21 24 27 30 4  8  12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
