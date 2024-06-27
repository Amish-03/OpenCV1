import os
import cv2

def images_to_video(image_folder, output_video_path, fps=30):
    # Get list of images in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()  # Ensure the images are sorted in order

    # Check if there are images in the folder
    if not images:
        print("No images found in the folder.")
        return

    # Get the first image to determine the size of the video
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    if frame is None:
        print(f"Failed to read image: {first_image_path}")
        return

    # Get the frame size
    height, width, layers = frame.shape
    frame_size = (width, height)

    # Initialize the VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
    video = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

    # Read and write each image to the video
    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Failed to read image: {image_path}")
            continue
        video.write(frame)

    # Release the VideoWriter
    video.release()
    print(f"Video saved at {output_video_path}")

# Example usage
image_folder = r'C:\Users\win10\Desktop\KLE tech\CIM\ICPR\training dataset.zip\train dataset\001\img'
output_video_path = os.path.join(image_folder, 'output_video.mp4')
images_to_video(image_folder, output_video_path)
