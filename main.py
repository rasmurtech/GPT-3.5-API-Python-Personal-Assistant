import openai
import os

# Replace 'your_api_key' with your actual API key
openai.api_key = "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"


def ask_gpt_35(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer


def personal_assistant():
    print("Hello! I am your personal assistant powered by GPT-3.5. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Assistant: Goodbye! Have a great day!")
            break

        prompt = f"My user asked: {user_input}\nAnswer:"
        response = ask_gpt_35(prompt)
        print(f"Assistant: {response}")


if __name__ == "__main__":
    personal_assistant()
