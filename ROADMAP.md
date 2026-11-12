# Roadmap một năm

Tính từ ngày bắt đầu học. Tất cả milestone thực hành bên dưới là Planned; scaffold không đồng nghĩa hoàn thành. Mỗi tuần dành một phiên xây, một phiên test/quan sát và một phiên đọc/ghi chép; điều chỉnh theo thời gian thực tế.

## Quarter 1 — Foundations

- Nội dung học: Linux, HTTP API, Ollama inference, context, sampling, quantization; lifecycle một bước.
- Bài thực hành: Chạy mock slice, trace một lỗi API; cấu hình hai laptop; chạy E01 lặp và thử E02–E06 theo khả năng máy.
- Paper: AgentBench; Lost in the Middle; xem [registry](literature/paper_registry.md).
- Sản phẩm: Inventory thật, trace có config, baseline và ghi chép lỗi.
- [ ] Có artifact và journal dẫn tới commit/config/run_id.
- [ ] Đọc paper liên quan và tách báo cáo tác giả khỏi quan sát cá nhân.
- [ ] Phân tích ít nhất một lỗi và một điều kiện đối chứng.
- Tiêu chí hoàn thành: Có thể giải thích request/result/evaluation; model metadata được xác minh; baseline thật có run_id và hạn chế.

## Quarter 2 — Practical Agents

- Nội dung học: Domain, prompt policy, state, tool schemas, allowlist, dừng và recovery.
- Bài thực hành: E07–E10; coding plan → generate → sandbox tests → feedback → sửa; evidence đọc tài liệu → claim → nguồn.
- Paper: ToolLLM / ToolBench; AgentBoard; xem [registry](literature/paper_registry.md).
- Sản phẩm: Hai CLI mini-app với workflow có kiểm thử; sandbox được đánh giá trước thực thi.
- [ ] Có artifact và journal dẫn tới commit/config/run_id.
- [ ] Đọc paper liên quan và tách báo cáo tác giả khỏi quan sát cá nhân.
- [ ] Phân tích ít nhất một lỗi và một điều kiện đối chứng.
- Tiêu chí hoàn thành: Tool ngoài allowlist bị từ chối; số bước/thời gian hữu hạn; chứng minh lỗi và dừng; không chạy code trên host.

## Quarter 3 — Memory & Adaptation

- Nội dung học: Short/long-term memory, RAG, reflection, feedback, contamination và belief/evidence.
- Bài thực hành: E11–E12 với đối chứng và dữ liệu held-out; thử B01–B05; reset session và kiểm tra leakage.
- Paper: Reflexion; ExpeL; Self-Refine; xem [registry](literature/paper_registry.md).
- Sản phẩm: Memory có snapshot/provenance và báo cáo trước/sau; rubric claim.
- [ ] Có artifact và journal dẫn tới commit/config/run_id.
- [ ] Đọc paper liên quan và tách báo cáo tác giả khỏi quan sát cá nhân.
- [ ] Phân tích ít nhất một lỗi và một điều kiện đối chứng.
- Tiêu chí hoàn thành: Tách development/final; lưu feedback có trace; báo cáo cả trường hợp giảm chất lượng và giới hạn causal inference.

## Quarter 4 — Reliability & Preparation

- Nội dung học: Provenance, dependency, conflicting evidence, active verification và reliability.
- Bài thực hành: B06–B08; sửa nguồn, invalidate claim phụ thuộc, phân bổ verification budget; đánh giá lỗi.
- Paper: AgentBoard; mục evidence dependence/provenance cần xác minh trong registry; xem [registry](literature/paper_registry.md).
- Sản phẩm: Reliability report, problem map và danh sách câu hỏi nghiên cứu chưa trả lời.
- [ ] Có artifact và journal dẫn tới commit/config/run_id.
- [ ] Đọc paper liên quan và tách báo cáo tác giả khỏi quan sát cá nhân.
- [ ] Phân tích ít nhất một lỗi và một điều kiện đối chứng.
- Tiêu chí hoàn thành: Có case pass/fail tái lập, nguồn và dependency được ghi; transition checklist được xem xét; không tự bật A2A.

Theo dõi [checklist tổng](LEARNING_CHECKLIST.md). Không chuyển quý chỉ vì tạo đủ file; ghi rõ mục chưa đạt và giảm phạm vi nếu phần cứng không đủ.
