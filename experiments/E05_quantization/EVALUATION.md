# Đánh giá E05 — Quantization

Tiêu chí chính: **Accuracy Degradation**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Công thức/cách đo | Đơn vị | Nguồn dữ liệu | Cách diễn giải |
|---|---|---|---|---|---|
| Accuracy Degradation | Mức giảm so với FP16 cùng trọng số | accuracy_FP16 − accuracy_quantized, trên cùng task | điểm tỷ lệ | Ghép cặp JSONL; FP16 không khả thi ghi N/A | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Task Success Rate | Tỷ lệ task trả lời đúng theo đáp án/rubric đã đăng ký | sum(score)/N; phân tầng domain/độ khó khi áp dụng; lỗi API có điểm 0 | tỷ lệ [0,1] | Tự động: JSONL exact-match; rubric task khác cần người chấm | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Format Validity | Mức thỏa mãn ràng buộc đầu ra | số ràng buộc đạt / tổng ràng buộc; format JSON dùng parser/schema; khóa ràng buộc trước đo | tỷ lệ | Thủ công hoặc validator đã đăng ký; MVP chỉ exact-match, chưa validator tổng quát | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Latency | Thời gian từ gửi yêu cầu đến nhận đủ output | perf_counter cuối − đầu; mean, median, P95 nearest-rank | giây | Tự động: latency trong JSONL; gồm mạng và tải model | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Throughput | Tốc độ sinh token của inference | eval_count / (eval_duration/1e9); tổng hợp median và P95; không chia cho wall latency | token/giây | Tự động: Ollama token_throughput | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Memory Usage | Tải xử lý và bộ nhớ trên máy chạy inference | lấy mẫu CPU/GPU %, RAM/VRAM bytes mỗi 100 ms; báo đỉnh và trung bình; ghi chu kỳ lấy mẫu | %, bytes | Chưa tự động: collector trên laptop Ollama; thiếu collector ghi N/A, không dùng RAM controller | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Result Consistency | Mức lặp lại cùng câu trả lời cho cùng task | trung bình theo task của max tần suất output / số lần lặp; báo cáo thêm độ lệch chuẩn accuracy | tỷ lệ và SD | Tự động: JSONL nhóm task, agent, condition | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |

## Diễn giải và kết luận
Thiết kế riêng: Xuất các mức quantization từ cùng trọng số; xác minh metadata và cấu hình FP16 khả thi.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức Q4 / Q8 / FP16 trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.

## Đối chiếu điều kiện branch
Các mức: q4, q8, fp16. Giữ cấu hình control làm mốc; báo chênh lệch theo task, không gộp lần lặp thành mẫu độc lập.
