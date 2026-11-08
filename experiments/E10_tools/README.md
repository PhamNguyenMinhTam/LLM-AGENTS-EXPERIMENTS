# E10 — Tool Access

## Mục tiêu và giả thuyết
Mục tiêu: Lợi ích công cụ. Giả thuyết đăng ký trước: Công cụ tăng thành công trên task cần tính toán nếu gọi đúng.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Tool Access; các mức: No Tool / Tool-enabled.
- Biến phụ thuộc chính: Task Success Rate; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Định nghĩa allowlist công cụ và timeout; cần triển khai tool loop cùng trace trước khi chạy điều kiện enabled.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E10_tools/run.py --dry-run
python experiments/E10_tools/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e10-tools`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Điều kiện can thiệp tools/memory/feedback chưa có runtime; chỉ dry-run được hỗ trợ và live bị chặn khi bật.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.
