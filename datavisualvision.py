# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
# import glob

# # Ensure the output directory exists
# output_dir = 'visualization_output'
# os.makedirs(output_dir, exist_ok=True)

# # --- Visualize Object Frequency ---
# try:
#     freq_df = pd.read_csv('analysis_results/object_frequency.csv')
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x='class', y='count', data=freq_df)
#     plt.title('Tần suất xuất hiện của đối tượng')
#     plt.xlabel('Lớp đối tượng')
#     plt.ylabel('Số lượng')
#     plt.xticks(rotation=45)
#     freq_chart_path = os.path.join(output_dir, 'object_frequency_distribution.png')
#     plt.savefig(freq_chart_path)
#     plt.close()
# except Exception:
#     pass

# # --- Visualize Class Correlation ---
# try:
#     corr_df = pd.read_csv('analysis_results/class_correlation.csv', index_col=0)
#     plt.figure(figsize=(8, 6))
#     sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f")
#     plt.title('Bản đồ nhiệt tương quan giữa các lớp')
#     corr_heatmap_path = os.path.join(output_dir, 'class_correlation_heatmap.png')
#     plt.savefig(corr_heatmap_path)
#     plt.close()
# except Exception:
#     pass

# # --- Visualize Objects Per Image ---
# try:
#     label_files = glob.glob('football_yolo/train/labels/*.txt')
#     objects_per_image = []
#     for file_path in label_files:
#         with open(file_path, 'r') as f:
#             objects_per_image.append(len(f.readlines()))

#     plt.figure(figsize=(12, 7))
#     if objects_per_image:
#         plt.hist(objects_per_image, bins=range(min(objects_per_image), max(objects_per_image) + 2), edgecolor='black', align='left')
#     plt.title('Phân bố số lượng đối tượng trên mỗi ảnh')
#     plt.xlabel('Số lượng đối tượng')
#     plt.ylabel('Số lượng ảnh')
#     plt.grid(axis='y', alpha=0.75)
#     plt.xticks(range(min(objects_per_image), max(objects_per_image) + 1))

#     objects_per_image_path = os.path.join(output_dir, 'objects_per_image_distribution.png')
#     plt.savefig(objects_per_image_path)
#     plt.close()
# except Exception:
#     pass



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
# import glob
# import cv2
# import random

# # Ensure the output directory exists
# output_dir = 'visualization_output'
# os.makedirs(output_dir, exist_ok=True)

# # --- Visualize Object Frequency ---
# try:
#     freq_df = pd.read_csv('analysis_results/object_frequency.csv')
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x='class', y='count', data=freq_df)
#     plt.title('Tần suất xuất hiện của đối tượng')
#     plt.xlabel('Lớp đối tượng')
#     plt.ylabel('Số lượng')
#     plt.xticks(rotation=45)
#     freq_chart_path = os.path.join(output_dir, 'object_frequency_distribution.png')
#     plt.savefig(freq_chart_path)
#     plt.close()
# except Exception as e:
#     print("❌ Lỗi phần Object Frequency:", e)

# # --- Visualize Class Correlation ---
# try:
#     corr_df = pd.read_csv('analysis_results/class_correlation.csv', index_col=0)
#     plt.figure(figsize=(8, 6))
#     sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt=".2f")
#     plt.title('Bản đồ nhiệt tương quan giữa các lớp')
#     corr_heatmap_path = os.path.join(output_dir, 'class_correlation_heatmap.png')
#     plt.savefig(corr_heatmap_path)
#     plt.close()
# except Exception as e:
#     print("❌ Lỗi phần Class Correlation:", e)

# # --- Visualize Objects Per Image ---
# try:
#     label_files = glob.glob('football_yolo/train/labels/*.txt')
#     objects_per_image = []
#     for file_path in label_files:
#         with open(file_path, 'r') as f:
#             objects_per_image.append(len(f.readlines()))

#     plt.figure(figsize=(12, 7))
#     if objects_per_image:
#         plt.hist(objects_per_image, bins=range(min(objects_per_image), max(objects_per_image) + 2), 
#                  edgecolor='black', align='left')
#     plt.title('Phân bố số lượng đối tượng trên mỗi ảnh')
#     plt.xlabel('Số lượng đối tượng')
#     plt.ylabel('Số lượng ảnh')
#     plt.grid(axis='y', alpha=0.75)
#     plt.xticks(range(min(objects_per_image), max(objects_per_image) + 1))

