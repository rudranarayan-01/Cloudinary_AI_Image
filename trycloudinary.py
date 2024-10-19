import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from cloudinary import CloudinaryImage
from config import api_key, api_secret, cloud_name

# Configuration       
cloudinary.config( 
    cloud_name = cloud_name, 
    api_key = api_key, 
    api_secret = api_secret, # Click 'View API Keys' above to copy your API secret
    secure=True
)

# Upload an image
upload_result = cloudinary.uploader.upload("./guddu.jpg",
                                           public_id="guddu")
print(upload_result["secure_url"])

# # Optimize delivery by resizing and applying auto-format and auto-quality
# optimize_url, _ = cloudinary_url("guddu", fetch_format="auto", quality="auto")
# print(optimize_url)

# # Transform the image: auto-crop to square aspect_ratio
# auto_crop_url, _ = cloudinary_url("guddu", width=500, height=500, crop="auto", gravity="auto")
# print(auto_crop_url)


# Transform the image: Gen Fill
# a = CloudinaryImage("guddu").image(aspect_ratio="1:1", gravity="center", background="gen_fill", crop="pad")

# Transform the image: Background Remove
a = CloudinaryImage("guddu").image(effect="gen_background_replace:prompt_Make this subject sit in time square New York")

print(a)
