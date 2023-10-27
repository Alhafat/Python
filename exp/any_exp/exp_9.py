def main():
    name = input('Yours name: ')
    if name.isalpha():
        print('Hello, ', name)
    else:
        main()


if __name__ == '__main__':
    main()
