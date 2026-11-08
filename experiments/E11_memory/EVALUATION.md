# Đánh giá E11 — Memory

Tiêu chí chính: **Accuracy Improvement**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Cách đo/công thức | Đơn vị | Nguồn dữ liệu | Ý nghĩa |
|---|---|---|---|---|---|
| Accuracy Improvement | Chênh lệch accuracy giữa can thiệp và đối chứng | accuracy_intervention − accuracy_control, cùng task và model | điểm tỷ lệ | Phân tích ghép cặp JSONL; adaptation chưa runtime | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Repeated Error Rate | Tỷ lệ lỗi cũ tái diễn trên lần thử sau | số lỗi cùng loại tái diễn / số cơ hội kiểm tra lỗi đã gặp | tỷ lệ | Thủ công: session/task/error labels; chưa adaptation runtime | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Memory Retrieval Accuracy | Tỷ lệ memory truy xuất liên quan và đúng | số mục memory đúng và liên quan / số mục truy xuất; nhãn độc lập trước chấm | tỷ lệ | Chưa triển khai: retrieval trace và nhãn liên quan | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Knowledge Transfer | Chất lượng trên tập mới hoặc ngoài domain | accuracy trên holdout chưa thấy; chênh lệch với đối chứng; không gộp domain chưa chuẩn hóa | tỷ lệ và điểm tỷ lệ | Final holdout khóa độc lập; chưa có bộ dữ liệu nghiên cứu thực | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Stale Memory Errors | Số lỗi có bằng chứng dùng memory lỗi thời | số output sai do mục memory hết hiệu lực / số task có memory; đối chiếu phiên bản nguồn | tỷ lệ | Thủ công: memory snapshot, thời hạn và output; chưa runtime | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Memory Overhead | Chi phí tăng thêm để truy xuất và lưu memory | latency_memory − latency_none; tokens_memory − tokens_none; kích thước snapshot bytes | giây, token, bytes | Chưa triển khai: trace memory và đối chứng ghép cặp | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |

## Diễn giải và kết luận
Thiết kế riêng: Cách ly memory theo agent/session; reset giữa điều kiện; đóng băng memory trước final; cần triển khai runtime.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức None / Short-term / Long-term trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.

## Đối chiếu điều kiện branch
Các mức: none, short-term, long-term. Giữ cấu hình control làm mốc; báo chênh lệch theo task, không gộp lần lặp thành mẫu độc lập.
