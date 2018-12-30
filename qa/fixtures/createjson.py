import json
from collections import defaultdict

input_types_dict = {}

# create inputtype.json
inputtype_content = []
with open ('inputtype.txt', encoding='utf8') as file:
    for row in file:
        inputtype_content.append(row)

inputtype_json_content  = []
inputtype_json_template = {'model':'qa.InputType', 'pk':0, 'fields':{}}
for inputtype in inputtype_content:
    x = inputtype.split()
    
    input_types_dict[x[1]] = int(x[0])
    
    fields = {'id'  : int(x[0]),
              'name': x[1]}
    inputtype_json_template['pk']     = int(x[0])
    inputtype_json_template['fields'] = fields
    inputtype_json_content.append(inputtype_json_template.copy())

with open("inputtype.json", "w") as file:
    json.dump(inputtype_json_content, file)

# create question.json and answer.json
QnA_content = []
with open ('QnA.txt', encoding='utf8') as file:
    for row in file:
        QnA_content.append(row)

question_json_content  = []
question_id            = 1
question_json_template = {'model':'qa.Question', 'pk':0, 'fields':{}}
answer_json_content    = []
answer_id              = 1
answer_json_template   = {'model':'qa.Answer', 'pk':0, 'fields':{}}
i = 0
while i < len(QnA_content):
    question_text = QnA_content[i].rstrip()
    if not question_text:
        break
    i += 1
    input_type, nb_of_answers = QnA_content[i].split()
    input_type    = input_types_dict[input_type]
    nb_of_answers = int(nb_of_answers)
    fields = {'id'        :question_id,
              'input_type':input_type,
              'text'      :question_text}
    question_json_template['pk']     = question_id
    question_json_template['fields'] = fields
    question_json_content.append(question_json_template.copy())
    i += 1

    i_max = i + nb_of_answers
    while i < i_max:
        fields = {'id'         :answer_id,
                  'question_id':question_id,
                  'text'       :QnA_content[i].rstrip()}
        answer_json_template['pk']     = answer_id
        answer_json_template['fields'] = fields
        answer_json_content.append(answer_json_template.copy())
        answer_id += 1
        i += 1
    question_id += 1
    i += 1

with open("question.json", "w") as file:
    json.dump(question_json_content, file)

with open("answer.json", "w") as file:
    json.dump(answer_json_content, file)