#     objects_per_image_path = os.path.join(output_dir, 'objects_per_image_distribution.png')
#     plt.savefig(objects_per_image_path)
#     plt.close()
# except Exception as e:
#     print("❌ Lỗi phần Objects Per Image:", e)


# # --- 🖼️ Visualize Sample YOLO Images with Bounding Boxes ---
# try:
#     img_dir = 'football_yolo/train/images'
#     label_dir = 'football_yolo/train/labels'
#     sample_output_dir = os.path.join(output_dir, 'sample_images')
#     os.makedirs(sample_output_dir, exist_ok=True)

#     # (Tùy chọn) nếu bạn có file data.yaml chứa tên class thì có thể đọc nó
#     # Tạm thời đặt tên class mặc định:
#     class_names = ["class_0", "class_1", "class_2", "class_3", "class_4"]

#     img_files = glob.glob(os.path.join(img_dir, '*.jpg')) + glob.glob(os.path.join(img_dir, '*.png'))
#     sample_files = random.sample(img_files, min(5, len(img_files)))  # Lấy ngẫu nhiên 5 ảnh

#     for img_path in sample_files:
#         label_path = os.path.join(label_dir, os.path.splitext(os.path.basename(img_path))[0] + '.txt')

#         img = cv2.imread(img_path)
#         if img is None:
#             continue

#         h, w, _ = img.shape
#         if not os.path.exists(label_path):
#             continue

#         with open(label_path, 'r') as f:
#             for line in f:
#                 cls, x, y, bw, bh = map(float, line.strip().split())
#                 x1 = int((x - bw / 2) * w)
#                 y1 = int((y - bh / 2) * h)
#                 x2 = int((x + bw / 2) * w)
#                 y2 = int((y + bh / 2) * h)
#                 class_name = class_names[int(cls)] if int(cls) < len(class_names) else f"class_{int(cls)}"

#                 color = (0, 255, 0)
#                 cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
#                 cv2.putText(img, class_name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

#         # Lưu ảnh trực quan
#         save_path = os.path.join(sample_output_dir, os.path.basename(img_path))
#         cv2.imwrite(save_path, img)

#     print(f"✅ Đã tạo {len(sample_files)} ảnh trực quan trong thư mục: {sample_output_dir}")

# except Exception as e:
#     print("❌ Lỗi phần trực quan hình ảnh:", e)




# import random

# image_dir = 'football_yolo/train/images'
# label_dir = 'football_yolo/train/labels'
# sample_paths = random.sample(glob.glob(os.path.join(image_dir, '*.jpg')), 5)

# for img_path in sample_paths:
#     file_name = os.path.basename(img_path).replace('.jpg', '.txt')
#     label_path = os.path.join(label_dir, file_name)

#     img = cv2.imread(img_path)
#     h, w = img.shape[:2]

#     if os.path.exists(label_path):
#         with open(label_path, 'r') as f:
#             for line in f:
#                 cls, x, y, bw, bh = map(float, line.split())
#                 x1, y1 = int((x - bw / 2) * w), int((y - bh / 2) * h)
#                 x2, y2 = int((x + bw / 2) * w), int((y + bh / 2) * h)
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
#                 cv2.putText(img, str(int(cls)), (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

#     plt.figure(figsize=(8,6))
#     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     plt.axis('off')
#     plt.title('Ảnh + bounding box')
#     plt.savefig(os.path.join(output_dir, f'sample_with_bbox_{os.path.basename(img_path)}.png'))
#     plt.close()

# plt.figure(figsize=(8, 8))
# plt.pie(freq_df['count'], labels=freq_df['class'], autopct='%1.1f%%', startangle=90)
# plt.title('Tỉ lệ phần trăm đối tượng theo lớp')
# plt.savefig(os.path.join(output_dir, 'object_class_ratio_pie.png'))
# plt.close()




# centers_x, centers_y = [], []
# for file_path in glob.glob('football_yolo/train/labels/*.txt'):
#     with open(file_path, 'r') as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 5:
#                 _, x, y, _, _ = map(float, parts)
#                 centers_x.append(x)
#                 centers_y.append(y)

# plt.figure(figsize=(6,6))
# sns.kdeplot(x=centers_x, y=centers_y, fill=True, cmap='mako')
# plt.title('Phân bố vị trí trung tâm của đối tượng')
# plt.xlabel('Tọa độ X (chuẩn hóa)')
# plt.ylabel('Tọa độ Y (chuẩn hóa)')
# plt.savefig(os.path.join(output_dir, 'bbox_center_heatmap.png'))
# plt.close()





# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import glob


# brightness = []
# contrast = []

