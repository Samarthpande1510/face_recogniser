import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="Name of the person being photographed")
args = vars(ap.parse_args())

# 2. Define the path: app/dataset/YourName
directory = os.path.join("dataset", args["name"])

# Create the folder if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"[INFO] Created directory: {directory}")

cam = cv2.VideoCapture(0)
img_counter = 0

print("[INFO] Press SPACE to take a photo. Press ESC to finish.")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    
    cv2.imshow("Capture Faces (Space=Snap, Esc=Exit)", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        img_name = f"{directory}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"[INFO] {img_name} saved!")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()