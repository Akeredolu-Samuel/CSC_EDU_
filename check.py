import re

def count_q(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return len(re.findall(r'\{q:', content))

print("EDU302:", count_q('edu302_quiz.html'))
print("EST312:", count_q('est312_quiz.html'))
