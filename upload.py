import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
dotenv_path = BASE_DIR.joinpath('.env')
load_dotenv(dotenv_path)


print(BASE_DIR.joinpath('images/sample.jpg'))

cloudinary.config(
  cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME"),
  api_key = os.environ.get("CLOUDINARY_API_KEY"),
  api_secret = os.environ.get("CLOUDINARY_SECRET_KEY"),
)

# Private
x = cloudinary.uploader.upload(str(BASE_DIR.joinpath('images/sample.png')),
  type = "private")

# Authenticated
# cloudinary.uploader.upload('/Users/sk37/Projects/PycharmProjects/Cloudinary/images/sample.png',
#   type = "authenticated")

# Sign URL
# x = cloudinary.uploader.upload('/Users/sk37/Projects/PycharmProjects/Cloudinary/images/sample.png',
#   type = "authenticated", sign_url=True)
print(x)

# Default
# cloudinary.uploader.upload('/Users/sk37/Projects/PycharmProjects/Cloudinary/images/sample.png',
#   type = "upload")
