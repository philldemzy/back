# CBEASY

CBeasy is a computer based test platform that makes creation of computer based tests easy with the uploading of **a formatted text file**

## Distinctiveness and Complexity:
- It is a web app that deals with coputer based test.
- It has back end api and front end applications seperately.
- It reads a text file into memory and uses regex to store each question, the options and its answer.
- It generates two different links.
  1. To enable students take specific exam.
  2. To enable examiners get results of exam and to also preview the exam before start time to correct any errors.
- It marks the result of each students after submitting or after duration of exam set by examiner is over.
- It follows timing procedures for computer based tests also shuffling of questions and options each time exam apge is loaded.




The front folder contains the front end application written in vue.js
### To run the front end application 
```bash
cd front
npm install
npm run serve
```



The back folder contains the backend end api written in django python
### To run back end application
```bash
pip install -r requirements.txt
cd back
python3 ./manage.py runserver
```

## Notes
The link to documentation of how to format file can be seen in the top of the page after clicking get started.
The examiner can preview an exam after setting of exam has been concluded and subsiquently through the examiner link.
Students have to put in Name and Id before taking tests.
Only examiner can see results of students after exam has ended.
