# Đánh giá E07 — Domain

Tiêu chí chính: **Domain Accuracy**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Công thức/cách đo | Đơn vị | Nguồn dữ liệu | Cách diễn giải |
|---|---|---|---|---|---|
| Domain Accuracy | Tỷ lệ task trả lời đúng theo đáp án/rubric đã đăng ký | sum(score)/N; phân tầng domain/độ khó khi áp dụng; lỗi API có điểm 0 | tỷ lệ [0,1] | Tự động: JSONL exact-match; rubric task khác cần người chấm | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Specialization Gain | Chênh lệch accuracy giữa can thiệp và đối chứng | accuracy_intervention − accuracy_control, cùng task và model | điểm tỷ lệ | Phân tích ghép cặp JSONL; adaptation chưa runtime | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Instruction Following | Mức thỏa mãn ràng buộc đầu ra | số ràng buộc đạt / tổng ràng buộc; format JSON dùng parser/schema; khóa ràng buộc trước đo | tỷ lệ | Thủ công hoặc validator đã đăng ký; MVP chỉ exact-match, chưa validator tổng quát | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Generalization | Chất lượng trên tập mới hoặc ngoài domain | accuracy trên holdout chưa thấy; chênh lệch với đối chứng; không gộp domain chưa chuẩn hóa | tỷ lệ và điểm tỷ lệ | Final holdout khóa độc lập; chưa có bộ dữ liệu nghiên cứu thực | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Cross-Domain Performance | Chất lượng trên tập mới hoặc ngoài domain | accuracy trên holdout chưa thấy; chênh lệch với đối chứng; không gộp domain chưa chuẩn hóa | tỷ lệ và điểm tỷ lệ | Final holdout khóa độc lập; chưa có bộ dữ liệu nghiên cứu thực | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Token/Latency Cost | Chi phí token và thời gian mỗi task | prompt_eval_count, eval_count và latency; báo riêng từng thành phần | token/task, giây/task | Tự động: Ollama và JSONL; thiếu count ghi null | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |

## Diễn giải và kết luận
Thiết kế riêng: So generalist/specialist trong từng domain trước; đánh giá thêm domain ngoài chuyên môn trên tập chuẩn hóa.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức Generalist / Specialist trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.

## Đối chiếu điều kiện branch
Các mức: mathematics-generalist, mathematics-specialist, coding-generalist, coding-specialist, classification-generalist, classification-specialist. Giữ cấu hình control làm mốc; báo chênh lệch theo task, không gộp lần lặp thành mẫu độc lập.
