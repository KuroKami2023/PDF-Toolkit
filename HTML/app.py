# app.py

from flask import Flask, request, send_file
import os
from pdf_to_excel import convert_pdf_to_excel  # Import your PDF to Excel conversion function

app = Flask(__name__)

@app.route('/convert_pdf_to_excel', methods=['POST'])
def convert_pdf_to_excel_endpoint():
    if 'pdf_file' not in request.files:
        return "No PDF file uploaded", 400

    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
        return "No PDF file selected", 400

    # Save the PDF file
    pdf_filename = pdf_file.filename
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
    pdf_file.save(pdf_path)

    # Generate a unique filename for the Excel file
    excel_filename = os.path.splitext(pdf_filename)[0] + '.xlsx'
    excel_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_filename)

    # Convert PDF to Excel
    convert_pdf_to_excel(pdf_path, excel_path)

    # Send the converted Excel file
    return send_file(excel_path, as_attachment=True)

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.run(debug=True)
