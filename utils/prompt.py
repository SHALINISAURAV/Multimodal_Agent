def build_prompt(user_text, caption):
    return f"""
You are an intelligent AI assistant.

User Question:
{user_text}

Image Description:
{caption}

Give a clear and helpful answer.
"""
