# Paper registry

Metadata và tóm tắt dưới đây được kiểm tra từ trang abstract arXiv gốc ngày 2026-11-12. Findings là báo cáo của tác giả, không phải tái lập độc lập. Reading Status của P01–P07: Metadata/abstract verified; full paper unread. DOI không được thêm; URL gốc đủ để tra cứu. Không lưu PDF.

## P01 — AgentBench: Evaluating LLMs as Agents

- Paper ID: P01
- Title: AgentBench: Evaluating LLMs as Agents
- Authors: Xiao Liu et al. (đầy đủ tại nguồn)
- Year: 2023 preprint
- Venue: ICLR 2024 (arXiv comments)
- DOI/URL: [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)
- Research Problem: Đánh giá LLM trong môi trường tương tác
- Core Method: Benchmark nhiều môi trường
- Findings (author-reported): Abstract báo cáo benchmark 8 môi trường và phân tích lỗi reasoning/decision/instruction following
- Limitations (lab interpretation unless stated): Không suy rộng kết quả model trong paper sang máy local
- Related Learning Track: A/B/C
- Related Experiment: E01/E07/E08
- Reproduction Idea: Phân loại lỗi task nhỏ, không gọi là reproduction đầy đủ
- Reading Status: Metadata/abstract verified; full paper unread

## P02 — Reflexion: Language Agents with Verbal Reinforcement Learning

- Paper ID: P02
- Title: Reflexion: Language Agents with Verbal Reinforcement Learning
- Authors: Noah Shinn; Federico Cassano; Edward Berman; Ashwin Gopinath; Karthik Narasimhan; Shunyu Yao
- Year: 2023
- Venue: Chưa xác minh venue trong nguồn đã đọc
- DOI/URL: [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- Research Problem: Cải thiện qua trial-and-error không cập nhật weights
- Core Method: Linguistic feedback và episodic reflective memory
- Findings (author-reported): Abstract báo cáo cải thiện trên các task được khảo sát
- Limitations (lab interpretation unless stated): Feedback tự sinh chưa phải ground truth; cần đọc ablation
- Related Learning Track: D
- Related Experiment: E11/E12
- Reproduction Idea: So sánh feedback có/không reflection trên development
- Reading Status: Metadata/abstract verified; full paper unread

## P03 — ExpeL: LLM Agents Are Experiential Learners

- Paper ID: P03
- Title: ExpeL: LLM Agents Are Experiential Learners
- Authors: Andrew Zhao; Daniel Huang; Quentin Xu; Matthieu Lin; Yong-Jin Liu; Gao Huang
- Year: 2023 preprint
- Venue: AAAI 2024 (arXiv comments)
- DOI/URL: [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144)
- Research Problem: Tích lũy kinh nghiệm không fine-tune
- Core Method: Trích insights từ training tasks rồi recall khi inference
- Findings (author-reported): Abstract báo cáo cải thiện khi tích lũy experience
- Limitations (lab interpretation unless stated): Không suy ra bảo đảm transfer hoặc causal effect cho lab
- Related Learning Track: D
- Related Experiment: E11/E12
- Reproduction Idea: Memory insights với hold-out và reset session
- Reading Status: Metadata/abstract verified; full paper unread

## P04 — Self-Refine: Iterative Refinement with Self-Feedback

- Paper ID: P04
- Title: Self-Refine: Iterative Refinement with Self-Feedback
- Authors: Aman Madaan et al. (đầy đủ tại nguồn)
- Year: 2023
- Venue: Chưa xác minh
- DOI/URL: [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)
- Research Problem: Cải thiện output tại test time
- Core Method: Generate → self-feedback → refine
- Findings (author-reported): Abstract báo cáo đánh giá trên 7 loại task
- Limitations (lab interpretation unless stated): Chưa đọc chi tiết rubric và chi phí; self-feedback có thể sai
- Related Learning Track: B/D
- Related Experiment: E09/E12
- Reproduction Idea: Đặt max iterations rồi so sánh one-shot
- Reading Status: Metadata/abstract verified; full paper unread

## P05 — AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents

- Paper ID: P05
- Title: AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents
- Authors: Chang Ma; Junlei Zhang; Zhihao Zhu; Cheng Yang; Yujiu Yang; Yaohui Jin; Zhenzhong Lan; Lingpeng Kong; Junxian He
- Year: 2024
- Venue: NeurIPS 2024 (arXiv comments)
- DOI/URL: [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://arxiv.org/abs/2401.13178)
- Research Problem: Quan sát tiến trình thay vì chỉ final success
- Core Method: Progress-rate và analytical evaluation toolkit
- Findings (author-reported): Abstract giới thiệu fine-grained progress metric
- Limitations (lab interpretation unless stated): Lab một bước chưa đo multi-turn progress như paper
- Related Learning Track: B/C/E
- Related Experiment: E08/E10
- Reproduction Idea: Thêm milestone trace khi có tool loop
- Reading Status: Metadata/abstract verified; full paper unread

## P06 — Lost in the Middle: How Language Models Use Long Contexts

- Paper ID: P06
- Title: Lost in the Middle: How Language Models Use Long Contexts
- Authors: Nelson F. Liu; Kevin Lin; John Hewitt; Ashwin Paranjape; Michele Bevilacqua; Fabio Petroni; Percy Liang
- Year: 2023 preprint
- Venue: TACL accepted (arXiv comments; năm xuất bản cần kiểm tra)
- DOI/URL: [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- Research Problem: Model sử dụng thông tin trong context dài thế nào
- Core Method: Đổi vị trí thông tin ở QA và key-value retrieval
- Findings (author-reported): Abstract báo cáo suy giảm khi thông tin liên quan nằm giữa context
- Limitations (lab interpretation unless stated): Không coi mọi model/context đều có cùng đường cong
- Related Learning Track: A/D
- Related Experiment: E09/E11
- Reproduction Idea: Chuyển cùng evidence vào đầu/giữa/cuối
- Reading Status: Metadata/abstract verified; full paper unread

## P07 — ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs

- Paper ID: P07
- Title: ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs
- Authors: Yujia Qin et al. (đầy đủ tại nguồn)
- Year: 2023 preprint
- Venue: Chưa xác minh
- DOI/URL: [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789)
- Research Problem: Khả năng gọi API của open models
- Core Method: ToolBench, training và ToolEval
- Findings (author-reported): Abstract giới thiệu dataset, retriever và framework tool-use
- Limitations (lab interpretation unless stated): Không dùng API thật hoặc benchmark này khi chưa có permissions; chưa đọc full evaluation
- Related Learning Track: B/C
- Related Experiment: E10
- Reproduction Idea: Tool giả lập một schema và test invalid args
- Reading Status: Metadata/abstract verified; full paper unread

## P08 — Evidence dependence / provenance / belief aggregation

- Paper ID: P08 (reading slot, không phải paper đã chọn)
- Title / Authors / Year / Venue / DOI/URL: Chưa xác minh; không tự điền.
- Research Problem: nguồn phụ thuộc và đếm trùng evidence.
- Core Method / Findings / Limitations: Chưa xác minh.
- Related Learning Track: E/F
- Related Experiment: B04/B06/B07/B08
- Reproduction Idea: toy lineage graph với ground truth do người thiết kế định nghĩa.
- Reading Status: Needs source verification.
