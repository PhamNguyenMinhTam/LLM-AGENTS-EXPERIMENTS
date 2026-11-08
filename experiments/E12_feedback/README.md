# E12 — Feedback

## Mục tiêu và giả thuyết
Mục tiêu: Khả năng sửa lỗi. Giả thuyết đăng ký trước: Feedback chi tiết tăng khả năng sửa lỗi so với binary với chi phí token cao hơn.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Feedback; các mức: None / Binary / Detailed.
- Biến phụ thuộc chính: Correction Success Rate; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Ghép before/after cùng task; giới hạn số vòng; thêm feedback sai có kiểm soát; final không tham gia sửa lỗi.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E12_feedback/run.py --dry-run
python experiments/E12_feedback/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e12-feedback`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Điều kiện can thiệp tools/memory/feedback chưa có runtime; chỉ dry-run được hỗ trợ và live bị chặn khi bật.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Điều kiện đã đăng ký trên branch

- `none`: `experiments/E12_feedback/conditions/none.yaml`
- `binary`: `experiments/E12_feedback/conditions/binary.yaml`
- `detailed`: `experiments/E12_feedback/conditions/detailed.yaml`

Chạy từng điều kiện bằng `python -m scripts.run_experiment --config <đường-dẫn-YAML> --dry-run`, sau đó bỏ `--dry-run` khi đã hoàn tất preflight.

Biến môi trường cần khai báo: `HARDWARE_A`, `HARDWARE_B`, `MODEL_DIGEST`, `MODEL_NAME`, `OLLAMA_ENDPOINT_A`, `OLLAMA_ENDPOINT_B`, `QUANTIZATION`. Các biến model theo điều kiện phải trỏ đúng tag/digest/quantization; tên mức không bảo đảm metadata tương ứng, cần rà soát trước chạy.

Ghép before/after cùng task; giới hạn số vòng; thêm feedback sai có kiểm soát; final không tham gia sửa lỗi. Chưa có kết quả nghiên cứu. Smoke task không đủ để kết luận.

Can thiệp chưa có runtime; dry-run báo unsupported, live từ chối.
