from flask import Flask, request, render_template
import os
from answer_query import answer_question
from context import bert_abstract
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("question.html")


@app.route('/answer', methods=["POST"])
def answer():

    question = request.form.get("question")
    answer = answer_question(question, bert_abstract)
    return render_template("answer.html", question=question, answer=answer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '3000'))
