# E08 — Task Difficulty

## Mục tiêu và giả thuyết
Mục tiêu: Giới hạn năng lực. Giả thuyết đăng ký trước: Tỷ lệ thành công giảm khi độ khó tăng theo rubric định trước.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Task Difficulty; các mức: Easy / Medium / Hard.
- Biến phụ thuộc chính: Success by Difficulty; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Gán độ khó trước khi chạy bởi hai người; cân bằng domain và số lượng task ở từng mức.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E08_difficulty/run.py --dry-run
python experiments/E08_difficulty/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e08-difficulty`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Runtime đối chứng đã triển khai; điều kiện so sánh cần điền cấu hình và thiết bị thực tế.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Điều kiện đã đăng ký trên branch

- `easy`: `experiments/E08_difficulty/conditions/easy.yaml`
- `medium`: `experiments/E08_difficulty/conditions/medium.yaml`
- `hard`: `experiments/E08_difficulty/conditions/hard.yaml`

Chạy từng điều kiện bằng `python -m scripts.run_experiment --config <đường-dẫn-YAML> --dry-run`, sau đó bỏ `--dry-run` khi đã hoàn tất preflight.

Biến môi trường cần khai báo: `HARDWARE_A`, `HARDWARE_B`, `MODEL_DIGEST`, `MODEL_NAME`, `OLLAMA_ENDPOINT_A`, `OLLAMA_ENDPOINT_B`, `QUANTIZATION`. Các biến model theo điều kiện phải trỏ đúng tag/digest/quantization; tên mức không bảo đảm metadata tương ứng, cần rà soát trước chạy.

Gán độ khó trước khi chạy bởi hai người; cân bằng domain và số lượng task ở từng mức. Chưa có kết quả nghiên cứu. Smoke task không đủ để kết luận.

Dataset easy/medium/hard chỉ là ví dụ định dạng; nhãn độ khó chưa được xác nhận và mỗi mức chỉ có một task.
