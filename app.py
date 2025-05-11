from flask import Flask, render_template, request

app = Flask(__name__)

# Переменные для хранения состояния калькулятора
current_input = '0'
current_expression = ''
last_result = None
waiting_for_operand = False

@app.route('/', methods=['GET', 'POST'])
def calculator():
    global current_input, current_expression, last_result, waiting_for_operand

    if request.method == 'POST':
        action = request.form.get('action')  # Какую кнопку нажали

        # Очистка всего
        if action == 'clear':
            current_input = '0'
            current_expression = ''
            last_result = None
            waiting_for_operand = False

        # Удаление последнего символа
        elif action == 'backspace':
            if len(current_input) > 1:
                current_input = current_input[:-1]
            else:
                current_input = '0'

        # Добавление числа
        elif action in '0123456789':
            if current_input == '0' or waiting_for_operand:
                current_input = action
                waiting_for_operand = False
            else:
                current_input += action

        # Добавление точки
        elif action == 'decimal':
            if waiting_for_operand:
                current_input = '0.'
                waiting_for_operand = False
            elif '.' not in current_input:
                current_input += '.'

        # Добавление оператора
        elif action in ['+', '−', '×', '÷', '%']:
            if last_result is not None:
                current_expression = f"{last_result} {action} "
                waiting_for_operand = True
            else:
                current_expression = f"{current_input} {action} "
                last_result = float(current_input) if '.' in current_input else int(current_input)
                waiting_for_operand = True

        # Вычисление результата
        elif action == 'equals':
            if last_result is None or waiting_for_operand:
                pass
            else:
                expression = current_expression + current_input
                try:
                    calc_expression = expression.replace('×', '*').replace('÷', '/').replace('−', '-')
                    result = eval(calc_expression)
                    current_expression = expression + ' ='
                    current_input = str(result)
                    last_result = result
                    waiting_for_operand = True
                except:
                    current_input = 'Ошибка'
                    current_expression = ''
                    last_result = None
                    waiting_for_operand = True

    return render_template('index.html', display=current_input, expression=current_expression)

if __name__ == '__main__':
    app.run(debug=True)