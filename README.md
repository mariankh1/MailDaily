# MailyDaily 📬 a Generative-AI Mail assistant

**MailyDaily** is a cross-platform mobile app built with React Native that helps you efficiently manage your Gmail inbox through a conversational and voice-assisted interface. The app provides a daily summary of your new emails and suggests actions for each, such as replying, archiving, or scheduling follow-ups, all in a user-friendly and intuitive format. With the integration of a Hugging Face model, MailyDaily offers personalized email summaries and automated response suggestions to help you keep your inbox clean and organized effortlessly.

## Key Features

- **Cross-Platform Support**: Built with React Native, MailyDaily runs seamlessly on both Android and iOS devices, providing a consistent user experience.
- **Gmail Integration**: Securely log in with your Gmail account to fetch and manage your emails directly from the app.
- **Conversational Interface**: Navigate through your emails in a conversational style, making it easier to process and take action on each email.
- **Voice Assistant**: Use the built-in voice assistant to interact with your emails hands-free, including reading summaries, replying, and more.
- **AI-Powered Email Summaries**: Leveraging a custom-trained Hugging Face model, MailyDaily provides concise summaries and suggested actions for each email.
- **Privacy-Focused**: All data is processed locally on your device, ensuring your privacy and keeping your sensitive information secure.

## How It Works

1. **Sign In with Gmail**: Log in securely using your Gmail account credentials.
2. **Daily Email Review**: Each morning, MailyDaily fetches your new emails and provides a cheerful summary with suggested actions.
3. **Take Action Effortlessly**: Respond to emails, archive, delete, or set reminders directly through the conversational interface or voice commands.
4. **Stay Organized**: Use the app to maintain a clean and tidy inbox, prioritizing important messages and filtering out spam.

## Technologies Used

- **React Native**: For cross-platform mobile app development.
- **Google Sign-In**: For secure authentication with Gmail.
- **TensorFlow Lite**: For running AI models directly on mobile devices.
- **Hugging Face Transformers**: For natural language processing and generating email summaries.
- **Async Storage**: For secure local data storage.

## Getting Started

To get started with MailyDaily, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MailyDaily.git
    ```
   
2. Install dependencies:
 ```bash
    npm install
 ``` 

3. Set up Google Sign-In and TensorFlow Lite as per the instructions.
   
5. Run the app on an emulator or physical device:

 ```
  npx react-native run-android
 ```
or
 ```
  npx react-native run-ios
 ```

## Contributing

Contributions are welcome! Please check the CONTRIBUTING.md file for guidelines on how to contribute to the project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
