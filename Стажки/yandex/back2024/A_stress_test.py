import re

def python_format_text(w):
    import re

    words = re.findall(r'\w+|\s+|,', w)

    max_word_length = max(len(word.rstrip(',')) for word in words if word.strip() and word != ',')
    max_len = max_word_length * 3

    lines = []
    current_line = ''
    current_length = 0

    for word in words:
        if word.isspace():
            continue

        if word == ',':
            current_line = current_line.rstrip() + ','
            current_length = len(current_line)
            continue
        
        word_length = len(word)

        if current_length + word_length + 1 > max_len:
            lines.append(current_line.strip())
            current_line = word
            current_length = word_length
        else:
            if current_line:
                current_line += ' '
                current_length += 1

            current_line += word
            current_length += word_length
        
        if word.endswith(',') and current_length < max_len:
            current_line += ' '
            current_length += 1

    if current_line:
        lines.append(current_line.strip())
    
    return lines

def run_stress_tests():
    import subprocess
    import random
    import string

    test_cases = [
        # Тест с длинными и короткими словами
        "a " * 50 + "longword" * 10 + " shortword " * 20 + "end",
        # Тест с большим количеством запятых
        ",".join(["word"] * 50) + ",end",
        # Тест с случайными длинными словами
        " ".join(["word" * i for i in range(1, 50)]),
        # Тест с запятыми и пробелами
        "word, " * 25 + " end",
        # Тест с комбинацией всех случаев
        "a, b, c, longword, shortword, " * 10 + "end",
    ]

    for _ in range(50):  # Добавляем 5 случайных тестов
        random_length = random.randint(1, 20)
        random_text = ''.join(random.choices(string.ascii_lowercase + ', ', k=random_length))
        random_text = re.sub(r'(?<!\w),', '', random_text)  # Удаление запятых, не следующих за словом
        random_text = re.sub(r'\s+', ' ', random_text)  # Замена множественных пробелов одним пробелом
        if random_text[-1] == ' ':
            random_text = random_text[:-1]  # Удаление пробела в конце строки
        test_cases.append(random_text)

    for idx, input_text in enumerate(test_cases):
        # Call C++ program
        process = subprocess.Popen(['./format_text'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=input_text.encode())

        result_cpp = stdout.decode().strip().split('\n')
        result_py = python_format_text(input_text)

        assert result_cpp == result_py, f"Mismatch found on test {idx + 1}!\nInput: {input_text}\nC++ Output: {result_cpp}\nPython Output: {result_py}"

    print("All tests passed!")

if __name__ == "__main__":
    run_stress_tests()
