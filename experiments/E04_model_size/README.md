# E04 — Model Size

## Mục tiêu và giả thuyết
Mục tiêu: Ảnh hưởng kích thước. Giả thuyết đăng ký trước: Tăng kích thước model có thể cải thiện accuracy với chi phí bộ nhớ cao hơn.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Model Size; các mức: 1B / 3B / 7B–8B.
- Biến phụ thuộc chính: Task Accuracy; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Giữ họ model, quantization, prompt và dataset; đánh dấu OOM thay vì loại bỏ âm thầm.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E04_model_size/run.py --dry-run
python experiments/E04_model_size/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e04-model-size`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Runtime đối chứng đã triển khai; điều kiện so sánh cần điền cấu hình và thiết bị thực tế.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Điều kiện đã đăng ký trên branch

- `1b`: `experiments/E04_model_size/conditions/1b.yaml`
- `3b`: `experiments/E04_model_size/conditions/3b.yaml`
- `8b`: `experiments/E04_model_size/conditions/8b.yaml`

Chạy từng điều kiện bằng `python -m scripts.run_experiment --config <đường-dẫn-YAML> --dry-run`, sau đó bỏ `--dry-run` khi đã hoàn tất preflight.

Biến môi trường cần khai báo: `E04_1B_DIGEST`, `E04_1B_NAME`, `E04_1B_QUANTIZATION`, `E04_3B_DIGEST`, `E04_3B_NAME`, `E04_3B_QUANTIZATION`, `E04_8B_DIGEST`, `E04_8B_NAME`, `E04_8B_QUANTIZATION`, `HARDWARE_A`, `HARDWARE_B`, `OLLAMA_ENDPOINT_A`, `OLLAMA_ENDPOINT_B`. Các biến model theo điều kiện phải trỏ đúng tag/digest/quantization; tên mức không bảo đảm metadata tương ứng, cần rà soát trước chạy.

Giữ họ model, quantization, prompt và dataset; đánh dấu OOM thay vì loại bỏ âm thầm. Chưa có kết quả nghiên cứu. Smoke task không đủ để kết luận.
