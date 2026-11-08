# E05 — Quantization

## Mục tiêu và giả thuyết
Mục tiêu: Đánh đổi chất lượng/tài nguyên. Giả thuyết đăng ký trước: Quantization mạnh hơn giảm bộ nhớ nhưng có thể giảm độ chính xác.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Quantization; các mức: Q4 / Q8 / FP16.
- Biến phụ thuộc chính: Accuracy Degradation; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Xuất các mức quantization từ cùng trọng số; xác minh metadata và cấu hình FP16 khả thi.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E05_quantization/run.py --dry-run
python experiments/E05_quantization/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e05-quantization`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Runtime đối chứng đã triển khai; điều kiện so sánh cần điền cấu hình và thiết bị thực tế.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Điều kiện đã đăng ký trên branch

- `q4`: `experiments/E05_quantization/conditions/q4.yaml`
- `q8`: `experiments/E05_quantization/conditions/q8.yaml`
- `fp16`: `experiments/E05_quantization/conditions/fp16.yaml`

Chạy từng điều kiện bằng `python -m scripts.run_experiment --config <đường-dẫn-YAML> --dry-run`, sau đó bỏ `--dry-run` khi đã hoàn tất preflight.

Biến môi trường cần khai báo: `E05_FP16_DIGEST`, `E05_FP16_NAME`, `E05_FP16_QUANTIZATION`, `E05_Q4_DIGEST`, `E05_Q4_NAME`, `E05_Q4_QUANTIZATION`, `E05_Q8_DIGEST`, `E05_Q8_NAME`, `E05_Q8_QUANTIZATION`, `HARDWARE_A`, `HARDWARE_B`, `OLLAMA_ENDPOINT_A`, `OLLAMA_ENDPOINT_B`. Các biến model theo điều kiện phải trỏ đúng tag/digest/quantization; tên mức không bảo đảm metadata tương ứng, cần rà soát trước chạy.

Xuất các mức quantization từ cùng trọng số; xác minh metadata và cấu hình FP16 khả thi. Chưa có kết quả nghiên cứu. Smoke task không đủ để kết luận.
