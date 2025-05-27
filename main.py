```python
def calculate(num1, num2, operation):
    # Приводим входные данные к числам
    num1 = float(num1)
    num2 = float(num2)
    
    # Выполняем операцию в зависимости от выбора
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2
    return "Неизвестная операция"
```