def main():
    name = input()
    if name.isalpha():
        print('Hello, ', name)
    else:
        main()


if __name__ == '__main__':
    main()
