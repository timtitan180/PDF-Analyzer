from flask import Flask, request, render_template, url_for, redirect, session


from datetime import date

'''from database import data
import sqlite3'''

import os

import pdfplumber

from db_connection import database_cursor

app = Flask(__name__)


#
# class Files(db.Model):
#     _id = db.Column("id", db.Integer(100))
#     filename = db.Column("filename", db.String)
#     repeated_word = db.Column(db.String())
#     date = db.Column()
#
#
# def__init__(self, filename, repeated_word, date):
#     self.filename = filename
#     self.repeated_word = repeated_word
#     self.date = date

MAX_FILE_SIZE = 24 * 1024 * 1024

ALLOWED_EXT = 'pdf'

word_counts = {}

errors = []

PORT = 4210

date = date.today()

def checkFile(file):
    filename = file.filename
    extension = filename[len(filename)-3:len(filename)]
    if(extension != ALLOWED_EXT):
        errors.append("File must be a PDF. Sorry!")
        return render_template("index.html",error=errors)
    else:
        print("Uploading file...")

def check_file_extension(filename):
    try:
        extension = os.path.splitext(filename)[1]
        return extension
    except Exception as e:
        errors.append("Only PDF files are accepted")
        redirect(url_for(home_route, errors=errors))
        print(e)


def check_file_size(filename):
    if (len(filename.read()) > MAX_FILE_SIZE):
        filename.read(MAX_FILE_SIZE)

    '''Push message that file cant be taken if it is larger than MAX_FILE_SIZE'''


@app.route('/', methods=["GET"])
def home_route():
    return render_template("index.html", datestamp=date)


@app.route('/analyze_pdf', methods=['GET', 'POST'])
def post_route():
    if request.method == "POST":
        file = request.files['file']
        with pdfplumber.open(file) as pdf:
            first_page = pdf.pages[0]
            pdf_paragraphs = first_page.extract_text()
            sentences = pdf_paragraphs.split()
            for word in sentences:
             if (sentences.count(word) > 1):
                 analysis = f"'{word}' is repeated a lot in the file"
        return render_template("index.html", errors=errors, pdf_analysis=analysis,datestamp=date)


if __name__ == "__main__":
    app.run(debug=True, PORT=os.getenv('FLASK_RUN_PORT'))
