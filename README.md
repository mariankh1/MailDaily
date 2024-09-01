# MailyDaily 📬 a Generative-AI Mail assistant

## About MailyDaily

**MailyDaily** is a smart, cross-platform mobile app designed to help you manage your Gmail inbox more efficiently and effortlessly. Built with React Native, MailyDaily leverages the power of AI to provide a daily email review in a conversational style. The app not only summarizes your new emails but also suggests actions like replying, archiving, or setting reminders, all through a user-friendly and interactive interface.

Our goal with MailyDaily is to revolutionize the way you interact with your emails by introducing a voice-assisted, hands-free experience that helps you stay organized and on top of your communication. By integrating a custom-trained Hugging Face model, MailyDaily provides personalized email summaries and automates routine tasks, helping you save time and maintain a clutter-free inbox.

MailyDaily is designed with privacy and security in mind. All data is processed locally on your device, ensuring that your sensitive information remains private and secure.

### Why MailyDaily?

- **Efficiency**: Quickly process and manage your emails with AI-powered summaries and action suggestions.
- **Simplicity**: Navigate through your inbox using a conversational, intuitive interface.
- **Voice Assistance**: Interact with your emails hands-free with the built-in voice assistant.
- **Privacy-First**: Enjoy peace of mind knowing that your data is processed securely on your device.

Join us in transforming email management and experience a smarter way to handle your inbox with MailyDaily!

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
   git clone https://github.com/mariankh1/MailyDaily.git
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

Contributions are welcome! Please check the CONTRIBUTE.md file for guidelines on how to contribute to the project.
For help, contact us at mailydailyproject@gmail.com 

## License

This project is licensed under the MIT License - see the LICENSE file for details.
