# B06 — Source Revision

Trạng thái: Planned, chưa thực thi.

## Scenario

Nguồn v1 được sửa thành v2; C1 dẫn v1, C2 dẫn nguồn khác.

Xem [scenario](scenario.json).

## Expected behavior

C1 cần reverify, C2 không tự bị invalidate; giữ lịch sử version.

## Actual observation template

- Date / commit / config / mode:
- Input/source version và hash:
- Actual output / trace path:
- Expected vs actual:
- Lỗi và giả thuyết nguyên nhân:
- Kiểm tra tiếp theo:

## Failure analysis

Hash đổi cho biết nội dung đổi, không tự biết claim nào đổi nghĩa.

## Connection to future Multi-Agent

Hỏi điều gì xảy ra nếu hai agent nhận các bản nguồn khác nhau hoặc chia sẻ nguồn phụ thuộc. Đây là câu hỏi tương lai, không phải thử nghiệm giao tiếp. [Problem map](../../../future_multi_agent/problem_map.md).

[Checklist](CHECKLIST.md).
