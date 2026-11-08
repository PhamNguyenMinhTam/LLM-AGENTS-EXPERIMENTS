# Hướng dẫn đánh giá
MVP tự động tính exact-match sau strip, accuracy (gồm lỗi API), latency mean/median/P95, failure rate và consistency theo task; JSONL giữ token counters và throughput.
Summary mặc định luôn xuất tập metric MVP; evaluation_metrics là danh sách mục tiêu hợp lệ, chưa hỗ trợ plugin metric tùy ý.
Không thực thi mã sinh bởi model. Reasoning, hallucination, tool use, memory, feedback cần rubric/trace riêng trong EVALUATION.md từng E. Các metric này không được giả định đã có trong CSV.
Resource, energy và TTFT chưa được thu thập. CPU/RAM controller không đại diện cho laptop inference. Thiếu đo ghi null/N/A và nguyên nhân.
Trước xuất báo cáo: kiểm tra manifest, checksum, số run dự kiến/thực, nhãn lỗi, dữ liệu thiếu và rò rỉ; ghép theo task/model/condition; tính CI và nhận xét hạn chế. Không coi smoke test hoặc mock là bằng chứng benchmark.
