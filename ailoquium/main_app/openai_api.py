import os
import openai

# Configure the OpenAI client with your API key
client = openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def send_message_to_openai(user_message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an AI librarian."},
                {"role": "user", "content": user_message}
            ],
            model="gpt-3.5-turbo",
        )
        if chat_completion.choices:
            return chat_completion.choices[0].message.content
        else:
            return None

    except Exception as e:
        print(f"Error in sending message to OpenAI: {e}")
        return None

def modify_openai_response(api_response):
    # Add your logic to modify the OpenAI API response
    # For example, you might want to format it or extract certain information
    # Return the modified response
    pass
