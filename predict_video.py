import cv2
from ultralytics import YOLO

# Đường dẫn đến mô hình đã huấn luyện
MODEL_PATH = 'd:/football/runs/detect/train4/weights/best.pt'

# Đường dẫn đến video đầu vào
VIDEO_PATH = 'D:/football/data/football/Match_1951_1_0_subclip/Match_1951_1_0_subclip.mp4'

# Tải mô hình YOLO
model = YOLO(MODEL_PATH)

# Mở tệp video
cap = cv2.VideoCapture(VIDEO_PATH)

# Kiểm tra xem video có được mở thành công không
if not cap.isOpened():
    print("Lỗi: Không thể mở tệp video.")
    exit()

# Tạo một cửa sổ có tên và đặt nó ở chế độ toàn màn hình
WINDOW_NAME = "YOLOv8 Prediction"
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Lặp qua các khung hình của video
frame_count = 0
while True:
    # Đọc một khung hình từ video
    ret, frame = cap.read()

    # Nếu không còn khung hình nào, thoát khỏi vòng lặp
    if not ret:
        print("Đã xử lý xong video hoặc có lỗi khi đọc khung hình.")
        break

    frame_count += 1
    print(f"Đang xử lý khung hình số: {frame_count}")

    # Chạy dự đoán trên khung hình với ngưỡng tin cậy thấp hơn
    results = model(frame, conf=0.1)

    # Vẽ các hộp giới hạn và nhãn lên khung hình
    annotated_frame = results[0].plot()

    # Hiển thị khung hình trong cửa sổ toàn màn hình
    cv2.imshow(WINDOW_NAME, annotated_frame)

    # Nhấn 'q' để thoát khỏi vòng lặp
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
