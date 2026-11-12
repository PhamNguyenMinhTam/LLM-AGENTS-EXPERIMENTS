# E03 — Hardware

## Mục tiêu và giả thuyết
Mục tiêu: Hiệu năng phần cứng. Giả thuyết đăng ký trước: Phần cứng ảnh hưởng latency nhiều hơn độ chính xác khi giữ nguyên model digest.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Hardware; các mức: Chip X / Chip Y.
- Biến phụ thuộc chính: Inference Throughput; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Dùng cùng digest trên hai máy; cố định chế độ nguồn, nhiệt độ, backend và số luồng.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E03_hardware/run.py --dry-run
python experiments/E03_hardware/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e03-hardware`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Runtime đối chứng đã triển khai; điều kiện so sánh cần điền cấu hình và thiết bị thực tế.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Liên kết học qua thực hành

- Learning Track: A; [tracks](../../learning/learning_tracks.md).
- Related Paper: P01/P06; [registry](../../literature/paper_registry.md) (liên hệ học tập, không khẳng định reproduction).
- Mini-App: [evidence_agent](../../apps/evidence_agent/README.md).
- Exploration: [agent_loop](../../explorations/agent_loop/README.md).
- Learning Journal: [mẫu tuần](../../learning/weekly_journal.md).

Trạng thái benchmark/checklist cũ được giữ nguyên; thêm liên kết không có nghĩa đã chạy thí nghiệm.
