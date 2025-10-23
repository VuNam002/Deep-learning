
import json
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Cấu hình ---
JSON_PATH = "D:\\football\\data\\football\\Match_2023_3_0_subclip\\Match_2023_3_0_subclip.json"
OUTPUT_DIR = "d:\\football\\analysis_results"

def analyze_and_visualize():
    """
    Thực hiện phân tích khám phá dữ liệu (EDA) trên tệp JSON chú thích
    theo một cấu trúc báo cáo chi tiết.
    """
    # --- Bước 1: Đọc tệp dữ liệu ---
    print(f"--- Bước 1: Đọc tệp dữ liệu ---")
    print(f"Đang đọc tệp: {JSON_PATH}")
    try:
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp JSON tại: {JSON_PATH}")
        return
    except json.JSONDecodeError:
        print(f"Lỗi: Tệp JSON không hợp lệ: {JSON_PATH}")
        return
    print("Đọc tệp thành công.")

    # Chuyển đổi các phần của JSON thành DataFrame của Pandas
    images_df = pd.DataFrame(data.get('images', []))
    annotations_df = pd.DataFrame(data.get('annotations', []))
    categories_df = pd.DataFrame(data.get('categories', []))

    # --- Bước 2: Kích thước và Đặc điểm của dữ liệu ---
    print("\n--- Bước 2: Kích thước và Đặc điểm của dữ liệu ---")
    print("\n[Thành phần 'images']")
    print(f"Kích thước: {images_df.shape[0]} dòng, {images_df.shape[1]} cột")
    print(f"Các cột: {', '.join(images_df.columns)}")

    print("\n[Thành phần 'annotations']")
    print(f"Kích thước: {annotations_df.shape[0]} dòng, {annotations_df.shape[1]} cột")
    print(f"Các cột: {', '.join(annotations_df.columns)}")

    print("\n[Thành phần 'categories']")
    print(f"Kích thước: {categories_df.shape[0]} dòng, {categories_df.shape[1]} cột")
    print(f"Các cột: {', '.join(categories_df.columns)}")

    # --- Bước 3: Kiểm tra số lượng giá trị thiếu ---
    print("\n--- Bước 3: Kiểm tra số lượng giá trị thiếu ---")
    
    def check_missing_values(df, name):
        missing_values = df.isnull().sum()
        total_missing = missing_values.sum()
        print(f"\n[Kiểm tra thành phần '{name}']")
        if total_missing == 0:
            print("=> Không có giá trị thiếu.")
        else:
            print("Số lượng giá trị thiếu cho mỗi cột:")
            print(missing_values[missing_values > 0])

    if not images_df.empty:
        check_missing_values(images_df, 'images')
    if not annotations_df.empty:
        check_missing_values(annotations_df, 'annotations')
    if not categories_df.empty:
        check_missing_values(categories_df, 'categories')

    # --- Bước 4: Tổng quan và Trực quan hóa Dữ liệu ---
    print("\n--- Bước 4: Tổng quan và Trực quan hóa Dữ liệu ---")
    
    # Tạo thư mục output nếu chưa có
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Đã tạo thư mục output cho biểu đồ: {OUTPUT_DIR}")

    if annotations_df.empty or categories_df.empty:
        print("\nCảnh báo: Không có đủ dữ liệu 'annotations' hoặc 'categories' để tạo biểu đồ.")
        return
        
    # 1. Biểu đồ cột: Số lượng đối tượng mỗi danh mục
    print("\nĐang tạo biểu đồ phân phối danh mục...")
    merged_df = pd.merge(annotations_df, categories_df, left_on='category_id', right_on='id', how='left')
    category_counts = merged_df['name'].value_counts()

    plt.figure(figsize=(12, 7))
    category_counts.plot(kind='bar')
    plt.title('Số lượng đối tượng trong mỗi danh mục')
    plt.xlabel('Danh mục')
    plt.ylabel('Số lượng')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    bar_chart_path = os.path.join(OUTPUT_DIR, 'category_distribution.png')
    plt.savefig(bar_chart_path)
    print(f"Đã lưu biểu đồ cột tại: {bar_chart_path}")
    plt.close()

    # 2. Biểu đồ đường: Số lượng cầu thủ theo thời gian
    print("\nĐang tạo biểu đồ số lượng cầu thủ theo thời gian...")
    player_category = categories_df[categories_df['name'].str.lower() == 'player']
    if player_category.empty:
        print("Không tìm thấy danh mục 'player' trong dữ liệu để vẽ biểu đồ đường.")
    else:
        player_id = player_category.iloc[0]['id']
        player_annotations = annotations_df[annotations_df['category_id'] == player_id]
        player_count_per_image = player_annotations.groupby('image_id').size().reset_index(name='player_count')
        
        images_df['frame_index'] = images_df['file_name'].str.extract('(\d+)').astype(int)
        
        player_count_full = pd.merge(images_df[['id', 'frame_index']], player_count_per_image, left_on='id', right_on='image_id', how='left').fillna(0)
        player_count_full = player_count_full.sort_values('frame_index')

        plt.figure(figsize=(15, 7))
        plt.plot(player_count_full['frame_index'], player_count_full['player_count'])
        plt.title('Số lượng cầu thủ xuất hiện theo thời gian')
        plt.xlabel('Chỉ số khung hình (Frame Index)')
        plt.ylabel('Số lượng cầu thủ')
        plt.grid(True)
        plt.tight_layout()
        
        line_chart_path = os.path.join(OUTPUT_DIR, 'player_count_over_time.png')
        plt.savefig(line_chart_path)
        print(f"Đã lưu biểu đồ đường tại: {line_chart_path}")
        plt.close()

    print("\nHoàn tất phân tích! Vui lòng kiểm tra kết quả in ra và các tệp trong thư mục:", OUTPUT_DIR)

if __name__ == '__main__':
    analyze_and_visualize()
