# Mail Daily Project

## Project Overview
Mail Daily is an application designed to automatically fetch emails, categorize them, apply labels on Gmail, summarize their content, convert the summary to speech, and perform recommended actions based on the category of the email.

## Setup
- [x] Set up Python environment and install required packages.
- [x] Enable the Gmail API and download `credentials.json`.
- [x] Set up Google Cloud project and configure OAuth consent screen.

## Development Checklist

### Back-end Functionality 
#### Step 1: Gmail API Integration
- [x] Authenticate and establish a connection with the Gmail API.
  - [x] Write a function to fetch emails based on specific queries.
  - [x] Write a function to list existing labels.
  - [x] Write a function to createa a label if does not exist.
  - [x] Write a function to apply a label to an email.

#### Step 2: Email Processing
- [ ] Develop a categorization system for incoming emails.
  - [ ] Define categories and implement the categorization function.
  - [ ] Use machine learning to categorize emails
  - [x] Implement functionality to apply Gmail labels based on email categories.
- [ ] Test summarization accuracy and adjust as needed.

#### Step 3: Speech Conversion
- [ ] Set up the Text-to-Speech (TTS) system using a suitable Python library.
- [ ] Ensure the TTS system accurately converts email summaries into audible speech.

#### Step 4: Actionable Tasks
- [ ] Define and implement recommended actions for each email category.
- [ ] Automate actions like adding events to Google Calendar based on email content.

### Web Application Development
- [ ] Design and implement a user-friendly web interface to display email summaries and categorization.
  - [ ] Create front-end using HTML, CSS, and JavaScript.
  - [ ] Develop Flask backend to serve API requests from the front-end.
  - [ ] Implement user authentication to secure access to emails.
- [ ] Allow users to manually override or confirm email categorizations through the web interface.
- [ ] Provide functionality for users to listen to their email summaries directly from the web interface.

### Testing and Deployment
- [ ] Conduct thorough testing to ensure all components work as expected, including:
  - [ ] Unit tests for backend logic.
  - [ ] Integration tests for end-to-end functionality.
  - [ ] User acceptance testing to validate user interface and interactions.
- [ ] Deploy the application in a suitable environment.
  - [ ] Set up a secure deployment using HTTPS.
  - [ ] Configure cloud-based hosting and domain settings.

### Documentation and Final Touches
- [ ] Create detailed documentation for the project.
  - [ ] Document API endpoints and their usage.
  - [ ] Provide setup and installation instructions.
  - [ ] List all dependencies and their purposes.
- [ ] Refine and finalize the user interface if applicable.

## Technologies Used
- Python 3.x
- Flask for the backend
- HTML, CSS, JavaScript for the frontend
- Google API Client Library
- Text-to-Speech Library (e.g., gTTS)
- Machine Learning libraries for NLP tasks

## Running the Application
Provide instructions on how to set up and run the application, including how to install dependencies, setting up environment variables, and running the script.

```bash
# To run the Flask application
export FLASK_APP=app.py
flask run
