# E09 — Prompt Strategy

## Mục tiêu và giả thuyết
Mục tiêu: Ảnh hưởng prompt. Giả thuyết đăng ký trước: Prompt có cấu trúc tăng tuân thủ định dạng so với zero-shot.
Đây là giả thuyết, chưa có dữ liệu thực nghiệm để chấp nhận hoặc bác bỏ.

## Thiết kế
- Biến độc lập: Prompt Strategy; các mức: Zero-shot / Few-shot / Structured.
- Biến phụ thuộc chính: Task Accuracy; phụ: các tiêu chí trong [EVALUATION.md](EVALUATION.md).
- Kiểm soát: dataset/checksum, độ khó, inference seed, temperature, context, prompt (trừ E09), model digest (trừ E02/E04/E05/E06), phần cứng (trừ E03/E06), phiên bản phần mềm.
- Đơn vị phân tích là task. Lần lặp không được coi là các task độc lập.

## Quy trình
Lưu nguyên văn từng prompt và phiên bản; ví dụ few-shot chỉ lấy từ development, không lấy final.
1. Đăng ký cỡ mẫu, metric chính và tiêu chí dừng trước khi đo; mẫu smoke đi kèm chỉ kiểm tra luồng.
2. Sao chép config cho từng điều kiện; đổi `condition` và đúng yếu tố cần khảo sát. Giữ config và manifest từng điều kiện.
3. Chạy dry-run, preflight, warm-up riêng, rồi đo theo thứ tự cân bằng/ngẫu nhiên.
4. Lưu JSONL/CSV, phân tích ghép cặp và CI bootstrap theo task; không kết luận chỉ từ một lần chạy.

## Chạy
```bash
python experiments/E09_prompt/run.py --dry-run
python experiments/E09_prompt/run.py
```
Runner dùng chung, không có giao tiếp giữa agent. Branch dành riêng: `experiment/e09-prompt`.

## Kết quả kỳ vọng và trạng thái
Kỳ vọng kiểm chứng được giả thuyết cùng khoảng bất định, không bảo đảm hướng hiệu ứng.
Config mặc định là điều kiện đối chứng. Runtime đối chứng đã triển khai; điều kiện so sánh cần điền cấu hình và thiết bị thực tế.
Chưa chạy benchmark thực; không có kết quả khoa học trong repository.

## Liên kết học qua thực hành

- Learning Track: B/C; [tracks](../../learning/learning_tracks.md).
- Related Paper: P01/P04/P05/P07; [registry](../../literature/paper_registry.md) (liên hệ học tập, không khẳng định reproduction).
- Mini-App: [evidence_agent](../../apps/evidence_agent/README.md).
- Exploration: [tool_calling](../../explorations/tool_calling/README.md).
- Learning Journal: [mẫu tuần](../../learning/weekly_journal.md).

Trạng thái benchmark/checklist cũ được giữ nguyên; thêm liên kết không có nghĩa đã chạy thí nghiệm.
