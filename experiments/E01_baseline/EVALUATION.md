# Đánh giá E01 — Baseline Stability

Tiêu chí chính: **Task Accuracy**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Công thức/cách đo | Đơn vị | Nguồn dữ liệu | Cách diễn giải |
|---|---|---|---|---|---|
| Task Accuracy | Tỷ lệ task trả lời đúng theo đáp án/rubric đã đăng ký | sum(score)/N; phân tầng domain/độ khó khi áp dụng; lỗi API có điểm 0 | tỷ lệ [0,1] | Tự động: JSONL exact-match; rubric task khác cần người chấm | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Result Consistency | Mức lặp lại cùng câu trả lời cho cùng task | trung bình theo task của max tần suất output / số lần lặp; báo cáo thêm độ lệch chuẩn accuracy | tỷ lệ và SD | Tự động: JSONL nhóm task, agent, condition | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Mean/Median/P95 Latency | Thời gian từ gửi yêu cầu đến nhận đủ output | perf_counter cuối − đầu; mean, median, P95 nearest-rank | giây | Tự động: latency trong JSONL; gồm mạng và tải model | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Token Usage | Chi phí token và thời gian mỗi task | prompt_eval_count, eval_count và latency; báo riêng từng thành phần | token/task, giây/task | Tự động: Ollama và JSONL; thiếu count ghi null | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| CPU/GPU/RAM/VRAM Usage | Tải xử lý và bộ nhớ trên máy chạy inference | lấy mẫu CPU/GPU %, RAM/VRAM bytes mỗi 100 ms; báo đỉnh và trung bình; ghi chu kỳ lấy mẫu | %, bytes | Chưa tự động: collector trên laptop Ollama; thiếu collector ghi N/A, không dùng RAM controller | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |
| Failure Rate | Tỷ lệ lỗi thực thi API | số run error_type khác null / tổng run; tách câu sai nội dung | tỷ lệ | Tự động: JSONL error_type | Báo từng điều kiện, chênh lệch ghép cặp và CI 95%; xem giới hạn bên dưới. |

## Diễn giải và kết luận
Thiết kế riêng: Chạy ít nhất 5 lần mỗi task; phân tách warm-up khỏi đo chính; ghi trạng thái nóng/lạnh.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức Cùng cấu hình, chạy lặp trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.
