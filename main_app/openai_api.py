import os
import openai

# Configure the OpenAI client with your API key
client = openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def send_message_to_openai(user_message, message_history):
    print("Printing history as soon as send_message func runs: ", message_history)
    # Add the new user message to the message history
    message_history.append({"role": "user", "content": user_message})

    # Truncate the history to keep the initial message, the first two exchanges, and the last three exchanges
    if len(message_history) > 7:
        message_history = [message_history[0]] + message_history[1:3] + message_history[-3:]

    try:
        print("Message history", message_history)
        chat_completion = client.chat.completions.create(
            messages=message_history,
            model="gpt-3.5-turbo",
        )
        if chat_completion.choices:
            ai_response = chat_completion.choices[0].message.content
            # Add AI response to the history
            message_history.append({"role": "assistant", "content": ai_response})
            return ai_response, message_history
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
