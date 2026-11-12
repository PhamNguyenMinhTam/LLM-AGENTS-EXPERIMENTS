# B01 — Correct Source

Trạng thái: Implemented fixture/mock, chưa live inference.

## Scenario

Một tài liệu giả lập ghi thời gian mở cửa; claim dẫn đúng đoạn.

Xem [scenario](scenario.json).

## Expected behavior

Quote/source ID/hash và answer khớp fixture; phản ví dụ sai quote/nguồn/answer bị từ chối.

## Actual observation template

- Date / commit / config / mode:
- Input/source version và hash:
- Actual output / trace path:
- Expected vs actual:
- Lỗi và giả thuyết nguyên nhân:
- Kiểm tra tiếp theo:

## Failure analysis

Nếu paraphrase đúng bị từ chối, đó là giới hạn exact-match, chưa phải lỗi suy luận.

## Connection to future Multi-Agent

Hỏi điều gì xảy ra nếu hai agent nhận các bản nguồn khác nhau hoặc chia sẻ nguồn phụ thuộc. Đây là câu hỏi tương lai, không phải thử nghiệm giao tiếp. [Problem map](../../../future_multi_agent/problem_map.md).

[Checklist](CHECKLIST.md).
