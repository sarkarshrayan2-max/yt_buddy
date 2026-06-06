from src.config import client
from src.prompts import SUMMARY_PROMPT
from src.chunker import get_processing_mode, split_transcript


def summarize_video(transcript):

    processing_info = get_processing_mode(transcript)

    if processing_info["mode"] == "direct":
        return direct_summary(transcript), processing_info

    return chunked_summary(transcript), processing_info


def direct_summary(transcript):
    prompt = SUMMARY_PROMPT.format(transcript=transcript)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def chunked_summary(transcript):
    chunks = split_transcript(transcript)

    chunk_summaries = []

    for index, chunk in enumerate(chunks):
        prompt = f"""
        Summarize this part of the video transcript.

        This is chunk {index + 1} of {len(chunks)}.

        Focus on:
        - Main ideas
        - Important concepts
        - Examples
        - Key points

        Transcript Chunk:
        {chunk}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        chunk_summaries.append(response.text)

    combined_summary_text = "\n\n".join(chunk_summaries)

    final_prompt = f"""
    You are an expert video summarizer.

    Below are summaries of different parts of one YouTube video.

    Create one final structured summary with:

    1. Short Summary
    2. Detailed Explanation
    3. Key Takeaways
    4. Important Concepts
    5. Actionable Insights

    Chunk Summaries:

    {combined_summary_text}
    """

    final_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    return final_response.text