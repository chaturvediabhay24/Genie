import openai
from dotenv import load_dotenv
import os
from utils import factory_import, read_file, write_file

load_dotenv()
# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_completion(messages, model="gpt-3.5-turbo", temperature=0.7, tools=[]):
    """
    Creates a chat completion using the OpenAI API.

    Parameters:
        messages (list): List of messages in the conversation. Each message is a dictionary with 'role' and 'content'.
        model (str): The model to use for chat completion.
        temperature float): Controls randomness of the response. (0.0 for deterministic, up to 1.0 for more random)

    Returns:
        str: The AI's response.
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            tools=tools
        )
        # write_file("file.json", response.model_dump())

        return response.choices[0].message
    
    except Exception as e:
        print(f"Error: {e}")
        return None
