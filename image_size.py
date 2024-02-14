import os
import cv2

def get_image_dimensions(image_path):
    image = cv2.imread(image_path)
    if image is not None:
        height, width, _ = image.shape
        print(f"Image Dimensions for {image_path}:")
        print(f"Width: {width} pixels")
        print(f"Height: {height} pixels")
    else:
        print(f"Failed to read image at path: {image_path}")

if __name__ == "__main__":
    # 이미지가 저장된 폴더 경로
    output_folder = "frames-2"

    # 이미지 파일들의 경로 리스트를 가져옴
    image_files = [f for f in os.listdir(output_folder) if f.endswith(".jpg")]

    if not image_files:
        print("No image files found in the specified folder.")
    else:
        for image_file in image_files:
            image_path = os.path.join(output_folder, image_file)
            get_image_dimensions(image_path)
