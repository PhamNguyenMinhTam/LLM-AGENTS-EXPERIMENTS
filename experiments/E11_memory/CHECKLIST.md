# Checklist E11

## A. Preparation
- [ ] Xác định giả thuyết.
- [ ] Xác định biến độc lập.
- [ ] Xác định biến phụ thuộc.
- [ ] Xác định biến kiểm soát.
- [ ] Chuẩn bị cấu hình thử nghiệm.
- [ ] Chuẩn bị dataset.
- [ ] Kiểm tra công cụ chấm điểm.
- [ ] Cách ly memory theo agent/session; reset giữa điều kiện; đóng băng memory trước final; cần triển khai runtime..

## B. Execution
- [ ] Kiểm tra phần cứng và môi trường.
- [ ] Xác minh model và cấu hình inference.
- [ ] Thực hiện từng cấu hình thử nghiệm.
- [ ] Chạy lặp theo kế hoạch.
- [ ] Lưu logs và kết quả từng run.
- [ ] Kiểm tra lỗi thực thi.
- [ ] Đối chiếu các mức None / Short-term / Long-term và lưu manifest từng mức.

## C. Evaluation
- [ ] Tính metrics chính.
- [ ] Tính metrics phụ.
- [ ] So sánh các cấu hình.
- [ ] Thống kê độ biến động.
- [ ] Phân tích lỗi.
- [ ] Vẽ biểu đồ kết quả.
- [ ] Chấm riêng Repeated Error Rate theo EVALUATION.md.

## D. Conclusion
- [ ] Đối chiếu giả thuyết.
- [ ] Xác định kết luận được dữ liệu hỗ trợ.
- [ ] Ghi nhận hạn chế.
- [ ] Lưu phiên bản model, code và config.
- [ ] Cập nhật research log.
- [ ] Hoàn thành báo cáo thí nghiệm.

## Kiểm tra bổ sung theo yêu cầu triển khai

- [ ] Chọn và ghi rõ model, hardware, domain cho từng điều kiện.
- [ ] Kiểm tra config trước chạy.
- [ ] Chạy baseline liên quan trước các điều kiện so sánh.
- [ ] Xác minh tính toàn vẹn dữ liệu bằng checksum và số run.
- [ ] Tính trung bình, độ phân tán và phân tích kết quả.
- [ ] Chuẩn bị memory store và nhãn retrieval.
- [ ] Tách experience dataset khỏi final evaluation.
- [ ] Kiểm tra retrieval và lỗi do memory cũ.

## E. Điều kiện branch
- [ ] Kiểm tra và thực thi điều kiện none.
- [ ] Kiểm tra và thực thi điều kiện short-term.
- [ ] Kiểm tra và thực thi điều kiện long-term.
