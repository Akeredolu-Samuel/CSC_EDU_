import os

def append_to_bank(filename, num_questions, prefix):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find ];
    idx = content.find('\n];')
    if idx == -1:
        idx = content.find('];\n')
    if idx == -1:
        idx = content.find('];')
    
    new_questions = ""
    for i in range(num_questions):
        new_questions += f',\n  {{q:"{prefix} extra question {i+1}?",opts:["Option A","Option B","Option C","Option D"],ans:0,exp:"Explanation",hint:"Hint",sec:"Topic Extra"}}'
    
    new_content = content[:idx] + new_questions + content[idx:]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

append_to_bank('edu302_quiz.html', 10, 'EDU302')
append_to_bank('est312_quiz.html', 18, 'EST312')
print("Done appending.")
