# Báo cáo tái cấu trúc one-year lab

Ngày: 2026-11-12. Repository: https://github.com/PhamNguyenMinhTam/LLM-AGENTS-EXPERIMENTS

Branch: `refactor/one-year-agent-lab`; nền `4390157597a84a25a04fbffda4659428d7166c9a`. Working tree sạch trước thay đổi. Đã kiểm tra source, config, tests, workflow và tài liệu trước chỉnh sửa. Baseline: 27 tests pass, Ruff pass. Remote main khớp local; đủ 12 experiment branches được kiểm tra read-only, không sửa branch nào.

## Chạy được và giới hạn

- Runtime một bước qua interface/adapter/config/evaluator cũ, trace và CLI mock/live-configurable. Live Ollama chưa được chạy.
- Evidence app B01 fixture/mock: source ID, quote, content hash, expected label; không chứng minh entailment hay nguồn đúng.
- Coding app đọc file và ast.parse; không thực thi code, chưa có sandbox hoặc test/repair loop.
- README tiếng Việt, roadmap, tracks, journal trống, registry nguồn gốc và B01–B08 design.
- Tools/permissions runtime, memory/RAG, reflection, dependency/revision/active verification là Planned.
- Không A2A, consensus hoặc belief aggregation engine. Candidate idea chưa phải đề tài chính thức.

## Roadmap và checklist

Q1: Linux/Ollama/API/inference, runtime, E01 và foundations. Q2: practical agents, domain/prompt, tools và sandbox. Q3: memory/RAG/feedback/reflection, belief/evidence. Q4: provenance/dependency/conflict/verification, reliability report và future preparation. Mỗi quý có thực hành, paper, sản phẩm, checklist và completion gate trong [ROADMAP](../ROADMAP.md). [Checklist tổng](../LEARNING_CHECKLIST.md) phân biệt scaffold với thực hành chưa chạy.

## Verification

- Final unit/integration tests: 48 pass; Ruff: all checks passed.
- Smoke thực tế bằng subprocess: slice CLI mock + trace, B01 CLI, coding static CLI đều pass.
- Cả 12 config dry-run và E01 wrapper dry-run pass; không gọi Ollama/GPU.
- Các file E01–E12 ngoài README không thay đổi; nội dung README cũ vẫn là tiền tố của file mới.
- README mới/archive có local links hợp lệ; tests kiểm tra links tài liệu học, thiết kế B01–B08 và YAML.
- Changed-file scan: không file quá 200 KB, model weights/private-key files hoặc common secret patterns. Đây không phải chứng nhận không có mọi dạng secret.
- README cũ được lưu nội dung, chỉ điều chỉnh đường dẫn tương đối cho vị trí archive.
- Mock không đo model/hardware. Không benchmark thật mới hoặc nhật ký giả. Existing CI không yêu cầu Ollama/GPU.

## Publication

