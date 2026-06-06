from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)

    if match:
        return match.group(1)

    raise ValueError("Invalid YouTube URL")


def get_transcript(url):

    video_id = extract_video_id(url)

    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video_id)

    transcript_text = " ".join(
        [snippet.text for snippet in transcript]
    )

    return {
        "video_id": video_id,
        "transcript": transcript_text,
        "word_count": len(transcript_text.split())
    }