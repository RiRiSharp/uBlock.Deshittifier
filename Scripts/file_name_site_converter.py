# platform_names.py

_platforms = {
    "discogs": "Discogs",
    "github": "GitHub",
    "google": "Google",
    "youtube": "YouTube",
    "nrc": "NRC",
    "storygraph": "StoryGraph",
}


def get_site_name(key: str) -> str:
    return _platforms.get(key, "")
