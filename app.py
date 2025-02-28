from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def extract_video_url(page_url):
    if "https://pin.it/" in page_url:  # Handle shortened URLs
        t_body = requests.get(page_url)
        if t_body.status_code != 200:
            return {"error": "Invalid or not working URL."}
        soup = BeautifulSoup(t_body.content, "html.parser")
        href_link = soup.find("link", rel="alternate")['href']
        match = re.search('url=(.*?)&', href_link)
        page_url = match.group(1)

    body = requests.get(page_url)
    if body.status_code != 200:
        return {"error": "Invalid or not working URL."}
    soup = BeautifulSoup(body.content, "html.parser")
    video_tag = soup.find("video", class_="hwa kVc MIw L4E")
    if video_tag:
        extract_url = video_tag['src']
        convert_url = extract_url.replace("hls", "720p").replace("m3u8", "mp4")
        return {"download_url": convert_url}
    return {"error": "Unable to extract video URL."}

@app.route("/download", methods=["GET"])
def download():
    page_url = request.args.get("url")
    if not page_url:
        return jsonify({"error": "URL parameter is required."}), 400
    if "pinterest.com/pin/" not in page_url and "https://pin.it/" not in page_url:
        return jsonify({"error": "Invalid Pinterest URL."}), 400

    result = extract_video_url(page_url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
