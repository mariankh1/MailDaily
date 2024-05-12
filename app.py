from flask import Flask, render_template, request, jsonify, send_file
from simplegmail import Gmail
from gtts import gTTS

app = Flask(__name__)
gmail = Gmail()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test_audio')
def test_audio():
    # Path to a sample audio file (replace 'sample_audio.mp3' with your actual audio file)
    audio_file_path = 'sample_audio.mp3'

    # Send the sample audio file to the frontend
    return send_file(audio_file_path, as_attachment=True)

@app.route('/fetch_emails', methods=['GET'])
def fetch_emails():
    messages = gmail.get_messages(query='is:unread newer_than:1d', include_spam_trash=False)
    emails = [{'subject': msg.subject, 'snippet': msg.snippet, 'id': msg.id} for msg in messages]
    return jsonify(emails)


@app.route('/apply_label', methods=['POST'])
def apply_label():
    email_id = request.json['email_id']
    label_name = request.json['label_name']
    labels = gmail.list_labels()
    label_dict = {label.name: label.id for label in labels}
    if label_name in label_dict:
        gmail.add_labels_to_message(email_id, [label_dict[label_name]])
        return jsonify({'message': 'Label applied'}), 200
    else:
        return jsonify({'message': 'Label not found'}), 404


@app.route('/get_email_summary_audio', methods=['POST'])
def get_email_summary_audio():
    print("summaru get_email_summary_audio")
    email_id = request.json['email_id']
    print("summaru " + email_id)
    message = gmail.get_message("18f588f59edff8ad")
    summary_text = f"Subject: {message.subject}. {message.snippet}"
    print("summaru" + summary_text)
    # Convert the summary text to speech
    tts = gTTS(summary_text, lang='en')
    tts.save('summary_audio.mp3')

    # Send the speech audio file back to the frontend
    return send_file('summary_audio.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
