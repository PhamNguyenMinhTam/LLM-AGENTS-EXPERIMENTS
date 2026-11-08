# Dữ liệu kết quả
Runner ghi `raw/E##/<run_id>/runs.jsonl`, `summary.csv`, `manifest.json` trong cùng thư mục run để bảo toàn nguồn gốc. Sao chép bảng tổng hợp đã rà soát vào summary/ nếu cần; figures/ dành cho biểu đồ.
Chưa có kết quả thực nghiệm. Raw và bảng tự sinh bị gitignore. Chỉ công bố dữ liệu đã khử thông tin nhạy cảm; lưu bản gốc trong kho dữ liệu riêng, có checksum và kiểm soát truy cập.
Null nghĩa chưa đo, không phải mức sử dụng bằng 0. P95 là nearest-rank; accuracy gồm cả run lỗi để tránh thiên lệch loại mẫu.
