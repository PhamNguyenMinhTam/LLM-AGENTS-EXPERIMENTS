# Đánh giá E11 — Memory

Tiêu chí chính: **Accuracy Improvement**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Công thức/cách đo | Đơn vị | Nguồn dữ liệu | Cách diễn giải |
|---|---|---|---|---|---|
| Accuracy Improvement | Chênh lệch accuracy giữa can thiệp và đối chứng | accuracy_intervention − accuracy_control, cùng task và model | điểm tỷ lệ | Phân tích ghép cặp JSONL; adaptation chưa runtime | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Repeated Error Rate | Tỷ lệ lỗi cũ tái diễn trên lần thử sau | số lỗi cùng loại tái diễn / số cơ hội kiểm tra lỗi đã gặp | tỷ lệ | Thủ công: session/task/error labels; chưa adaptation runtime | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Memory Retrieval Accuracy | Tỷ lệ memory truy xuất liên quan và đúng | số mục memory đúng và liên quan / số mục truy xuất; nhãn độc lập trước chấm | tỷ lệ | Chưa triển khai: retrieval trace và nhãn liên quan | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Knowledge Transfer | Chất lượng trên tập mới hoặc ngoài domain | accuracy trên holdout chưa thấy; chênh lệch với đối chứng; không gộp domain chưa chuẩn hóa | tỷ lệ và điểm tỷ lệ | Final holdout khóa độc lập; chưa có bộ dữ liệu nghiên cứu thực | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Stale Memory Errors | Số lỗi có bằng chứng dùng memory lỗi thời | số output sai do mục memory hết hiệu lực / số task có memory; đối chiếu phiên bản nguồn | tỷ lệ | Thủ công: memory snapshot, thời hạn và output; chưa runtime | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Memory Overhead | Chi phí tăng thêm để truy xuất và lưu memory | latency_memory − latency_none; tokens_memory − tokens_none; kích thước snapshot bytes | giây, token, bytes | Chưa triển khai: trace memory và đối chứng ghép cặp | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |

## Diễn giải và kết luận
Thiết kế riêng: Cách ly memory theo agent/session; reset giữa điều kiện; đóng băng memory trước final; cần triển khai runtime.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức None / Short-term / Long-term trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.
