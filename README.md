# LGCY Flashcard App

## Welcome to the **LGCY Flashcard App** project! This Django application allows you to create and manage flashcards. Below, you will find information about the project's structure, its components, and how to get started.

## Table of Contents
- Introduction
- Project Structure
- Installation
- Usage
- Contributing

## Introduction
The LGCY Flashcard App is a Django web application that allows you to create and manage flashcards. This is a great spot for a new hire to come into and read up about the specific LGCY lingo and what we use here. You can also test your knowledge to see how well you know LGCY Power! 

## Project Structure
The project is organized as follows:

- **models.py**: Defines the data model for flashcards.
- **urls.py**: Configures the application's URL routing.
- **views.py**: Contains the view logic for rendering flashcards.


## Installation
To install this project, follow these steps:

1. Clone the repository.
`git clone https://github.com/your-username/LGCY_Flashcard.git`

2. Navigate to the project directory:
`cd LGCY_Flashcard`

3. Create a virtual environment (recommended):
`python -m venv venv`

4. Activate the virtual environment:

5. Install the project dependencies:
`pip install -r requirements.txt`

6. Migrate the database to create the necessary tables:
`python manage.py migrate`

7. Start the development server:
`python manage.py runserver`

8. Access the application in your web browser at [localhost](http://localhost:8000/).

## Usage
The LGCY Flashcard App provides the following functionality:

- **Creating Flashcards**: You can add flashcards with topics, question text, and answer text.
- **Viewing Flashcards**: Flashcards are displayed in a list format, and you can click on individual flashcards to see their details.

To use the app, follow these steps:

1. Open the application in your web browser.

2. Click on the "Create Flashcard" button to add new flashcards.

3. View your flashcards on the main page, and click on a flashcard to see its details.

## Contributing

If you would like to contribute to the flashcards or make any changes:

1. Login to the admin portal.
`http://localhost:8000/admin/`

2. Use credentials:
- **Username**: admin
- **Password**: lgcytest

3. Go to Flashcards under **FLASHCARD**.

4. Make changes as needed but dont be an idiot!

Have fun learning about LGCY Power and if you have any questions feel free to ask any of your co-workers, We are all happy to help! <3