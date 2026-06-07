from src.config import groq_llm


def translate_text(text, target_language):
    if target_language == "English":
        return text

    prompt = f"""
    Translate the following text into {target_language}.

    Keep:
    - headings
    - bullet points
    - formatting
    - meaning

    Do not add extra explanation.

    Text:
    {text}
    """

    response = groq_llm.invoke(prompt)

    return response.content