from datetime import datetime


def logger(path=''):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            file_path = str(path) + 'log.txt'
            print('Logging in ', file_path)
            with open(file_path, "a", encoding="utf-8") as f:
                f.write('дата и время вызова: ' + str(datetime.now()) + '\n')
                f.write('имя функции: ' + str(old_function.__name__) + '\n')
                f.write('аргументы: '+ str(args) + str(kwargs) +'\n')
                f.write('возвращаемое значение: ' + str(result) + '\n')
                f.write('---------------------------' + '\n')
            return result
        return new_function
    return _logger

