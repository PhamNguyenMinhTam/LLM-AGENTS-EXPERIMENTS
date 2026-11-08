# Checklist E10

## A. Preparation
- [ ] Xác định giả thuyết.
- [ ] Xác định biến độc lập.
- [ ] Xác định biến phụ thuộc.
- [ ] Xác định biến kiểm soát.
- [ ] Chuẩn bị cấu hình thử nghiệm.
- [ ] Chuẩn bị dataset.
- [ ] Kiểm tra công cụ chấm điểm.
- [ ] Định nghĩa allowlist công cụ và timeout; cần triển khai tool loop cùng trace trước khi chạy điều kiện enabled..

## B. Execution
- [ ] Kiểm tra phần cứng và môi trường.
- [ ] Xác minh model và cấu hình inference.
- [ ] Thực hiện từng cấu hình thử nghiệm.
- [ ] Chạy lặp theo kế hoạch.
- [ ] Lưu logs và kết quả từng run.
- [ ] Kiểm tra lỗi thực thi.
- [ ] Đối chiếu các mức No Tool / Tool-enabled và lưu manifest từng mức.

## C. Evaluation
- [ ] Tính metrics chính.
- [ ] Tính metrics phụ.
- [ ] So sánh các cấu hình.
- [ ] Thống kê độ biến động.
- [ ] Phân tích lỗi.
- [ ] Vẽ biểu đồ kết quả.
- [ ] Chấm riêng Tool Selection Accuracy theo EVALUATION.md.

## D. Conclusion
- [ ] Đối chiếu giả thuyết.
- [ ] Xác định kết luận được dữ liệu hỗ trợ.
- [ ] Ghi nhận hạn chế.
- [ ] Lưu phiên bản model, code và config.
- [ ] Cập nhật research log.
- [ ] Hoàn thành báo cáo thí nghiệm.
