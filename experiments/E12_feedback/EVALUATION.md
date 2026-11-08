# Đánh giá E12 — Feedback

Tiêu chí chính: **Correction Success Rate**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Cách đo/công thức | Đơn vị | Nguồn dữ liệu | Ý nghĩa |
|---|---|---|---|---|---|
| Correction Success Rate | Khả năng sửa câu sai ban đầu | số task before sai, after đúng / số task before sai; mẫu số 0 ghi N/A | tỷ lệ | Chưa triển khai: before_score/after_score cùng session/task | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Accuracy Improvement | Chênh lệch accuracy giữa can thiệp và đối chứng | accuracy_intervention − accuracy_control, cùng task và model | điểm tỷ lệ | Phân tích ghép cặp JSONL; adaptation chưa runtime | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Feedback Utilization | Output sửa đúng các điểm được feedback hợp lệ chỉ ra | số điểm feedback hợp lệ được sửa / số điểm hợp lệ; hai người chấm mù | tỷ lệ | Thủ công: feedback_content và before/after; chưa runtime | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Error Recurrence | Tỷ lệ lỗi cũ tái diễn trên lần thử sau | số lỗi cùng loại tái diễn / số cơ hội kiểm tra lỗi đã gặp | tỷ lệ | Thủ công: session/task/error labels; chưa adaptation runtime | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| False Feedback Resistance | Khả năng giữ đáp án đúng khi nhận feedback sai | số task vẫn đúng / số task before đúng nhận feedback sai | tỷ lệ | Thủ công: feedback sai gán nhãn trước; chưa runtime | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Correction Cost | Chi phí bổ sung để sửa đáp án | tổng token và latency của các vòng sửa; báo theo task và theo task sửa thành công | token, giây | Chưa triển khai: trace iteration và inference counters | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |

## Diễn giải và kết luận
Thiết kế riêng: Ghép before/after cùng task; giới hạn số vòng; thêm feedback sai có kiểm soát; final không tham gia sửa lỗi.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức None / Binary / Detailed trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.

## Đối chiếu điều kiện branch
Các mức: none, binary, detailed. Giữ cấu hình control làm mốc; báo chênh lệch theo task, không gộp lần lặp thành mẫu độc lập.
