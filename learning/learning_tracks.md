# Sáu learning tracks

Mỗi vòng học: hiểu → xây → test → quan sát → đọc đối chiếu → cải thiện. Trạng thái mục tiêu: Planned.

## A — LLM Foundations

- Nội dung: Inference, model selection/capability, context, sampling, quantization và hardware limits.
- Benchmark: E01–E06; [ma trận](../experiments/experiment_matrix.md).
- Thực hành: [exploration](../explorations/agent_loop/README.md).
- Mini-app: [coding](../apps/coding_agent/README.md), [evidence](../apps/evidence_agent/README.md).
- Paper: [mapping](../literature/paper_to_experiment.md).
- Sản phẩm/tiêu chí: Đổi một tham số; ghi latency/quality và giới hạn RAM; dẫn artifact trong [journal](weekly_journal.md).

## B — Agent Engineering

- Nội dung: Architecture, lifecycle, loop, state, prompt policy, tools, error handling, permissions, stop.
- Benchmark: E07–E10; [ma trận](../experiments/experiment_matrix.md).
- Thực hành: [exploration](../explorations/tool_calling/README.md).
- Mini-app: [coding](../apps/coding_agent/README.md), [evidence](../apps/evidence_agent/README.md).
- Paper: [mapping](../literature/paper_to_experiment.md).
- Sản phẩm/tiêu chí: Trace một lỗi và một permission denial; dẫn artifact trong [journal](weekly_journal.md).

## C — Practical Mini-Apps

- Nội dung: Coding, evidence, workflow, tool integration, CLI, logging/debugging.
- Benchmark: E07–E10; [ma trận](../experiments/experiment_matrix.md).
- Thực hành: [exploration](../explorations/belief_formation/README.md).
- Mini-app: [coding](../apps/coding_agent/README.md), [evidence](../apps/evidence_agent/README.md).
- Paper: [mapping](../literature/paper_to_experiment.md).
- Sản phẩm/tiêu chí: Một workflow có input/output và lỗi tái lập; dẫn artifact trong [journal](weekly_journal.md).

## D — Memory & Adaptation

- Nội dung: Short/long-term memory, retrieval, feedback, reflection, correction, reuse, contamination.
- Benchmark: E11–E12; [ma trận](../experiments/experiment_matrix.md).
- Thực hành: [exploration](../explorations/memory_behavior/README.md).
- Mini-app: [coding](../apps/coding_agent/README.md), [evidence](../apps/evidence_agent/README.md).
- Paper: [mapping](../literature/paper_to_experiment.md).
- Sản phẩm/tiêu chí: So sánh reset/giữ memory; không dùng final labels; dẫn artifact trong [journal](weekly_journal.md).

## E — Belief, Evidence & Verification

- Nội dung: Claims, extraction, provenance, conflict, dependencies, duplicates, revision, active checking.
- Benchmark: E09/E11; [ma trận](../experiments/experiment_matrix.md).
- Thực hành: [exploration](../explorations/active_verification/README.md).
- Mini-app: [coding](../apps/coding_agent/README.md), [evidence](../apps/evidence_agent/README.md).
- Paper: [mapping](../literature/paper_to_experiment.md).
- Sản phẩm/tiêu chí: B01–B08 với nguồn, hash và failure analysis; dẫn artifact trong [journal](weekly_journal.md).

## F — Future Multi-Agent Preparation

- Nội dung: Giới hạn một agent, câu hỏi tương tác, hiểu biết và hướng đọc tiếp.
- Benchmark: E01–E12 làm nền; [ma trận](../experiments/experiment_matrix.md).
- Thực hành: [exploration](../explorations/dependency_detection/README.md).
- Mini-app: [coding](../apps/coding_agent/README.md), [evidence](../apps/evidence_agent/README.md).
- Paper: [mapping](../literature/paper_to_experiment.md).
- Sản phẩm/tiêu chí: Problem map và transition checklist, không A2A; dẫn artifact trong [journal](weekly_journal.md).