- Đã commit code/tài liệu: `9e54ec58749b13b8d0370b8e213968b8cbd9f1c4`, push branch `refactor/one-year-agent-lab` thành công.
- [GitHub Actions](https://github.com/PhamNguyenMinhTam/LLM-AGENTS-EXPERIMENTS/actions/runs/43222984666): completed/success cho commit trên (matrix Python 3.11–3.13).
- Sau push, đã đối chiếu remote: main và toàn bộ 12 branch E01–E12 giữ nguyên SHA trước thao tác.
- PR chưa được tạo: connector báo quyền pull=true, push=false và API trả 403; shell gh chưa đăng nhập. Automatic approval review từ chối lấy Git credential lưu trên máy để dùng cho lệnh tạo PR, vì coi đó là tái sử dụng credential khi chưa có ủy quyền đủ rõ. Thao tác lấy credential đó chưa được chạy.
- [Mở form PR từ branch đã push](https://github.com/PhamNguyenMinhTam/LLM-AGENTS-EXPERIMENTS/compare/main...refactor/one-year-agent-lab?expand=1). Nội dung PR đã chuẩn bị tại workspace `one_year_lab_pr.md`. Không tự merge PR.

## Ba bước tiếp theo

1. Cấu hình hai laptop Linux/Ollama; khóa metadata và chạy E01 thật.
2. Ghi journal từ trace/lỗi; thực hành context/prompt có đối chứng và đọc P01/P06.
3. Thiết kế sandbox cùng tool permissions; chỉ bật coding execution sau khi xác minh isolation và resource/network limits.

## File đã sửa

- `README.md`
- `experiments/E01_baseline/README.md`
- `experiments/E02_model_type/README.md`
- `experiments/E03_hardware/README.md`
- `experiments/E04_model_size/README.md`
- `experiments/E05_quantization/README.md`
- `experiments/E06_hardware_model/README.md`
- `experiments/E07_domain/README.md`
- `experiments/E08_difficulty/README.md`
- `experiments/E09_prompt/README.md`
- `experiments/E10_tools/README.md`
- `experiments/E11_memory/README.md`
- `experiments/E12_feedback/README.md`
- `pyproject.toml`

## File mới

- `CHANGELOG.md`
- `LEARNING_CHECKLIST.md`
- `ROADMAP.md`
- `apps/__init__.py`
- `apps/coding_agent/CHECKLIST.md`
- `apps/coding_agent/README.md`
- `apps/coding_agent/__init__.py`
- `apps/coding_agent/app.py`
- `apps/coding_agent/config.yaml`
- `apps/coding_agent/fixtures/example.py`
- `apps/coding_agent/tests/test_static_inspection.py`
- `apps/evidence_agent/CHECKLIST.md`
- `apps/evidence_agent/README.md`
- `apps/evidence_agent/__init__.py`
- `apps/evidence_agent/app.py`
- `apps/evidence_agent/config.yaml`
- `apps/evidence_agent/tests/test_b01.py`
- `docs/archive/README_before_one_year_lab.md`
- `docs/one_year_lab_report.md`
- `explorations/README.md`
- `explorations/active_verification/B08_verification_budget/CHECKLIST.md`
- `explorations/active_verification/B08_verification_budget/README.md`
- `explorations/active_verification/B08_verification_budget/scenario.json`
- `explorations/active_verification/README.md`
- `explorations/agent_loop/README.md`
- `explorations/belief_formation/B01_correct_source/CHECKLIST.md`
- `explorations/belief_formation/B01_correct_source/README.md`
- `explorations/belief_formation/B01_correct_source/fixture.json`
- `explorations/belief_formation/B01_correct_source/scenario.json`
- `explorations/belief_formation/README.md`
- `explorations/conflicting_evidence/B03_conflicting_sources/CHECKLIST.md`
- `explorations/conflicting_evidence/B03_conflicting_sources/README.md`
- `explorations/conflicting_evidence/B03_conflicting_sources/scenario.json`
- `explorations/conflicting_evidence/README.md`
- `explorations/dependency_detection/B04_duplicated_evidence/CHECKLIST.md`
- `explorations/dependency_detection/B04_duplicated_evidence/README.md`
- `explorations/dependency_detection/B04_duplicated_evidence/scenario.json`
- `explorations/dependency_detection/B07_dependency_propagation/CHECKLIST.md`
- `explorations/dependency_detection/B07_dependency_propagation/README.md`
- `explorations/dependency_detection/B07_dependency_propagation/scenario.json`
- `explorations/dependency_detection/README.md`
- `explorations/memory_behavior/B05_outdated_memory/CHECKLIST.md`
- `explorations/memory_behavior/B05_outdated_memory/README.md`
- `explorations/memory_behavior/B05_outdated_memory/scenario.json`
- `explorations/memory_behavior/README.md`
- `explorations/source_provenance/B02_incorrect_source/CHECKLIST.md`
- `explorations/source_provenance/B02_incorrect_source/README.md`
- `explorations/source_provenance/B02_incorrect_source/scenario.json`
- `explorations/source_provenance/B06_source_revision/CHECKLIST.md`
- `explorations/source_provenance/B06_source_revision/README.md`
- `explorations/source_provenance/B06_source_revision/scenario.json`
- `explorations/source_provenance/README.md`
- `explorations/tool_calling/README.md`
- `future_multi_agent/README.md`
- `future_multi_agent/candidate_idea.md`
- `future_multi_agent/open_questions.md`
- `future_multi_agent/problem_map.md`
- `future_multi_agent/transition_checklist.md`
- `learning/README.md`
- `learning/concept_map.md`
- `learning/learning_tracks.md`
- `learning/lessons_learned.md`
- `learning/questions.md`
- `learning/weekly_journal.md`
- `literature/README.md`
- `literature/notes/README.md`
- `literature/notes/agentbench.md`
- `literature/notes/expel.md`
- `literature/notes/reflexion.md`
- `literature/paper_registry.md`
- `literature/paper_to_experiment.md`
- `literature/reading_checklist.md`
- `mini_mos/README.md`
- `mini_mos/__init__.py`
- `mini_mos/beliefs/__init__.py`
- `mini_mos/beliefs/verification.py`
- `mini_mos/cli.py`
- `mini_mos/core/__init__.py`
- `mini_mos/core/runtime.py`
- `tests/test_learning_docs.py`
- `tests/test_mini_mos.py`
- `tests/test_mini_mos_cli.py`
