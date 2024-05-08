# Mail Daily Project

## Project Overview
Mail Daily is an application designed to automatically fetch emails, categorize them, apply labels on Gmail, summarize their content, convert the summary to speech, and perform recommended actions based on the category of the email.

## Setup
- [x] Set up Python environment and install required packages.
- [x] Enable the Gmail API and download `credentials.json`.
- [x] Set up Google Cloud project and configure OAuth consent screen.

## Development Checklist

### Step 1: Gmail API Integration
- [x] Authenticate and establish a connection with the Gmail API.
- [x] Write a function to fetch emails based on specific queries.
- [x] Write a function to list existing lables
- [x] Write a function to add a label into an email

### Step 2: Email Processing
- [ ] Develop a categorization system for incoming emails. 
- [ ] Define categories and Implement the Categorization Function
- [x] Implement functionality to apply Gmail labels based on email categories.
- [ ] Use Machine Learning to categorise emails. Use Name entity extractors to understand the meaning to assign category.

### Step 3: Email Summarization
- [ ] Integrate or develop a summarization algorithm to extract key points from emails.
- [ ] Test summarization accuracy and adjust as needed.

### Step 4: Speech Conversion
- [ ] Set up the Text-to-Speech (TTS) system using a suitable Python library.
- [ ] Ensure the TTS system accurately converts email summaries into audible speech.

### Step 5: Actionable Tasks
- [ ] Define and implement recommended actions for each email category.
- [ ] Automate actions like adding events to Google Calendar based on email content.

### Step 6: Testing and Deployment
- [ ] Conduct thorough testing to ensure all components work as expected.
- [ ] Deploy the application in a suitable environment.

### Step 7: Documentation and Final Touches
- [ ] Create detailed documentation for the project.
- [ ] Refine and finalize the user interface if applicable.

## Technologies Used
- Python 3.x
- Google API Client Library
- Text-to-Speech Library (e.g., gTTS or similar)
- Any other libraries or APIs used

## Running the Application
Provide instructions on how to set up and run the application, including how to install dependencies, setting up environment variables, and running the script.

```bash
# Example to run the application
python main.py
