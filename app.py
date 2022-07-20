from flask import Flask, request, render_template
import os
from answer_query import answer_question
from context import bert_abstract
from producer import publish_question
from transformers import BertTokenizer
import pickle

app = Flask(__name__)

tokenizer = BertTokenizer.from_pretrained(
    'bert-large-uncased-whole-word-masking-finetuned-squad')
with open('BERT_DL_model.pkl', 'rb') as file:
    BERT_DL_Model = pickle.load(file)


@app.route("/")
def home():
    return render_template("question.html")


@app.route('/answer', methods=["POST"])
def answer():

    question = request.form.get("question")
    publish_question(question)
    answer = answer_question(question, bert_abstract, tokenizer, BERT_DL_Model)
    return render_template("answer.html", question=question, answer=answer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '3000'))
