# B05 — Outdated Memory

Trạng thái: Planned, chưa thực thi.

## Scenario

Memory snapshot v1 ghi 08:00; tài liệu hiện tại v2 ghi 09:00.

Xem [scenario](scenario.json).

## Expected behavior

Truy nguyên timestamp/version; đánh dấu stale, không âm thầm trộn phiên bản.

## Actual observation template

- Date / commit / config / mode:
- Input/source version và hash:
- Actual output / trace path:
- Expected vs actual:
- Lỗi và giả thuyết nguyên nhân:
- Kiểm tra tiếp theo:

## Failure analysis

Nếu memory thắng nguồn mới, kiểm tra retrieval ranking, expiry và prompt.

## Connection to future Multi-Agent

Hỏi điều gì xảy ra nếu hai agent nhận các bản nguồn khác nhau hoặc chia sẻ nguồn phụ thuộc. Đây là câu hỏi tương lai, không phải thử nghiệm giao tiếp. [Problem map](../../../future_multi_agent/problem_map.md).

[Checklist](CHECKLIST.md).
