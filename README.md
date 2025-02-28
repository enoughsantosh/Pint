# Pinterest Video Downloader API

A simple and efficient API service that allows you to download videos from Pinterest pins. This API extracts the direct video URL from Pinterest pins and provides an easy-to-use endpoint for downloading.



## 📌 Features

- Extract video URLs from Pinterest pins
- Support for 720p video quality
- Fast and reliable response
- Simple JSON response format
- Easy to integrate with any application

## 🔧 API Usage
- Create a vercel account
- connect with GitHub
- deploy it

### Download Endpoint

```
GET /download?url={pinterest_pin_url}
```

#### Parameters

| Parameter | Type   | Required | Description                    |
|-----------|--------|----------|--------------------------------|
| url       | string | Yes      | The URL of the Pinterest pin   |

#### Example Request

```
https://example.vercel.app/download?url=https://pin.it/3JEdwfKlU
```

#### Example Response

```json
{
    "download_url": "https://v1.pinimg.com/videos/iht/720p/b3/3f/50/b33f50637f6fd2463d6ffa2771edb026.mp4"
}
```

## 💻 Tech Stack

- Python
- Web Scraping
- Vercel Serverless Functions

## 🛠️ Local Development

1. Clone the repository
```bash
git clone [your-repository-url]
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the development server
```bash
python [your-main-file].py
```

## ⚠️ Important Notes

- This API is for educational purposes only
- Please respect Pinterest's terms of service and content ownership rights
- Be mindful of rate limiting and fair usage

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

If you have any questions or suggestions, please open an issue in the repository.

---
Made with ❤️ 
