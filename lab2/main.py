import pandas as pd
import openai
from collections import Counter

# Ustaw swój klucz API OpenAI
openai.api_key = "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"

def read_diabetes_data(filename):
    data = pd.read_csv(filename)
    decision_classes = data.iloc[:, -1]
    class_counts = Counter(decision_classes)

    return class_counts

def ask_openai(question):
    openai_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = openai_response.choices[0].text.strip()
    return response

def chatbot(question):
    question = question.lower()

    if "ile klas decyzyjnych" in question or "klas decyzyjnych" in question:
        class_counts = read_diabetes_data("diabetes.txt")
        num_classes = len(class_counts)
        response = f"W pliku diabetes.txt znajduje się {num_classes} klas decyzyjnych."

    elif "wielkość" in question and ("klas decyzyjnych" in question or "klasy decyzyjnej" in question):
        class_counts = read_diabetes_data("diabetes.txt")
        response = "Wielkości klas decyzyjnych w pliku diabetes.txt:\n"
        for cls, count in class_counts.items():
            response += f"Klasa {cls}: {count}\n"

    else:
        response = ask_openai(question)

    return response

if __name__ == "__main__":
    while True:
        question = input("Zadaj pytanie: ")
        print(chatbot(question))