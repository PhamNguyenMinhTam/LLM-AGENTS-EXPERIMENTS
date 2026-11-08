# Đánh giá E02 — Model Type

Tiêu chí chính: **Task Accuracy**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Công thức/cách đo | Đơn vị | Nguồn dữ liệu | Cách diễn giải |
|---|---|---|---|---|---|
| Task Accuracy | Tỷ lệ task trả lời đúng theo đáp án/rubric đã đăng ký | sum(score)/N; phân tầng domain/độ khó khi áp dụng; lỗi API có điểm 0 | tỷ lệ [0,1] | Tự động: JSONL exact-match; rubric task khác cần người chấm | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Reasoning Quality | Chất lượng lời giải hiển thị, không suy đoán suy nghĩ ẩn | Hai người chấm mù: 0 sai, 1 đúng một phần, 2 hợp lệ đủ bước; báo trung bình/2 và tỷ lệ điểm 2 | điểm [0,2], tỷ lệ | Thủ công: output có lời giải và rubric task; không phù hợp prompt chỉ đáp án | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Instruction Following | Mức thỏa mãn ràng buộc đầu ra | số ràng buộc đạt / tổng ràng buộc; format JSON dùng parser/schema; khóa ràng buộc trước đo | tỷ lệ | Thủ công hoặc validator đã đăng ký; MVP chỉ exact-match, chưa validator tổng quát | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Hallucination Rate | Tỷ lệ khẳng định có thể kiểm chứng nhưng sai hoặc không được nguồn hỗ trợ | số khẳng định sai/không hỗ trợ / số khẳng định kiểm chứng; mẫu không có khẳng định ghi N/A | tỷ lệ | Thủ công: hai người chấm mù và nguồn kiểm chứng lưu kèm | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Latency | Thời gian từ gửi yêu cầu đến nhận đủ output | perf_counter cuối − đầu; mean, median, P95 nearest-rank | giây | Tự động: latency trong JSONL; gồm mạng và tải model | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Token Efficiency | Số task thành công trên tổng token sinh | sum(success)/sum(output_tokens); báo thêm prompt tokens | task đúng/token | Tổng hợp JSONL; thiếu token ghi N/A | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Result Consistency | Mức lặp lại cùng câu trả lời cho cùng task | trung bình theo task của max tần suất output / số lần lặp; báo cáo thêm độ lệch chuẩn accuracy | tỷ lệ và SD | Tự động: JSONL nhóm task, agent, condition | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |

## Diễn giải và kết luận
Thiết kế riêng: Chọn tag thực tế; ghép kích thước và quantization gần nhau; ghi chênh lệch còn lại.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức Qwen / Llama / Gemma trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.
