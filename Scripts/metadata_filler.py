import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from Scripts import file_name_site_converter


def fill_metadata_template(metadata: str, target_path: Optional[Path] = None) -> str:
    now_utc = datetime.now(timezone.utc)
    full_sha = os.getenv("GITHUB_SHA", "LOCAL00")
    short_sha = full_sha[:7]

    replacements = {
        "{{YEAR}}": str(now_utc.year),
        "{{MONTH}}": str(now_utc.month),
        "{{DAY}}": str(now_utc.day),
        "{{HOUR}}": str(now_utc.hour),
        "{{MINUTE}}": str(now_utc.minute),
        "{{MONTH_DD}}": str(now_utc.month).zfill(2),
        "{{DAY_DD}}": str(now_utc.day).zfill(2),
        "{{HOUR_DD}}": str(now_utc.hour).zfill(2),
        "{{MINUTE_DD}}": str(now_utc.minute).zfill(2),
        "{{BUILD_ID}}": short_sha,
    }

    if target_path:
        file_name = target_path.stem
        site_name = file_name_site_converter.get_site_name(file_name)
        replacements["{{SITE}}"] = site_name

    for key, value in replacements.items():
        metadata = metadata.replace(key, value)

    return metadata
