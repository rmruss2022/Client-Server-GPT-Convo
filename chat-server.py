from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

def read_api_key_from_file():
    with open('api_key.txt', "r") as f:
        return f.readline().strip()

openai.api_key = read_api_key_from_file()


@app.route('/conversation', methods=['POST'])
def conversation():
    input_data = request.get_json()
    messages = input_data["messages"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_message = response.choices[0].message["content"]

    print(assistant_message)

    return {"message": {'content': assistant_message, 'role': 'assistant'}}

if __name__ == '__main__':
    app.run(port=5001, debug=True)



