import os
import random
import shutil

def split_and_move_dataset(base_dir, train_ratio=0.8):
    """
    Splits the dataset into training and validation sets and moves the files.

    Args:
        base_dir (str): The base directory of the YOLO dataset (e.g., 'd:/football/football_yolo').
        train_ratio (float): The ratio of training data.
    """
    images_dir = os.path.join(base_dir, 'images')
    labels_dir = os.path.join(base_dir, 'labels')

    # Destination directories
    train_img_dir = os.path.join(images_dir, 'train')
    val_img_dir = os.path.join(images_dir, 'val')
    train_lbl_dir = os.path.join(labels_dir, 'train')
    val_lbl_dir = os.path.join(labels_dir, 'val')

    # Ensure destination directories exist
    os.makedirs(train_img_dir, exist_ok=True)
    os.makedirs(val_img_dir, exist_ok=True)
    os.makedirs(train_lbl_dir, exist_ok=True)
    os.makedirs(val_lbl_dir, exist_ok=True)

    # Get all image files (ignoring subdirectories)
    image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f)) and f.endswith('.jpg')]
    
    if not image_files:
        print("No image files found in the root 'images' directory.")
        print("Please ensure your image files are directly in 'd:\\football\\football_yolo\\images\\'.")
        return

    # Shuffle the files randomly
    random.shuffle(image_files)

    # Split the files
    split_index = int(len(image_files) * train_ratio)
    train_files = image_files[:split_index]
    val_files = image_files[split_index:]

    print(f"Total images: {len(image_files)}")
    print(f"Training images: {len(train_files)}")
    print(f"Validation images: {len(val_files)}")

    # Function to move files
    def move_files(files, dest_img_dir, dest_lbl_dir):
        moved_count = 0
        for img_file in files:
            # Source paths
            src_img_path = os.path.join(images_dir, img_file)
            
            label_file = os.path.splitext(img_file)[0] + '.txt'
            src_lbl_path = os.path.join(labels_dir, label_file)

            # Destination paths
            dest_img_path = os.path.join(dest_img_dir, img_file)
            dest_lbl_path = os.path.join(dest_lbl_dir, label_file)

            # Move image
            if os.path.exists(src_img_path):
                shutil.move(src_img_path, dest_img_path)
                moved_count += 1
            
            # Move label if it exists
            if os.path.exists(src_lbl_path):
                shutil.move(src_lbl_path, dest_lbl_path)
        return moved_count

    # Move the files
    print("\nMoving training files...")
    moved_train = move_files(train_files, train_img_dir, train_lbl_dir)
    print(f"Moved {moved_train} training image files.")

    print("\nMoving validation files...")
    moved_val = move_files(val_files, val_img_dir, val_lbl_dir)
    print(f"Moved {moved_val} validation image files.")

    print("\nDone!")

if __name__ == '__main__':
    yolo_base_dir = r'd:\\football\\football_yolo'
    split_and_move_dataset(yolo_base_dir)