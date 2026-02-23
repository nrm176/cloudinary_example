# Cloudinary Image Uploader

A Python script for uploading images to [Cloudinary](https://cloudinary.com/) with support for different upload types (public, private, authenticated).

## Tech Stack

- Python
- Cloudinary Python SDK
- python-dotenv

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your Cloudinary credentials:
   ```
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_SECRET_KEY=your_secret_key
   ```

## Usage

Place the image in the `images/` directory, then run:

```bash
python upload.py
```

Supports three upload types: **upload** (public), **private**, and **authenticated**.

## Project Structure

```
├── .env                # Cloudinary API credentials (not committed)
├── images/             # Images to upload
├── requirements.txt
└── upload.py           # Main upload script
```
