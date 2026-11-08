# Dataset
Các file smoke.jsonl là nhiệm vụ kiểm tra luồng do dự án tự soạn, không phải kết quả mô phỏng và không phải benchmark khoa học.
JSONL: task_id duy nhất, domain, difficulty (easy/medium/hard), input, expected_output, split (development/final).
Evaluator MVP so khớp chính xác sau strip; không thực thi mã do model sinh. Coding thực tế cần sandbox và test suite riêng; toán tự do cần rubric, không dùng exact-match thay cho tương đương biểu thức.
Trước nghiên cứu cần dataset đủ mẫu, nguồn/license, khử trùng lặp, rubric độ khó và checksum. Tách development khỏi final theo task family để tránh rò rỉ.
Final không được đưa vào memory hoặc feedback. Chưa cung cấp final benchmark; cần chuẩn bị và khóa trước đo.
