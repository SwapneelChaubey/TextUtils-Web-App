# TextUtils - Django Web App

A powerful and simple web-based web application built with **Django** and styled with **Bootstrap 5**. TextUtils allows users to easily process, analyze, and format large blocks of text directly in their browser.

## Features Currently Supported

Our tool provides a stackable series of features you can execute on any block of text:
- 🧹 **Remove Punctuations**: Strips out all punctuation marks from your text block.
- 🔠 **UPPER CASE**: Converts all characters into loud UPPERCASE format!
- 🔡 **lower case**: Forces all characters to lowercase.
- 🏕️ **Title Case**: Capitalizes the first letter of every single word in the text.
- 🧢 **Capitalize**: Capitalizes just the very first letter of the text block.
- 🔢 **Is All Digits**: Analyzes the text and alerts you if it is composed entirely of numbers.
- 🔤 **Is All Alphabets**: Analyzes the text and alerts you if it is composed exclusively of alphabetic letters.

## Technical Details
This application uses:
- Django as the primary web backend framework processing the text routing.
- Context dictionaries mapping boolean toggles from HTML forms to Python conditional logic sequences in `views.py`.
- Modern Bootstrap 5 for the dark-mode aesthetic responsive frontend GUI.

## Running Locally

To run this application locally on your machine:

1. **Clone this repository** (or download the zip)
2. **Open a terminal** and navigate to to the inner folder where `manage.py` lives:
   ```bash
   cd TextUtils-Web-App
   ```
3. **Start the Django Development Server**:
   ```bash
   python manage.py runserver
   ```
4. **View the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`

---
*Created as a learning project to master Django view logic, forms, and template rendering!*
