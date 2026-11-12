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

## Liên kết học qua thực hành

- Learning Track: D; [tracks](../../learning/learning_tracks.md).
- Related Paper: P02/P03/P04; [registry](../../literature/paper_registry.md) (liên hệ học tập, không khẳng định reproduction).
- Mini-App: [coding_agent](../../apps/coding_agent/README.md).
- Exploration: [memory_behavior](../../explorations/memory_behavior/README.md).
- Learning Journal: [mẫu tuần](../../learning/weekly_journal.md).

Trạng thái benchmark/checklist cũ được giữ nguyên; thêm liên kết không có nghĩa đã chạy thí nghiệm.
