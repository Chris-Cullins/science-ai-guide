#!/usr/bin/env python3
import argparse
import re
import sys
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable
from youtube_transcript_api import YouTubeTranscriptApi


def video_id_from_url(url_or_id: str) -> str:
    s = url_or_id.strip()

    # If an 11-char id was provided, accept it.
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", s):
        return s

    u = urlparse(s)

    # https://www.youtube.com/watch?v=VIDEOID
    if u.netloc in {"www.youtube.com", "youtube.com", "m.youtube.com"}:
        qs = parse_qs(u.query)
        if qs.get("v"):
            return qs["v"][0]

    # https://youtu.be/VIDEOID
    if u.netloc == "youtu.be":
        vid = u.path.strip("/").split("/")[0]
        if vid:
            return vid

    raise ValueError(f"Could not extract video id from: {url_or_id}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch a YouTube transcript.")
    ap.add_argument("url_or_id", help="YouTube URL or 11-char video id")
    ap.add_argument("--lang", default="en", help="Preferred language (default: en)")
    ap.add_argument(
        "--format",
        choices=["text"],
        default="text",
        help="Output format (default: text)",
    )
    ap.add_argument("-o", "--out", help="Write to file instead of stdout")
    args = ap.parse_args()

    vid = video_id_from_url(args.url_or_id)

    try:
        api = YouTubeTranscriptApi()

        # Support both older and newer youtube-transcript-api versions.
        if hasattr(api, "list"):
            transcripts = api.list(vid)

            tr = None
            try:
                tr = transcripts.find_manually_created_transcript([args.lang])
            except Exception:
                pass
            if tr is None:
                try:
                    tr = transcripts.find_generated_transcript([args.lang])
                except Exception:
                    pass
            if tr is None:
                tr = transcripts.find_transcript([args.lang])

            fetched = tr.fetch()
            items = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else fetched

        elif hasattr(YouTubeTranscriptApi, "list_transcripts"):
            transcripts = YouTubeTranscriptApi.list_transcripts(vid)
            tr = transcripts.find_transcript([args.lang])
            items = tr.fetch()

        elif hasattr(api, "fetch"):
            fetched = api.fetch(vid, languages=[args.lang])
            items = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else fetched

        else:
            raise RuntimeError(
                "Unsupported youtube-transcript-api version: expected list/list_transcripts/fetch APIs."
            )

    except (TranscriptsDisabled, NoTranscriptFound) as e:
        print(f"Transcript not available: {e}", file=sys.stderr)
        return 2
    except VideoUnavailable as e:
        print(f"Video unavailable: {e}", file=sys.stderr)
        return 3

    content = "\n".join((it.get("text") or "").replace("\n", " ").strip() for it in items).strip() + "\n"

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        sys.stdout.write(content)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
