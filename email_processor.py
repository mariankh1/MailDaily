from simplegmail import Gmail

class EmailProcessor:
    labels = {
        "Meetings": ["meeting", "appointment", "schedule"],
        "Financial": ["invoice", "receipt", "payment", "budget"],
        "Personal": ["birthday", "party", "wedding"],
        "Work": ["project", "deadline", "assignment", "team"],
        "Promotions": ["offer", "sale", "discount", "promo"]
    }

    def __init__(self):
        self.gmail = Gmail()

    def list_and_select_label(self):
        labels = self.gmail.list_labels()
        print("Available Labels:")
        for index, label in enumerate(labels, start=1):
            print(f"{index}. {label.name} (ID: {label.id})")

        choice = int(input("Select a label number to apply: "))
        if 1 <= choice <= len(labels):
            return labels[choice - 1]
        else:
            print("Invalid choice. Please run the function again and select a valid number.")
            return None

    def fetch_unread_emails(self):
        query = 'is:unread newer_than:1d'
        messages = self.gmail.get_messages(query=query, include_spam_trash=False)
        return messages

    def apply_label(self, message, label_id):
        self.gmail.add_labels_to_message(message.id, [label_id])

    def label_email(self, subject, body):
        subject_lower = subject.lower()
        body_lower = body.lower()

        for label, keywords in self.labels.items():
            if any(keyword in subject_lower for keyword in keywords) or any(keyword in body_lower for keyword in keywords):
                return label
        return "Other"

    def process_emails(self):
        unread_emails = self.fetch_unread_emails()
        if not unread_emails:
            print("No unread emails from the last day.")
            return

        label_dict = {label.name: label.id for label in self.gmail.list_labels()}
        for email in unread_emails:
            suggested_label = self.label_email(email.subject, email.snippet)
            print(f"Subject: {email.subject}")
            print(f"Suggested Label: {suggested_label}")
            user_input = input("Apply this label? (yes/no): ")
            if user_input.lower() == 'yes':
                if suggested_label in label_dict:
                    self.apply_label(email, label_dict[suggested_label])
                    print("Label applied.")
                else:
                    print(f"Label '{suggested_label}' does not exist.")
            else:
                print("Label not applied.")

# Example of how to use the class
if __name__ == "__main__":
    email_processor = EmailProcessor()
    email_processor.process_emails()