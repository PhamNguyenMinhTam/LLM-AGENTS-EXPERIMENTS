# Đánh giá E09 — Prompt Strategy

Tiêu chí chính: **Task Accuracy**. Các tiêu chí còn lại là phụ, không chọn lại metric chính sau khi xem kết quả.

| Tiêu chí | Định nghĩa | Cách đo/công thức | Đơn vị | Nguồn dữ liệu | Ý nghĩa |
|---|---|---|---|---|---|
| Task Accuracy | Tỷ lệ task trả lời đúng theo đáp án/rubric đã đăng ký | sum(score)/N; phân tầng domain/độ khó khi áp dụng; lỗi API có điểm 0 | tỷ lệ [0,1] | Tự động: JSONL exact-match; rubric task khác cần người chấm | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi thiếu trường dữ liệu hoặc mẫu số bằng 0. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Instruction Following | Mức thỏa mãn ràng buộc đầu ra | số ràng buộc đạt / tổng ràng buộc; format JSON dùng parser/schema; khóa ràng buộc trước đo | tỷ lệ | Thủ công hoặc validator đã đăng ký; MVP chỉ exact-match, chưa validator tổng quát | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Format Compliance | Mức thỏa mãn ràng buộc đầu ra | số ràng buộc đạt / tổng ràng buộc; format JSON dùng parser/schema; khóa ràng buộc trước đo | tỷ lệ | Thủ công hoặc validator đã đăng ký; MVP chỉ exact-match, chưa validator tổng quát | Kiểm chứng lợi ích về chất lượng hoặc hiệu quả. Cao hơn thường tốt. N/A khi chưa có collector/trace/rubric cần thiết. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Prompt Sensitivity | Biến động accuracy giữa prompt đã đăng ký | max accuracy − min accuracy; cùng task và ngân sách | điểm tỷ lệ | Phân tích ghép cặp JSONL theo prompt_version | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi thiếu trường dữ liệu hoặc mẫu số bằng 0. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Token Usage | Chi phí token và thời gian mỗi task | prompt_eval_count, eval_count và latency; báo riêng từng thành phần | token/task, giây/task | Tự động: Ollama và JSONL; thiếu count ghi null | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi thiếu trường dữ liệu hoặc mẫu số bằng 0. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |
| Latency | Thời gian từ gửi yêu cầu đến nhận đủ output | perf_counter cuối − đầu; mean, median, P95 nearest-rank | giây | Tự động: latency trong JSONL; gồm mạng và tải model | Kiểm tra chi phí hoặc rủi ro của điều kiện. Thấp hơn thường tốt. N/A khi thiếu trường dữ liệu hoặc mẫu số bằng 0. Kết luận từ chênh lệch ghép cặp và CI 95%, không từ giá trị đơn lẻ. |

## Diễn giải và kết luận
Thiết kế riêng: Lưu nguyên văn từng prompt và phiên bản; ví dụ few-shot chỉ lấy từ development, không lấy final.
Accuracy, consistency, throughput, utilization đúng công cụ và resistance thường cao hơn là tốt; latency, tài nguyên, tỷ lệ lỗi và chi phí thường thấp hơn là tốt. CPU/GPU utilization cao không tự chứng minh hiệu quả; phải xét throughput và chất lượng cùng lúc.
So các mức Zero-shot / Few-shot / Structured trên cùng task và cùng split. Bootstrap 10.000 lần theo task (không theo từng repetition), báo CI 95% cho chênh lệch; giữ các lần lặp cùng task trong một cụm. E06 báo hiệu ứng tương tác trên đủ ô factorial. Đăng ký ngưỡng khác biệt có ý nghĩa thực tiễn trước khi đo; điều chỉnh Holm khi kiểm định nhiều cặp.
Rubric thủ công: hai người chấm mù điều kiện; lưu điểm độc lập, tỷ lệ đồng thuận, giải quyết bất đồng bằng người thứ ba. Không dùng model tự chấm làm chân lý duy nhất.
Mẫu số bằng 0 hoặc thiếu thiết bị đo ghi N/A/null kèm lý do, không thay bằng 0. Metrics ghi “chưa triển khai” không có trong summary tự động; cần collector, trace hoặc quy trình chấm ngoài trước khi công bố.
Không có dữ liệu: chưa kết luận. Nếu CI rộng hoặc điều kiện không khả thi, báo không đủ bằng chứng thay vì xếp hạng model.

## Đối chiếu điều kiện branch
Các mức: zero-shot, few-shot, structured. Giữ cấu hình control làm mốc; báo chênh lệch theo task, không gộp lần lặp thành mẫu độc lập.
