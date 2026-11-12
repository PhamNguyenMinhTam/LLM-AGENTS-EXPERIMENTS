# B07 — Dependency Propagation

Trạng thái: Planned, chưa thực thi.

## Scenario

S1 → C1 → C2; C3 chỉ dựa S2. S1 bị rút lại.

Xem [scenario](scenario.json).

## Expected behavior

Liệt kê C1/C2 cần kiểm tra; giữ C3; tránh vòng lặp khi graph có cycle.

## Actual observation template

- Date / commit / config / mode:
- Input/source version và hash:
- Actual output / trace path:
- Expected vs actual:
- Lỗi và giả thuyết nguyên nhân:
- Kiểm tra tiếp theo:

## Failure analysis

Dependency biểu thị ảnh hưởng tiềm năng, không chứng minh mọi kết luận downstream sai.

## Connection to future Multi-Agent

Hỏi điều gì xảy ra nếu hai agent nhận các bản nguồn khác nhau hoặc chia sẻ nguồn phụ thuộc. Đây là câu hỏi tương lai, không phải thử nghiệm giao tiếp. [Problem map](../../../future_multi_agent/problem_map.md).

[Checklist](CHECKLIST.md).
