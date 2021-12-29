from sequence import syracuse_sequence, syracuse_max


def main():
    print('Write Number')
    number = int(input())
    print('Sequence - 1 or Max - 2')
    com = int(input())
    if com == 1:
        print(syracuse_sequence(number))
    else:
        print(syracuse_max(number))


if __name__ == '__main__':
    main()
