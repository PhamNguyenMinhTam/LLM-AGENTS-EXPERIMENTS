# E06 — Hardware × Model

## Mục tiêu và giả thuyết
Mục tiêu: Tương tác phần cứng và model. Giả thuyết đăng ký trước: Tác động của model lên latency phụ thuộc phần cứng.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Hardware × Model; các mức: Các tổ hợp chip–model.
- Biến phụ thuộc chính: Task Accuracy; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Đăng ký thiết kế factorial đầy đủ; đo từng ô chip × model; giữ task ghép cặp và ghi ô không khả thi.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E06_hardware_model/run.py --dry-run
python experiments/E06_hardware_model/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e06-hardware-model`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Runtime đối chứng đã triển khai; điều kiện so sánh cần điền cấu hình và thiết bị thực tế.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Điều kiện đã đăng ký trên branch

- `x-small`: `experiments/E06_hardware_model/conditions/x-small.yaml`
- `x-large`: `experiments/E06_hardware_model/conditions/x-large.yaml`
- `y-small`: `experiments/E06_hardware_model/conditions/y-small.yaml`
- `y-large`: `experiments/E06_hardware_model/conditions/y-large.yaml`

Chạy từng điều kiện bằng `python -m scripts.run_experiment --config <đường-dẫn-YAML> --dry-run`, sau đó bỏ `--dry-run` khi đã hoàn tất preflight.

Biến môi trường cần khai báo: `E06_LARGE_DIGEST`, `E06_LARGE_NAME`, `E06_LARGE_QUANTIZATION`, `E06_SMALL_DIGEST`, `E06_SMALL_NAME`, `E06_SMALL_QUANTIZATION`, `HARDWARE_A`, `HARDWARE_B`, `OLLAMA_ENDPOINT_A`, `OLLAMA_ENDPOINT_B`. Các biến model theo điều kiện phải trỏ đúng tag/digest/quantization; tên mức không bảo đảm metadata tương ứng, cần rà soát trước chạy.

Đăng ký thiết kế factorial đầy đủ; đo từng ô chip × model; giữ task ghép cặp và ghi ô không khả thi. Chưa có kết quả nghiên cứu. Smoke task không đủ để kết luận.
