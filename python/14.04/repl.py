def repl():
    try:
        while True:
            line = input('>>> ')
            tokens = line.split(None, 1)

            try:
                command = tokens[0].lower()
            except IndexError:
                command = ''

            try:
                rest = tokens[1]
            except IndexError:
                rest = ''

            if command == 'eval':
                try:
                    result = eval(rest)
                except Exception as e:
                    print(type(e).__name__)
                else:
                    print(result)
            elif command == 'exit':
                raise KeyboardInterrupt
            elif command == '':
                pass
            else:
                print('Invalid command.')
    except KeyboardInterrupt:
        pass
    finally:
        print('Bye')