import os

image_directory ="images"  # Replace with the actual path to your image directory

# Get a list of image files
image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Iterate through each image file
for image_file in image_files:
    image_name = os.path.splitext(image_file)[0]  # Extract the image name without extension
    txt_file = image_name + ".txt"  # Assume the corresponding text file has the same name with .txt extension

    # Check if the corresponding text file exists
    if not os.path.exists(os.path.join(image_directory, txt_file)):
        # Delete the image file if the corresponding text file does not exist
        os.remove(os.path.join(image_directory, image_file))
        print(f"Deleted {image_file} because {txt_file} does not exist.")