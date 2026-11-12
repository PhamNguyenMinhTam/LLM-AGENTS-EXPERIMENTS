# B02 — Incorrect Source

Trạng thái: Planned, chưa thực thi.

## Scenario

Nguồn S1 ghi một giờ sai so với nguồn chuẩn S0 do người thiết kế cung cấp.

Xem [scenario](scenario.json).

## Expected behavior

Không xem có quote là đủ đúng; báo chênh lệch với nguồn chuẩn và đánh dấu unverified.

## Actual observation template

- Date / commit / config / mode:
- Input/source version và hash:
- Actual output / trace path:
- Expected vs actual:
- Lỗi và giả thuyết nguyên nhân:
- Kiểm tra tiếp theo:

## Failure analysis

Quote chính xác từ nguồn sai vẫn sai; cần phân biệt độ tin cậy nguồn với liên kết nguồn.

## Connection to future Multi-Agent

Hỏi điều gì xảy ra nếu hai agent nhận các bản nguồn khác nhau hoặc chia sẻ nguồn phụ thuộc. Đây là câu hỏi tương lai, không phải thử nghiệm giao tiếp. [Problem map](../../../future_multi_agent/problem_map.md).

[Checklist](CHECKLIST.md).
