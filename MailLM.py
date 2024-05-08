from transformers import AutoModelForCausalLM, AutoTokenizer


def download_and_save_model(model_name, save_directory):
    # Load model and tokenizer from Hugging Face Model Hub
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Save model and tokenizer to the specified directory
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)


def load_model_from_local(save_directory):
    # Load the model and tokenizer from a local directory
    model = AutoModelForCausalLM.from_pretrained(save_directory)
    tokenizer = AutoTokenizer.from_pretrained(save_directory)
    return model, tokenizer


# Specify the model and where you want to save it
model_name = "NousResearch/Nous-Hermes-2-Mistral-7B-DPO"
save_directory = "./Nous-Hermes-2-Mistral-7B-DPO"
download_and_save_model(model_name, save_directory)
model, tokenizer = load_model_from_local(save_directory)


def generate_email_response(model, tokenizer, subject, body):
    prompt = f"Subject: {subject}\nBody: {body}\n\nSuggest a category and actions for this email:"
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs['input_ids'], max_length=1024, no_repeat_ngram_size=2)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Example usage
subject = "Reminder: Project Meeting Tomorrow"
body = "Hello, just a reminder about our project meeting tomorrow at 10 AM. Please confirm your attendance."
response = generate_email_response(model, tokenizer, subject, body)
print(response)
