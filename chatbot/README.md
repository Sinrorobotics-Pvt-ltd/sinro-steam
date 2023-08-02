# Chatbot with Knowledge Base

This is a simple chatbot that interacts with the user, answers questions, and learns new information. The chatbot uses a knowledge base stored in a JSON file to respond to user queries. If the chatbot doesn't know the answer to a question, it will prompt the user to provide the answer and add it to the knowledge base for future reference.

## How to Use

1. Install Python (if you don't have it installed already): [Python Installation](https://www.python.org/downloads/)

2. Clone this repository and navigate to the directory:

```
$ git clone https://github.com/Sinrorobotics-Pvt-ltd/sinro-steam.git
$ cd your-repository
```

3. Make sure to have a knowledge base file named 'knowledge_base.json' in the same directory. The knowledge base should be in the following format:

```json
{
  "questions": [
    {
      "question": "What is the capital of France?",
      "answer": "The capital of France is Paris."
    },
    {
      "question": "What is the meaning of life?",
      "answer": "The meaning of life is 42."
    }
    // More question-answer pairs can be added
  ]
}
```

4. Run the chatbot:

```
$ python chatbot.py
```

5. The chatbot will continuously prompt for your input. Type your question or type 'quit' to exit the chatbot.

## How it Works

1. The chatbot loads the knowledge base from the 'knowledge_base.json' file and stores it in memory.

2. The user can ask a question, and the chatbot will try to find the closest matching question in the knowledge base using fuzzy string matching.

3. If the chatbot finds a match, it will return the corresponding answer.

4. If no match is found, the chatbot will ask the user to provide the answer. The user can either provide the answer or skip if they don't want to contribute.

5. If the user provides a new answer, the chatbot will add it to the knowledge base and save the updated knowledge base back to 'knowledge_base.json'.

6. The chatbot will continue the conversation until the user types 'quit'.

## Dependencies

The chatbot script uses the following Python libraries:

- `json`: For reading and writing JSON files.
- `difflib.get_close_matches`: For finding the closest matching question in the knowledge base.

## Note

Please make sure to keep the 'knowledge_base.json' file in the same directory as the chatbot script. You can customize the knowledge base file with more question-answer pairs as needed.

Happy chatting and teaching the chatbot new things!