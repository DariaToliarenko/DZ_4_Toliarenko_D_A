import re

def calculate(expression):
    """Выполняет вычисление арифметического выражения."""
    try:
        # Удаляем все пробелы из выражения
        expression = expression.replace(" ", "")

        # Проверяем на наличие некорректных символов
        if not re.match(r'^[\d\s+*/-]+$', expression):
            raise ValueError("Недопустимые символы в выражении")

        # Выполняем вычисление
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Деление на ноль")
    except Exception as e:
        raise e

def log_error(line_number, error_message):
    """Записывает сообщение об ошибке в app.log."""
    with open("app.log", "a") as log_file:
        log_file.write(f"Ошибка на строке {line_number}: {error_message}\n")

def main():
    # Открываем файл с выражениями
    with open("expressions.txt", "r") as file:
        lines = file.readlines()
    
    for line_number, expression in enumerate(lines, start=1):
        expression = expression.strip()
        
        try:
            if expression:  # Пропускаем пустые строки
                result = calculate(expression)
                print(f"{expression} = {result}")
        except Exception as e:
            print(f"Ошибка на строке {line_number}: {e}")
            log_error(line_number, str(e))

if __name__ == "__main__":
    main()