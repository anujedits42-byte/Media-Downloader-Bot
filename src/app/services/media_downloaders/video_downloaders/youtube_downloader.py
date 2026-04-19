import asyncio
import os
from yt_dlp import YoutubeDL

from src.app.services.media_downloaders.utils.files import get_video_file_name
from src.app.services.media_downloaders.seekers.search import YouTubeSearcher
from src.app.utils.enums.error import DownloadError


class YouTubeDownloader:
    def __init__(self):
        self.searchs = YouTubeSearcher()

    async def youtube_video_and_shorts_downloader(self, video_url: str):
        os.makedirs("./media/videos", exist_ok=True)

        video_path = f"./media/videos/{get_video_file_name()}"
        errors = []

        try:
            # ✅ FIXED cookies path
            cookie_path = "cookies.txt"

            ydl_opts = {
                "format": "bestvideo[height<=1080]+bestaudio/best",
                "outtmpl": video_path,
                "merge_output_format": "mp4",
                "quiet": True,
                "no_warnings": True,
                "cookiefile": cookie_path,

                # ✅ anti-block
                "sleep_interval": 3,
                "retries": 10,
                "http_headers": {
                    "User-Agent": "Mozilla/5.0"
                },
                "extractor_args": {
                    "youtube": {
                        "player_client": ["android", "web"]
                    }
                },

                "postprocessors": [{"key": "FFmpegMetadata"}],
            }

            def download_video():
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])

            await asyncio.to_thread(download_video)

            video_data = await self.searchs.get_media_info(video_url)

            video_filesize = video_data["filesize_mb"] if video_data else None

            if video_filesize and video_filesize > 2000:
                errors.append(DownloadError.FILE_TOO_BIG)

            if not video_data:
                errors.append(DownloadError.DOWNLOAD_ERROR)

            return video_path, errors

        except Exception as e:
            print("FULL ERROR:", str(e))
            return None, [DownloadError.DOWNLOAD_ERROR]
