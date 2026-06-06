from src.config import client
from src.prompts import SUMMARY_PROMPT


def summarize_video(transcript):

    prompt = SUMMARY_PROMPT.format(
        transcript=transcript
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text