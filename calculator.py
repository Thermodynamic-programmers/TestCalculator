# Этот код не используется на GitHub Pages, так как требуется серверная часть
# Он здесь для информации, если вы решите добавить серверную поддержку (например, через Flask)

class Calculator:
    def __init__(self):
        self.current_input = '0'  # Что сейчас на экране
        self.current_expression = ''  # Что мы считаем
        self.last_result = None  # Последний результат
        self.waiting_for_operand = False  # Ждем следующее число

    def update_display(self):
        # Метод для отображения результата (нуждается в DOM, чего нет без JS)
        pass

    def append_number(self, number):
        if self.current_input == '0' or self.waiting_for_operand:
            self.current_input = number
            self.waiting_for_operand = False
        else:
            self.current_input += number

    def append_decimal(self):
        if self.waiting_for_operand:
            self.current_input = '0.'
            self.waiting_for_operand = False
        elif '.' not in self.current_input:
            self.current_input += '.'

    def append_operator(self, operator):
        if self.last_result is not None:
            self.current_expression = f"{self.last_result} {operator} "
            self.waiting_for_operand = True
        else:
            self.current_expression = f"{self.current_input} {operator} "
            self.last_result = float(self.current_input) if '.' in self.current_input else int(self.current_input)
            self.waiting_for_operand = True

    def calculate(self):
        if self.last_result is None or self.waiting_for_operand:
            return
        expression = self.current_expression + self.current_input
        try:
            result = eval(expression.replace('×', '*').replace('÷', '/').replace('−', '-'))
            self.current_expression = expression + ' ='
            self.current_input = str(result)
            self.last_result = result
            self.waiting_for_operand = True
        except:
            self.current_input = 'Ошибка'
            self.current_expression = ''
            self.last_result = None
            self.waiting_for_operand = True

    def clear_all(self):
        self.current_input = '0'
        self.current_expression = ''
        self.last_result = None
        self.waiting_for_operand = False

    def backspace(self):
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = '0'