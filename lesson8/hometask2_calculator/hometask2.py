import logging

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8",
)

input_file_path = 'input'
output_file_path = 'output'

class UnsupportedOperationError(Exception):
    pass

with open(input_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
expressions = [line.strip().split() for line in lines]
lines = [line.strip() + " = " for line in lines]
for i in range(len(expressions)):
    try:
        first_operand = int(expressions[i][0])
        operator = expressions[i][1]
        second_operand = int(expressions[i][2])
        if operator == '+':
            result = first_operand + second_operand
        elif operator == '-':
            result = first_operand - second_operand
        elif operator == '*':
            result = first_operand * second_operand
        elif operator == '/':
            result = first_operand / second_operand
        else:
            raise UnsupportedOperationError
        lines[i] += str(result) + "\n"
    except ZeroDivisionError:
        lines[i] += "Ошибка: деление на ноль\n"
        logging.error(f"in line {i + 1}: Деление на ноль")
    except (ValueError, TypeError):
        lines[i] += "Ошибка: некорректные данные\n"
        logging.error(f"in line {i + 1}: Некорректные данные")
    except UnsupportedOperationError:
        lines[i] += "Ошибка: оператор в данном выражении не обрабатывается программой\n"
        logging.error(f"in line {i + 1}: Оператор в данном выражении не обрабатывается программой")
    except:
        lines[i] += "Неизвестная ошибка\n"
        logging.error(f"in line {i + 1}: Неизвестная ошибка")
with open(output_file_path, "w", encoding="utf-8") as file:
    file.writelines(lines)
