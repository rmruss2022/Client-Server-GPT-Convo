from flask import Flask, request, jsonify
import openai
import requests
import textwrap
from datetime import datetime

app = Flask(__name__)

conversation_history = []

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"history/chat-history-{current_time}.txt"

def read_api_key_from_file():
    with open('api_key.txt', "r") as f:
        return f.readline().strip()

openai.api_key = read_api_key_from_file()


@app.route('/start_conversation', methods=['POST'])
def start_conversation():
    input_data = request.get_json()
    initial_message = input_data["message"]
    conversation_history.append({"role": "system", "content": "You are two chat bots conversing with one another, trying to create an interesting discussion as to the nature of travel to fictional and non-fictional places."})
    conversation_history.append({"role": "user", "content": 'What fictional or non-fictional location would you travel to first? Who would you take along and why? Reason why and have a discussion about it and limit your response to three sentences. An example would be Hitchkikers Guide to the Galaxy, think of the adventures you would have and write about it!.' or initial_message})
    while True:
        r = requests.post("http://localhost:5001/conversation", json={"messages": conversation_history})
        conversation = r.json()
        print(f"Message from server: {conversation['message']!r}")

        conversation_history.append(conversation["message"])

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )

        user_message = response.choices[0].message["content"]
        conversation_history.append({'content': user_message, 'role': 'user'})

        with open(filename, "w") as f:
            for message in conversation_history:
                wrapped_content = textwrap.fill(message['content'], width=80)
                f.write('role: ' + message['role'] + '\ncontent: ' + wrapped_content + '\n\n')
            f.close()


    return jsonify(conversation_history)

if __name__ == '__main__':
    app.run(port=5000, debug=True)





