"""
To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database)
and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of
times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs
at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?


"""


input_file = __file__.replace('.py', '.txt')


def validate_password1(min, max, letter, password):
    count = len([l for l in password if l == letter])
    return min <= count <= max

def validate_password2(pos1, pos2, letter, password):
    # xor
    return (password[pos1-1] == letter) != (password[pos2-1] == letter)

def test():
    assert validate_password1(1, 3, 'a', 'abcde')
    assert False == validate_password1(1, 3, 'b', 'cdefg')
    assert validate_password1(2, 9, 'c', 'ccccccccc')

    assert validate_password2(1, 3, 'a', 'abcde')
    assert False == validate_password2(1, 3, 'b', 'cdefg')
    assert False == validate_password2(2, 9, 'c', 'ccccccccc')


def run():
    total1 = 0
    total2 = 0
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()

            ranges, letter, password = line.replace(':','').split(' ')
            min, max = ranges.split('-')

            if validate_password1(int(min), int(max), letter, password):
                total1 += 1

            if validate_password2(int(min), int(max), letter, password):
                total2 += 1

    print(total1)
    print(total2)


if __name__ == '__main__':
    test()
    run()
