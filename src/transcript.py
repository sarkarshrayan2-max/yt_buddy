from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)

    if match:
        return match.group(1)

    raise ValueError("Invalid YouTube URL")


def get_transcript(url):
    try:
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

    except Exception as e:
        error_message = str(e)

        if "blocking requests from your IP" in error_message:
            raise Exception(
                "YouTube is temporarily blocking transcript requests from this IP. "
                "Please try again later or use another video."
            )

        raise Exception(
            "Transcript could not be fetched. "
            "The video may not have captions, may be private, or YouTube may be blocking the request."
        )