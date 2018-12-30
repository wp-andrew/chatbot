# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer

from qa.models import Question, Answer

INTRODUCTION = 'Hello, I am going to ask you few questions that will help me know you better.'

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.scope['session']['answer'] = []
        self.scope['session']['question_id'] = 1
        
        self.send(text_data=json.dumps({
            'user_type'   : 'Bot',
            'message_type': 'information',
            'message'     : INTRODUCTION,
        }))
        
        question_id = self.scope['session']['question_id']
        question_qs = Question.objects.get(pk=question_id)
        answer_qs   = Answer.objects.filter(question_id=question_id)
        
        self.send(text_data=json.dumps({
            'user_type'   : 'Bot',
            'message_type': 'question',
            'message'     : question_qs.text,
            'input_type'  : question_qs.input_type.name,
            'answer'      : [answer.text for answer in answer_qs],
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.scope['session']['answer'].append(message)
        
        self.send(text_data=json.dumps({
            'user_type'   : 'You',
            'message_type': 'answer',
            'message'     : message,
        }))

        self.scope['session']['question_id'] += 1

        if self.scope['session']['question_id'] == 7:
            answer = self.scope['session']['answer']
            answer[3] = 'smoker' if answer[3].lower().find('ye') >= 0 else 'non-smoker'
            pronoun = 'he' if answer[1] == 'Male' else 'she'
            self.send(text_data=json.dumps({
                'user_type'   : 'Bot',
                'message_type': 'information',
                'message'     : answer[0] + ' was born in ' + answer[2] + ' and is a '
                                + answer[1] + ' ' + answer[3] + '. ' + pronoun.capitalize()
                                + ' usually wakes up at ' + answer[4]
                                + ' and likes to play ' + answer[5] + '.'
            }))
        else:
            question_id = self.scope['session']['question_id']
            question_qs = Question.objects.get(pk=question_id)
            answer_qs   = Answer.objects.filter(question_id=question_id)
            
            self.send(text_data=json.dumps({
                'user_type'   : 'Bot',
                'message_type': 'question',
                'message'     : question_qs.text,
                'input_type'  : question_qs.input_type.name,
                'answer'      : [answer.text for answer in answer_qs],
            }))
