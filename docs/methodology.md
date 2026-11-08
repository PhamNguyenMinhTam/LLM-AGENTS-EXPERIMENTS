# Phương pháp
Đăng ký giả thuyết, metric chính, cỡ mẫu từ power analysis/pilot, quy tắc dừng và ngân sách trước đo. Smoke tasks chỉ kiểm tra kỹ thuật.
Ghép cặp cùng task, giữ nguyên yếu tố ngoài biến độc lập. Đổi model có thể kéo theo tokenizer/context; phải ghi rõ nhiễu còn lại.
Warm-up riêng, ghi cold/warm, nhiệt độ và chế độ nguồn. Lặp tối thiểu theo protocol; không coi repeated runs là mẫu task độc lập.
Lưu model digest, quantization, config đã resolve, dataset checksum và commit. Commit sạch trước benchmark; manifest ghi dirty nếu có thay đổi.
Phân tích accuracy ghép cặp với bootstrap 10.000 lần theo task, CI 95%; latency báo median/P95 và hiệu số ghép cặp. Chưa có script bootstrap/plot trong MVP; cần triển khai trước báo cáo khoa học.
Chấm mù bởi hai người cho metrics định tính. Báo mọi lỗi/OOM và cấu hình không khả thi. Không so domain khác nhau để xếp hạng model nếu chưa chuẩn hóa.
Tách development/final theo nhóm task; không huấn luyện, tạo few-shot, memory hoặc feedback từ final. E11/E12 cần đóng băng trạng thái trước final.
