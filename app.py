# Task 1: Setting Up the Flask Environment and Database Connection (db_connect.py)

from flask import Flask, jsonify, request #importing the Flask class
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError
from db_connect import db_connection, Error



# Task 2: Implementing CRUD Operations for Members

# Define the Book schema using Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)

#Creating Book Table Schema
class BookSchema(ma.Schema):

    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    isbn = fields.String(required=True)
    publication_date = fields.String(required=True)
    availability = fields.String(required=True)

    class Meta:
        fields = ('id', 'title', 'isbn', 'publication_date', 'availability')

book_schema = BookSchema()
books_schema = BookSchema(many=True)


@app.route('/')
def home():
    return 'Welcome to the Library Management System!'



@app.route('/books', methods=['POST'])
def add_book():
    try:
        book_data = book_schema.load(request.json)
        print(book_data)
    except ValidationError as e:
        return jsonify(e.messages), 400


    conn = db_connection()
    if con is not None:
        try:
            cursor = conn.cursor()

            new_book = (title['title'], isbn['isbn'], publication_date['published_date'], availability['availability'])
            
            query = "INSERT INTO books (title, isbn, publication_date, availability) VALUES (%s, %s, %s, %s)"
            
            cursor.execute(query, new_book)
            conn.commit()
            
            return jsonify({"message": "Book added successfully!"}), 201
        except Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({"Error": "Database Connection Failed"}), 500


if __name__ == '__main__':
    app.run(debug=True)