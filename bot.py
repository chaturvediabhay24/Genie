import json
from tools import tool_descriptions, tool_map
from utils import factory_import, read_file, write_file
import config as cfg

chat_completion=factory_import(cfg.MODULE, cfg.FUNCTION)

CONVERSATION_PATH="history.json"

def update_conversation(conversation, assistant_message=None, user_message=None, message=None):
    if assistant_message:
        conversation.append({"role": "assistant", "content": assistant_message})
    if user_message:
        conversation.append({"role": "user", "content": user_message})
    if message:
        conversation.append(message)
    write_file(CONVERSATION_PATH, conversation)

def chat_with_assistant():
    print("Welcome to the terminal chatbot! Type 'exit' to end the conversation.")

    # Initialize the conversation context
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        # Get user input
        user_input = input("User: ")

        if not user_input:
            continue
        
        if user_input.lower() == "exit":
            print("Exiting the chat. Goodbye!")
            break

        # Append user's message to the conversation
        update_conversation(conversation, user_message=user_input)

        if True:
        # try:
            # Extract the assistant's message
            message = chat_completion(conversation, tools=tool_descriptions)

            if message.content:
                assistant_message = message.content
                print(f"Assistant: {assistant_message}")

            # Append assistant's message to the conversation
            update_conversation(conversation, message=message)

            while message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_name=tool_call.function.name
                    print(f"Calling tool: {tool_name}")
                    tool_arguments = tool_call.function.arguments
                    tool_result=tool_map[tool_name](**json.loads(tool_arguments))
                    update_conversation(conversation, message={"tool_call_id": tool_call.id, 
                                                               "role": "tool", 
                                                               "name": tool_name, 
                                                               "content": str(tool_result)})
                message = chat_completion(conversation, tools=tool_descriptions, model=cfg.model)

                if message.content:
                    assistant_message = message.content
                    print(f"Assistant: {assistant_message}")

                # Append assistant's message to the conversation
                update_conversation(conversation, message=message)

        # except Exception as e:
        #     print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_assistant()
