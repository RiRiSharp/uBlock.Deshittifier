# platform_names.py

_platforms = {
    "discogs": "Discogs",
    "github": "GitHub",
    "google": "Google",
    "youtube": "YouTube",
}

def get_site_name(key: str) -> str:
    return _platforms.get(key, "")