# for path in glob.glob('football_yolo/train/images/*.jpg'):
#     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#     if img is not None:
#         brightness.append(np.mean(img))
#         contrast.append(np.std(img))

# plt.figure(figsize=(8,6))
# sns.scatterplot(x=brightness, y=contrast)
# plt.title('Phân bố độ sáng và tương phản ảnh')
# plt.xlabel('Brightness (mean pixel)')
# plt.ylabel('Contrast (std pixel)')
# plt.grid(True)
# plt.savefig('visualization_output/image_brightness_contrast.png')
# plt.close()




# import matplotlib.pyplot as plt
# import glob
# import os

# label_files = sorted(glob.glob('football_yolo/train/labels/*.txt'))

# objects_per_frame = []
# frame_ids = []

# # for i, file_path in enumerate(label_files):
# #     with open(file_path, 'r') as f:
# #         count = len(f.readlines())
# #         objects_per_frame.append(count)
# #         frame_ids.append(i)

# # plt.figure(figsize=(12,6))
# # plt.plot(frame_ids, objects_per_frame, lw=1)
# # plt.title('Số lượng đối tượng qua từng frame')
# # plt.xlabel('Chỉ số frame (thời gian)')
# # plt.ylabel('Số lượng đối tượng')
# # plt.grid(True)
# # plt.savefig(os.path.join('visualization_output', 'objects_per_frame.png'))
# # plt.close()



# # import numpy as np
# # import matplotlib.pyplot as plt

# # ball_positions = []

# # for file_path in label_files:
# #     with open(file_path, 'r') as f:
# #         for line in f:
# #             cls, x, y, _, _ = map(float, line.strip().split())
# #             if int(cls) == 0:  # ví dụ 0 là 'ball'
# #                 ball_positions.append((x, y))

# # ball_positions = np.array(ball_positions)
# # plt.figure(figsize=(6,6))
# # plt.plot(ball_positions[:,0], ball_positions[:,1], 'o-', alpha=0.5)
# # plt.title('Quỹ đạo di chuyển của bóng qua các frame')
# # plt.xlabel('Tọa độ X (chuẩn hóa)')
# # plt.ylabel('Tọa độ Y (chuẩn hóa)')
# # plt.gca().invert_yaxis()  # y tăng từ trên xuống trong YOLO
# # plt.savefig(os.path.join('visualization_output', 'ball_trajectory.png'))
# # plt.close()



# import os
# import numpy as np
# import matplotlib.pyplot as plt

# label_dir = 'football_yolo/train/labels'
# label_files = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith('.txt')]

# # --- 1. Lấy vị trí bóng từ các file YOLO ---
# ball_positions = []
# for file_path in label_files:
#     with open(file_path, 'r') as f:
#         for line in f:
#             cls, x, y, _, _ = map(float, line.strip().split())
#             if int(cls) == 0:  # ví dụ 0 là bóng
#                 ball_positions.append((x, y))

# ball_positions = np.array(ball_positions)

# # --- 2. Vẽ quỹ đạo bóng ---
# plt.figure(figsize=(6,6))
# plt.plot(ball_positions[:,0], ball_positions[:,1], 'o-', alpha=0.5)
# plt.title('Quỹ đạo di chuyển của bóng qua các frame')
# plt.xlabel('Tọa độ X (chuẩn hóa)')
# plt.ylabel('Tọa độ Y (chuẩn hóa)')
# plt.gca().invert_yaxis()  # hệ trục YOLO: Y tăng từ trên xuống
# os.makedirs('visualization_output', exist_ok=True)
# plt.savefig(os.path.join('visualization_output', 'ball_trajectory.png'))
# plt.close()

# # --- 3. Tính vận tốc & tốc độ ---
# vx, vy, speed = [], [], []
# for i in range(1, len(ball_positions)):
#     dx = ball_positions[i,0] - ball_positions[i-1,0]
#     dy = ball_positions[i,1] - ball_positions[i-1,1]
#     vx.append(dx)
#     vy.append(dy)
#     speed.append(np.sqrt(dx**2 + dy**2))

# # --- 4. Vẽ biểu đồ tốc độ ---
# plt.figure(figsize=(10,4))
# plt.plot(speed, color='blue', linewidth=1.5)
# plt.title('Tốc độ di chuyển (chuẩn hóa) của bóng qua các frame')
# plt.xlabel('Frame')
# plt.ylabel('Tốc độ')
# plt.grid(True)
# plt.savefig(os.path.join('visualization_output', 'ball_speed_over_time.png'))
# plt.close()
