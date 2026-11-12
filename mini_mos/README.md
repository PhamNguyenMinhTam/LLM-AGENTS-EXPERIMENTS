# mini-mOS: kiến trúc thực hành cá nhân

Đây không phải bản sao kiến trúc nội bộ ChatGPT/mOS. Giới hạn hiện tại: mỗi task một inference, không agent-to-agent.

## Tái sử dụng thay vì nhân đôi

| Layer | Nơi thực thi / kế hoạch | Trạng thái |
|---|---|---|
| Provider interface | `agents/base_agent.py`: BaseAgent.respond → AgentResponse | Existing |
| Ollama provider | `agents/ollama_agent.py`: timeout, non-stream chat, metadata verification | Existing |
| Task | `controller/config.py`: Task và AgentConfig Pydantic | Existing |
| Runtime & state | `core/runtime.py`: started → inference → evaluation → completed/failed | Implemented |
| Observability | Events UTC, run/task ID, latency và result JSON trong CLI | Implemented |
| Evaluation | `evaluation/evaluator.py`, exact-match; benchmark giữ runner cũ | Existing |
| Tool/permissions | Typed schema, allowlist deny-by-default, validated args và budget | Planned Q2 |
| Memory/retrieval | Session isolation, source hash/version, expiry, snapshots | Planned Q3 |
| Belief/evidence | B01 exact quote/source/fixture label; không có belief score | Fixture only |
| Dependency/verification | Graph claim→evidence→source; invalidate revision; budget policy | Planned Q4 |

Không tạo các module provider/task/evaluator mới trùng logic. Benchmark controller tiếp tục sở hữu repetitions, randomized order, manifest và CSV; mini runtime chỉ cho học từng task. CLI `python -m mini_mos.cli --help` dùng config E01 hiện có và adapter cũ. Xem [README](../README.md) để chạy.

## Contract và ranh giới

Input là Task; expected_output chỉ vào evaluator, không vào provider. Provider được inject để kiểm thử. Runtime trả state kết thúc, output, assessment (null khi inference lỗi), tên lớp lỗi, latency và events có run ID. Sai đáp án vẫn là task completed với success=false; lỗi hạ tầng là failed. CLI ghi file mới, không ghi đè. Lỗi config/model verification trước task làm CLI dừng; không tạo trace task giả. Trace chứa output, cần bảo vệ dữ liệu nhạy cảm. Chưa có durable state/cancellation/streaming, retries hoặc token budget; một request với timeout là stopping condition hiện tại.

## Thiết kế các bước sau

1. Q2: model đề xuất action; runtime validate schema và permissions trước execution; chỉ allowlist, giới hạn bước/thời gian và audit từng action. Tool output là dữ liệu không tin cậy. Không cấp shell tùy ý.
2. Coding sandbox: filesystem tạm, không secrets, không network, CPU/RAM/process/time limits, cleanup và negative tests. Chưa có sandbox được xác minh nên runtime không thực thi mã sinh ra.
3. Q3: memory record gồm session_id, source_id/hash, time, retrieval reason; feedback chỉ từ development; snapshot trước/sau và kiểm thử contamination. Không tự dùng final labels làm memory.
4. Q4: claim chứa text/status/evidence IDs; evidence chứa quote/source/version/location; dependency ghi quan hệ dùng chung nguồn, không xem nguồn sao chép là độc lập. Verification ghi budget/reason/check/result và invalidate khi nguồn đổi. Chưa có semantic entailment hoặc aggregation engine.

Mọi mở rộng phải có case lỗi, trace, phép thử và bài học cụ thể. [Roadmap](../ROADMAP.md), [explorations](../explorations/README.md).
