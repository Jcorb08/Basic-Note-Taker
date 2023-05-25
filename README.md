# Basic-Note-Taker
RESTful API for a basic note-taking application using Django

[![Django Tests CI](https://github.com/Jcorb08/Basic-Note-Taker/actions/workflows/tests.yml/badge.svg)](https://github.com/Jcorb08/Basic-Note-Taker/actions/workflows/tests.yml)

## To run
- Download the git repo
- install a local python3.10 enviroment
- activate your enviroment
- install the packages using requirements.txt
- run tests using `python manage.py test`
- run API/webserver using `python manage.py runserver`
- access get_all and create on `/`
- access get_single, update and delete on `/<int:pk>`

## Features
- All requirements below
- Uses SQLite to store the data
- runs tests on push using github CI

## Requirements
Broken down by me to better understand task

- The API should allow:
  -  create a note, 
  -  read a note 
    -  single by ID
    -  list all
  -  update a note, 
  -  delete notes.
 
- Each note should have a title and content.
- Save Notes to memory is ok
  - maybe use models just because SQLite is easy to implement
- Write unit tests to ensure the functionality and reliability of the API.
- Include appropriate error handling and validation for note creation and updates.
 
 
- Use a modern backend framework (e.g., Flask, Django, Express) to develop the API.
- Write clear and concise code, follow best practices, and use appropriate design patterns.
- Provide a README file with instructions on how to set up and run the API locally.

- Optionally, you can add additional features or enhancements to showcase your skills and creativity.

## Original Task
BGN Graduate Software Engineer Technical Test

### Introduction
This is a small task designed for us to better understand your approach to solving software engineering problems and interpretation of requirements. You may use a language or framework of your choice.

Please aim to spend no more than 2-3 hours on this task. If you run out of time, don't worry, just add a description of what you would have added or changed to complete it.

### The Task 
Task: Build a RESTful API for a basic note-taking application.

### Requirements

* The API should allow users to create, read, update, and delete notes.
* Each note should have a title and content.
* The API should provide endpoints to list all notes, retrieve a single note by ID, create a new note, update an existing note, and delete a note.
  * For the purpose of this task, you can save the notes in memory so don't worry about using a persistance layer like MySQL.
* Use a modern backend framework (e.g., Flask, Django, Express) to develop the API.
* Include appropriate error handling and validation for note creation and updates.
* Write clear and concise code, follow best practices, and use appropriate design patterns.
* Write unit tests to ensure the functionality and reliability of the API.
* Provide a README file with instructions on how to set up and run the API locally.
* Optionally, you can add additional features or enhancements to showcase your skills and creativity.

## How to submit your technical test

Preferably you will submit your code via a public repository you own e.g. your own Github or Bitbucket account. However, you may also submit your code via email or file sharing mechanism - e.g. Dropbox - using an archive, such as zip file or tarball (please consider the size of the file before emailing).

```
Please include a README file detailing how to run your application and a brief explanation of why you chose your language/framework.
```
