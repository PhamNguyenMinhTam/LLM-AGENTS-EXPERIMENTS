# B03 — Conflicting Sources

Trạng thái: Planned, chưa thực thi.

## Scenario

S1 và S2 cùng ngày nhưng ghi giờ mở cửa khác nhau, chưa có nguồn ưu tiên.

Xem [scenario](scenario.json).

## Expected behavior

Giữ cả hai provenance, nêu mâu thuẫn và chưa kết luận; không chọn theo số phiếu.

## Actual observation template

- Date / commit / config / mode:
- Input/source version và hash:
- Actual output / trace path:
- Expected vs actual:
- Lỗi và giả thuyết nguyên nhân:
- Kiểm tra tiếp theo:

## Failure analysis

Kết luận chắc chắn có thể do bỏ qua nguồn hoặc prompt thiên lệch.

## Connection to future Multi-Agent

Hỏi điều gì xảy ra nếu hai agent nhận các bản nguồn khác nhau hoặc chia sẻ nguồn phụ thuộc. Đây là câu hỏi tương lai, không phải thử nghiệm giao tiếp. [Problem map](../../../future_multi_agent/problem_map.md).

[Checklist](CHECKLIST.md).
