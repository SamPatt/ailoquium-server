def check_for_secret_phrase(ai_response, secret_phrase):
    if not secret_phrase:
        return False
    else:
        if secret_phrase.lower() in ai_response.lower():
            return True
        else:
            return False