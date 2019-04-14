def repl():
    try:
        while True:
            line = input('>>> ')
            command, rest = parse(line)
            execute(command, rest)
    except KeyboardInterrupt:
        pass
    finally:
        print('Bye')
        

def parse(line):
    tokens = line.split(None, 1)

    try:
        command = tokens[0].lower()
    except IndexError:
        command = ''

    try:
        rest = tokens[1]
    except IndexError:
        rest = ''    
        
    return command, rest

def execute(command, rest):
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

repl()