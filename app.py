from flask import Flask, render_template, request, jsonify
from simplegmail import Gmail

app = Flask(__name__)
gmail = Gmail()

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
