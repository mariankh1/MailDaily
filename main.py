from simplegmail import Gmail

labels = {
    "Meetings": ["meeting", "appointment", "schedule"],
    "Financial": ["invoice", "receipt", "payment", "budget"],
    "Personal": ["birthday", "party", "wedding"],
    "Work": ["project", "deadline", "assignment", "team"],
    "Promotions": ["offer", "sale", "discount", "promo"]
}


def list_and_select_label(gmail):
    labels = gmail.list_labels()
    print("Available Labels:")
    for index, label in enumerate(labels, start=1):
        print(f"{index}. {label.name} (ID: {label.id})")  # Use dot notation

    choice = int(input("Select a label number to apply: "))
    if 1 <= choice <= len(labels):  # Ensure the choice is within the range
        selected_label = labels[choice - 1]
        return selected_label
    else:
        print("Invalid choice. Please run the function again and select a valid number.")
        return None

def fetch_unread_emails(gmail):
    """
    Fetch unread emails from the last day.

    :param gmail: Authenticated Gmail object.
    :return: List of email objects that are unread and from the last day.
    """
    # Define the query to fetch unread emails from the last 24 hours
    query = 'is:unread newer_than:1d'  # '1d' specifies a time period of one day
    messages = gmail.get_messages(query=query, include_spam_trash=False)
    return messages

def ensure_labels_exist(gmail):
    """Ensure all necessary labels exist in Gmail."""
    existing_labels = {label.name for label in gmail.list_labels()}
    missing_labels = set(labels.keys()) - existing_labels
    for label in missing_labels:
        gmail.create_label(label)  # Create each missing label
    print(f"Created missing labels: {missing_labels}")

def apply_label(gmail, message, label_id):
    """Apply the given label to the email message."""
    gmail.add_labels_to_message(message.id, [label_id])


def label_email(subject, body):
    subject_lower = subject.lower()
    body_lower = body.lower()

    for label, keywords in labels.items():
        if any(keyword in subject_lower for keyword in keywords) or any(keyword in body_lower for keyword in keywords):
            return label
    return "Other"  # Default category if no keywords match



def authenticate_gmail():
    gmail = Gmail()
    return gmail




def get_emails(query=''):
    """
    Fetch emails based on the specified query.
    :param query: Gmail search query string (similar to what you'd use in the Gmail search bar)
    :return: List of emails matching the query
    """
    messages = gmail.get_messages(query=query, include_spam_trash=False)
    emails = []
    for message in messages:
        email_details = {
            'subject': message.subject,
            'snippet': message.snippet,
            'date': message.date,
            'sender': message.sender
        }
        emails.append(email_details)
    return emails


# Example usage: Fetch unread emails
#unread_emails = get_emails('is:unread')
#for email in unread_emails:
 #   print(email)

def process_emails(gmail):
    unread_emails = fetch_unread_emails(gmail)
    if not unread_emails:
        print("No unread emails from the last day.")
        return

    labels = gmail.list_labels()
    label_dict = {label.name: label.id for label in labels}  # Create a dictionary of label names to IDs

    for email in unread_emails:
        suggested_label = label_email(email.subject, email.snippet)
        print(f"Subject: {email.subject}")
        print(f"Suggested Label: {suggested_label}")
        user_input = input("Apply this label? (yes/no): ")
        if user_input.lower() == 'yes':
            if suggested_label in label_dict:  # Check if the label exists
                apply_label(gmail, email, label_dict[suggested_label])
                print("Label applied.")
            else:
                print(f"Label '{suggested_label}' does not exist.")
        else:
            print("Label not applied.")

if __name__ == "__main__":
    gmail = authenticate_gmail()
    process_emails(gmail)