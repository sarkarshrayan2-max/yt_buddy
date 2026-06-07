from pytube import YouTube


def format_duration(seconds):

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if hours > 0:
        return f"{hours}h {minutes}m"

    return f"{minutes}m {seconds}s"


def get_video_metadata(url):

    try:
        yt = YouTube(url)

        return {
            "title": yt.title,
            "author": yt.author,
            "duration": format_duration(yt.length),
            "thumbnail_url": yt.thumbnail_url,
            "publish_date": str(yt.publish_date)
        }

    except Exception:
        return {
            "title": "Metadata unavailable",
            "author": "Metadata unavailable",
            "duration": "Metadata unavailable",
            "thumbnail_url": None,
            "publish_date": "Metadata unavailable"
        }