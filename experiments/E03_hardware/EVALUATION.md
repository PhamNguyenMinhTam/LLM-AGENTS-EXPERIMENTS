# Đánh giá E03 — Hardware

Tiêu chí chính: **Inference Throughput**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Cách đo/công thức | Đơn vị | Nguồn dữ liệu | Ý nghĩa |
|---|---|---|---|---|---|
| Inference Throughput | Tốc độ sinh token của inference | eval_count / (eval_duration/1e9); tổng hợp median và P95; không chia cho wall latency | token/giây | Tự động: Ollama token_throughput | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi thiếu trường dữ liệu hoặc mẫu số bằng 0. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Time to First Token | Khoảng từ gửi request đến token nội dung đầu tiên | đo timestamp chunk đầu có content − timestamp gửi trong streaming client | giây | Chưa triển khai: runtime dùng stream=false nên N/A | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Total Latency | Thời gian từ gửi yêu cầu đến nhận đủ output | perf_counter cuối − đầu; mean, median, P95 nearest-rank | giây | Tự động: latency trong JSONL; gồm mạng và tải model | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi thiếu trường dữ liệu hoặc mẫu số bằng 0. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| CPU/GPU Utilization | Tải xử lý và bộ nhớ trên máy chạy inference | lấy mẫu CPU/GPU %, RAM/VRAM bytes mỗi 100 ms; báo đỉnh và trung bình; ghi chu kỳ lấy mẫu | %, bytes | Chưa tự động: collector trên laptop Ollama; thiếu collector ghi N/A, không dùng RAM controller | Định lượng hiệu quả sử dụng tài nguyên. Không có chiều tốt tuyệt đối; xét cùng chất lượng và latency. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Peak RAM/VRAM | Tải xử lý và bộ nhớ trên máy chạy inference | lấy mẫu CPU/GPU %, RAM/VRAM bytes mỗi 100 ms; báo đỉnh và trung bình; ghi chu kỳ lấy mẫu | %, bytes | Chưa tự động: collector trên laptop Ollama; thiếu collector ghi N/A, không dùng RAM controller | Định lượng hiệu quả sử dụng tài nguyên. Không có chiều tốt tuyệt đối; xét cùng chất lượng và latency. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Energy per Task | Năng lượng hoặc hiệu quả trên năng lượng | J/task = tích phân công suất theo thời gian; efficiency = số task đúng / tổng J | J/task hoặc task đúng/J | Thiết bị đo hoặc RAPL/GPU power đã hiệu chuẩn; không có ghi N/A | Kiểm tra chi phí năng lượng để hoàn thành task. Thấp hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Task Accuracy | Tỷ lệ task trả lời đúng theo đáp án/rubric đã đăng ký | sum(score)/N; phân tầng domain/độ khó khi áp dụng; lỗi API có điểm 0 | tỷ lệ [0,1] | Tự động: JSONL exact-match; rubric task khác cần người chấm | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi thiếu trường dữ liệu hoặc mẫu số bằng 0. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |

## Diễn giải và kết luận
Thiết kế riêng: Dùng cùng digest trên hai máy; cố định chế độ nguồn, nhiệt độ, backend và số luồng.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức Chip X / Chip Y trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.

## Đối chiếu điều kiện branch
Các mức: hardware-x, hardware-y. Giữ cấu hình control làm mốc; báo chênh lệch theo task, không gộp lần lặp thành mẫu độc lập.
