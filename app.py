import yt_dlp

playlist_url = input("Enter playlist URL: ")

options = {
    "extract_flat": True,
    "quiet": True,
    "skip_download": True,
}

with yt_dlp.YoutubeDL(options) as ydl:
    playlist = ydl.extract_info(playlist_url, download=False)

with open("video_links.txt", "w", encoding="utf-8") as file:
    for video in playlist["entries"]:
        if video:
            video_url = video["url"]
            file.write(video_url + "\n")

print("Done! Video links saved to video_links.txt")
