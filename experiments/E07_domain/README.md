# E07 — Domain

## Mục tiêu và giả thuyết
Mục tiêu: Chuyên môn hóa. Giả thuyết đăng ký trước: Prompt chuyên gia tăng điểm trong domain nhưng có thể giảm chuyển giao.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Domain; các mức: Generalist / Specialist.
- Biến phụ thuộc chính: Domain Accuracy; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
So generalist/specialist trong từng domain trước; đánh giá thêm domain ngoài chuyên môn trên tập chuẩn hóa.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E07_domain/run.py --dry-run
python experiments/E07_domain/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e07-domain`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Runtime đối chứng đã triển khai; điều kiện so sánh cần điền cấu hình và thiết bị thực tế.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Điều kiện đã đăng ký trên branch

- `mathematics-generalist`: `experiments/E07_domain/conditions/mathematics-generalist.yaml`
- `mathematics-specialist`: `experiments/E07_domain/conditions/mathematics-specialist.yaml`
- `coding-generalist`: `experiments/E07_domain/conditions/coding-generalist.yaml`
- `coding-specialist`: `experiments/E07_domain/conditions/coding-specialist.yaml`
- `classification-generalist`: `experiments/E07_domain/conditions/classification-generalist.yaml`
- `classification-specialist`: `experiments/E07_domain/conditions/classification-specialist.yaml`

Chạy từng điều kiện bằng `python -m scripts.run_experiment --config <đường-dẫn-YAML> --dry-run`, sau đó bỏ `--dry-run` khi đã hoàn tất preflight.

Biến môi trường cần khai báo: `HARDWARE_A`, `HARDWARE_B`, `MODEL_DIGEST`, `MODEL_NAME`, `OLLAMA_ENDPOINT_A`, `OLLAMA_ENDPOINT_B`, `QUANTIZATION`. Các biến model theo điều kiện phải trỏ đúng tag/digest/quantization; tên mức không bảo đảm metadata tương ứng, cần rà soát trước chạy.

So generalist/specialist trong từng domain trước; đánh giá thêm domain ngoài chuyên môn trên tập chuẩn hóa. Chưa có kết quả nghiên cứu. Smoke task không đủ để kết luận.
