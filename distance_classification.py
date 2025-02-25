import cv2
import matplotlib.pyplot as plt

# Define image file paths
image_paths = ["Plaksha_Faculty.jpg", "Dr_Shashi_Tharoor.jpg"]

# Load and display images
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

for i, image_path in enumerate(image_paths):
    try:
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        axes[i].imshow(image)
        axes[i].set_title(image_path)
        axes[i].axis("off")
    except Exception as e:
        print(f"Error loading {image_path}: {e}")

plt.show()
