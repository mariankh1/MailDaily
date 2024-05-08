from simplegmail import Gmail


def authenticate_gmail():
    gmail = Gmail()
    return gmail


gmail = authenticate_gmail()


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
unread_emails = get_emails('is:unread')
for email in unread_emails:
    print(email)
