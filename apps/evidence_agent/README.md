# Knowledge & Evidence Agent

## Trạng thái

Fixture/mock: đọc JSON cục bộ, đối chiếu claim đã cho với source ID, quote, SHA256 và expected fixture answer. Không gọi LLM, không RAG/memory.

## Setup và chạy

Từ repository root, tạo venv và `python -m pip install -r requirements.txt` theo [setup](../../README.md). Không cần Ollama cho demo.

```bash
python -m apps.evidence_agent.app --fixture explorations/belief_formation/B01_correct_source/fixture.json
```

`config.yaml` mô tả kế hoạch, CLI chưa nạp file này; thay model qua config slice E01 hiện có.

## Workflow mục tiêu

Tài liệu → trích claim → liên kết nguồn → memory → retrieval → phát hiện mâu thuẫn → kiểm tra nguồn → revise → trả lời provenance.

## Tiêu chí hoàn thành

Có trace mỗi bước, negative tests, stopping condition, dữ liệu development/final tách biệt và phân tích ít nhất một lỗi. LLM extraction, persistent memory, retrieval, contradictions và revision Planned Q2–Q4. B01 không chứng minh entailment hoặc world truth.

Theo dõi [checklist](CHECKLIST.md), [mini-mOS](../../mini_mos/README.md) và [roadmap](../../ROADMAP.md).
