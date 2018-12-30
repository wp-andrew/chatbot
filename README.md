# chatbot

**chatbot** is a web application that can initiate simple conversation with users and provide a summary based on their answers.

### Django Applications
The application based on two core components:
- _chat/_ : **Chat Module** - allows the program to communicate with the user through a simple UI.
- _qa/_ : **Q&A Module** - allows the user to update the question and answer database.

### Initial Setup
1. create a database in postgresql (you can name it anything)
2. update DATABASES parameter in chatbot/settings.py accordingly (NAME, PASSWORD, etc)
3. pip install django
4. pip install psycopg2
5. pip install -U channels
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py loaddata inputtype.json
9. python manage.py loaddata question.json
10. python manage.py loaddata answer.json

### How to Run
1. python manage.py runserver
2. Navigate to http://localhost:8000/chat/

### Updating the Q&A database
1. Add more questions and answers into QnA.txt in the following format (currently the supported input types are text, radio, checkbox, date, time):
   > question
   > input_type nb_of_answer
   > answer1
   > answer2
   > ...
   > --- empty line ---
2. run createjson.py
3. python manage.py loaddata question.json
4. python manage.py loaddata answer.json