# Client-Server-GPT-Convo

Input your api key in plain text in api_key.txt

api_key.txt

your-api-key
  
  Then, run the client and server in two terminals:
  
  python chat-client.py
  
  python chat-server.py
  
  Finally, start the conversation with a curl http request:
  
  curl -X POST -H "Content-Type: application/json" -d '{"message": "What fictional or non-fictional location would you travel to first? Who would you take along and why? Reason why and have a discussion about it and limit your response to three sentences."}' http://localhost:5000/start_conversation
  
  Enjoy overdrafting your OpenAI account! 😄 ctrl-c the terminal windows when you have had enough of the conversation. View the history in your history folder.
