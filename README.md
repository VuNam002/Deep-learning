# Dự án Nhận diện Đối tượng trong Bóng đá sử dụng YOLO

Dự án này sử dụng mô hình YOLO (You Only Look Once) để phát hiện các đối tượng trong các video hoặc hình ảnh về bóng đá, chẳng hạn như cầu thủ, bóng, trọng tài, và khung thành.

## Mục lục

- [Tính năng](#tính-năng)
- [Cấu trúc Dự án](#cấu-trúc-dự-án)
- [Cài đặt](#cài-đặt)
- [Luồng làm việc](#luồng-làm-việc)
- [Cách sử dụng](#cách-sử-dụng)

## Tính năng

-   **Chuẩn bị dữ liệu**: Các script để chuyển đổi, phân chia và chuẩn bị dữ liệu cho việc huấn luyện mô hình YOLO.
-   **Phân tích dữ liệu**: Phân tích tần suất xuất hiện của các đối tượng và mối tương quan giữa chúng.
-   **Huấn luyện mô hình**: Huấn luyện mô hình YOLO tùy chỉnh trên bộ dữ liệu về bóng đá.
-   **Dự đoán**: Sử dụng mô hình đã huấn luyện để phát hiện đối tượng trên video mới.
-   **Trực quan hóa**: Trực quan hóa dữ liệu và kết quả dự đoán.

## Cấu trúc Dự án

```
.
├── .gitignore
├── analyze_data.py             # Script để phân tích dữ liệu (tần suất, tương quan).
├── create_yolo_format_dataset.py # Script để tạo bộ dữ liệu theo định dạng YOLO.
├── datavisualvision.py         # Script để trực quan hóa dữ liệu.
├── football.yaml                 # File cấu hình cho dataset YOLO (đường dẫn, tên lớp).
├── predict_video.py            # Script để chạy dự đoán trên video.
├── README.md                     # File tài liệu này.
├── split_dataset.py              # Script để chia bộ dữ liệu thành tập train/val/test.
├── analysis_results/             # Thư mục chứa kết quả phân tích dữ liệu.
│   ├── class_correlation.csv
│   └── object_frequency.csv
├── data/                         # Thư mục chứa dữ liệu gốc (hình ảnh, video, annotations).
├── football_yolo/                # Thư mục chứa bộ dữ liệu đã được xử lý theo định dạng YOLO.
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   └── labels/
│       ├── train/
│       └── val/
├── my_results/                   # Thư mục tùy chỉnh để lưu kết quả dự đoán.
├── runs/                         # Thư mục mặc định của YOLO để lưu kết quả huấn luyện và dự đoán.
│   └── detect/
└── visualization_output/         # Thư mục chứa các hình ảnh được trực quan hóa.
```

## Cài đặt

1.  **Clone repository:**
    ```bash
    git clone <your-repository-url>
    cd football
    ```

2.  **Tạo môi trường ảo (khuyến nghị):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    Bạn nên tạo một file `requirements.txt` chứa các thư viện như `ultralytics`, `pandas`, `seaborn`, `opencv-python`.
    ```bash
    pip install -r requirements.txt
    ```

## Luồng làm việc

1.  **Chuẩn bị dữ liệu**: Thu thập hình ảnh/video và gán nhãn cho chúng. Đặt chúng vào thư mục `data/`.
2.  **Tạo bộ dữ liệu YOLO**: Chạy `create_yolo_format_dataset.py` để chuyển đổi dữ liệu gốc sang định dạng YOLO và lưu vào `football_yolo/`.
3.  **Phân chia dữ liệu**: Chạy `split_dataset.py` để tự động chia dữ liệu trong `football_yolo/` thành các tập `train` và `val`.
4.  **Phân tích dữ liệu (Tùy chọn)**: Chạy `analyze_data.py` để hiểu rõ hơn về bộ dữ liệu của bạn.
5.  **Huấn luyện mô hình**: Sử dụng CLI của YOLO hoặc một script tùy chỉnh để bắt đầu quá trình huấn luyện. File `football.yaml` sẽ được dùng để chỉ định đường dẫn dữ liệu.
6.  **Dự đoán**: Sử dụng `predict_video.py` và mô hình đã huấn luyện (thường là file `.pt` trong `runs/train/.../weights/best.pt`) để phát hiện đối tượng trên video mới.

## Cách sử dụng

### 1. Tạo và chuẩn bị Dataset

-   Chạy script để tạo dataset theo định dạng YOLO.
    ```bash
    python create_yolo_format_dataset.py
    ```
-   Chạy script để phân chia dataset.
    ```bash
    python split_dataset.py
    ```

### 2. Huấn luyện mô hình

-   Sử dụng lệnh `yolo` từ thư viện `ultralytics`. Đảm bảo file `football.yaml` đã được cấu hình đúng.
    ```bash
    # Ví dụ huấn luyện với mô hình yolov8n trong 100 epochs
    yolo train data=football.yaml model=yolov8n.pt epochs=100 imgsz=640
    ```
-   Kết quả huấn luyện sẽ được lưu trong thư mục `runs/detect/train/`.

### 3. Chạy dự đoán

-   Chỉnh sửa file `predict_video.py` để trỏ đến video đầu vào và file trọng số (`.pt`) tốt nhất từ quá trình huấn luyện.
    ```bash
    python predict_video.py --source path/to/your/video.mp4 --weights runs/detect/train/weights/best.pt
    ```
-   Kết quả dự đoán sẽ được lưu trong thư mục `my_results/` hoặc `runs/detect/predict/`.

## Video và Ảnh Demo

Đây là video demo kết quả dự đoán của mô hình trên một video bóng đá.

<video controls>
  <source src="video/YOLOv8 Prediction 2025-10-23 22-22-58.mp4" type="video/mp4">
  Your browser does not support the video tag.a
</video>

Và đây là một hình ảnh mẫu:

<img src="video/image.png">
</img>
