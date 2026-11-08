# Checklist tổng tiến độ

`[x]` chỉ cho việc đã kiểm chứng tại local; không đại diện hoàn thành benchmark hoặc triển khai từ xa.

## 1. Repository Setup

- [x] Tạo framework và cấu trúc E01–E12 trên local.
- [x] Tạo 12 branch thí nghiệm có commit điều kiện riêng.
- [x] Gắn origin đúng repository được chỉ định.
- [x] Push main và 12 branch; xác minh remote.
- [x] Xác minh GitHub Actions trên main.
- [ ] Rà soát tài liệu sau từng đợt cập nhật.

## 2. Linux & Ollama Setup

- [ ] Cài Ubuntu/Python trên hai laptop.
- [ ] Cài Ollama và tải tag model.
- [ ] Kiểm kê chip, GPU, RAM/VRAM, nguồn và thermal throttling.
- [ ] Kiểm tra API/digest/quantization từng endpoint.
- [ ] Xác nhận hai chip cùng loại không bị coi là hiệu năng giống tuyệt đối.

## 3. Agent Runtime

- [x] Chuẩn hóa response Ollama và kiểm thử parser.
- [x] Kiểm thử timeout/lỗi API bằng mock.
- [x] Không truyền expected_output hoặc lịch sử agent khác vào request.
- [ ] Xác minh agent A/B trên Ollama thật.

## 4. Experiment Controller

- [x] Đọc và validate YAML/dataset.
- [x] Hỗ trợ repetition, dry-run và mock test.
- [x] Ghi manifest, JSONL và CSV qua kiểm thử.
- [ ] Xác minh toàn bộ luồng trên hai laptop.

## 5. Dataset Preparation

- [x] Tạo smoke tasks có ghi rõ giới hạn sử dụng.
- [ ] Chọn dataset nghiên cứu có nguồn/license.
- [ ] Khử trùng lặp và chuẩn hóa domain/độ khó.
- [ ] Tách experience/development khỏi final evaluation.
- [ ] Khóa checksum, rubric và cỡ mẫu.

## 6. E01–E06: Model & Hardware

- [ ] E01: đo độ ổn định và biến động.
- [ ] E02: so model cùng điều kiện.
- [ ] E03: kiểm soát nguồn/nhiệt và đo tài nguyên.
- [ ] E04: so kích thước và ghi OOM.
- [ ] E05: so quantization từ cùng trọng số.
- [ ] E06: đo đủ tổ hợp chip–model hoặc ghi không khả thi.

## 7. E07–E10: Domain & Behavior

- [ ] E07: đánh giá chuyên môn hóa trong và ngoài domain.
- [ ] E08: xác nhận độ khó trước chạy.
- [ ] E09: khóa prompt và ví dụ few-shot ngoài final.
- [ ] E10: triển khai tool loop/trace rồi đo can thiệp.

## 8. E11–E12: Adaptation

- [ ] Triển khai memory store tách agent/session và retrieval trace.
- [ ] E11: đánh giá chuyển giao, lỗi lặp và memory cũ.
- [ ] Thiết kế feedback đúng/sai, binary/detailed và correction trace.
- [ ] E12: đánh giá sửa lỗi và chống feedback sai.
- [ ] Đóng băng adaptation trước final; không kết luận thay đổi trọng số.

## 9. Evaluation & Analysis

- [x] Kiểm thử exact-match, latency và consistency.
- [ ] Thu thập resource/energy/TTFT bằng công cụ phù hợp.
- [ ] Chấm rubric mù và giải quyết bất đồng.
- [ ] Bootstrap theo task, báo CI, phân tích lỗi và vẽ biểu đồ.
- [ ] Kiểm tra tính tái lập từ manifest.

## 10. Research Reporting

- [ ] Tổng hợp kết quả và hạn chế.
- [ ] Tách giả thuyết, dự đoán và quan sát thực tế.
- [ ] Cập nhật research log.
- [ ] Viết báo cáo khoa học có nguồn dữ liệu và code/config version.

## Trạng thái từng thí nghiệm

### [E01_baseline](../experiments/E01_baseline/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E02_model_type](../experiments/E02_model_type/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E03_hardware](../experiments/E03_hardware/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E04_model_size](../experiments/E04_model_size/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E05_quantization](../experiments/E05_quantization/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E06_hardware_model](../experiments/E06_hardware_model/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E07_domain](../experiments/E07_domain/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E08_difficulty](../experiments/E08_difficulty/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E09_prompt](../experiments/E09_prompt/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E10_tools](../experiments/E10_tools/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E11_memory](../experiments/E11_memory/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

### [E12_feedback](../experiments/E12_feedback/CHECKLIST.md)

- [ ] Chuẩn bị
- [ ] Thực thi
- [ ] Đánh giá
- [ ] Hoàn thành

