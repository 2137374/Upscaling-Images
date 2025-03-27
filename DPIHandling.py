from PIL import Image

# Open the upscaled image
img = Image.open("C:\\Users\\path\\path\\path\\path.jpg")

# Set new DPI
new_dpi = (300, 300)
img.info["dpi"] = new_dpi

# Save with new DPI
img.save("C:\\Users\\path\\path\\path\\path.jpg", dpi=new_dpi)