from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import json
import re
import string

with open('reponses.json', 'r') as file:
    responses = json.load(file)

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

chatbot = pipeline('text-generation', model=model, tokenizer=tokenizer)

def clean_input(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

def detect_intent(user_input):
    user_input = clean_input(user_input)

    if re.search(r'\b(register|course registration)\b', user_input):
        return 'ask_course_registration'
    elif re.search(r'\badmit card\b', user_input):
        return 'ask_admit_card_generation'
    elif re.search(r'\b(security|exam security)\b', user_input):
        return 'ask_exam_security'
    elif re.search(r'\bresult\b', user_input):
        return 'ask_result_generation'
    elif re.search(r'\battendance\b', user_input):
        return 'ask_attendance_tracking'
    elif re.search(r'\b(thank you|thanks|thx|thank u)\b', user_input):
        return 'thank_you'
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return 'goodbye'
    elif re.search(r'\bexam modules?\b', user_input):
        return 'ask_exam_modules'
    elif re.search(r'\bcheating percentage\b', user_input):
        return 'ask_cheating_percentage'
    elif re.search(r'\bpost[- ]?exam analysis\b', user_input):
        return 'ask_post_exam_analysis'
    elif re.search(r'\bsystem features?\b', user_input):
        return 'ask_system_features'
    elif re.search(r'\bsecurity measures?\b', user_input):
        return 'ask_security_measures'
    elif re.search(r'\bregistration issues?\b', user_input):
        return 'ask_registration_issues'
    elif re.search(r'\badmit card issues?\b', user_input):
        return 'ask_admit_card_issues'
    elif re.search(r'\bexam schedule\b', user_input):
        return 'ask_exam_schedule'
    elif re.search(r'\bexam format\b', user_input):
        return 'ask_exam_format'
    elif re.search(r'\bsupport contact\b', user_input):
        return 'ask_support_contact'
    elif re.search(r'\bdata privacy\b', user_input):
        return 'ask_data_privacy'
    elif re.search(r'\bfeedback\b', user_input):
        return 'ask_feedback'
    else:
        return 'default'

def get_response(intent):
    if intent in responses:
        return responses[intent][0]
    else:
        return responses["default"][0]

def main():
    print("Hello! I'm here to assist you with the Smart Entry Test Proctor system. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye! Have a great day!")
            break

        intent = detect_intent(user_input)
        response = get_response(intent)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
