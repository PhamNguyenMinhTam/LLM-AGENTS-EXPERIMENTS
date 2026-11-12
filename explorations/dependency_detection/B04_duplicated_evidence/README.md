# B04 — Duplicated Evidence

Trạng thái: Planned, chưa thực thi.

## Scenario

S2 sao chép S1, S3 độc lập; cả ba cùng khẳng định một claim.

Xem [scenario](scenario.json).

## Expected behavior

Ghi S2 depends_on S1; báo hai nhóm nguồn, không ba bằng chứng độc lập.

## Actual observation template

- Date / commit / config / mode:
- Input/source version và hash:
- Actual output / trace path:
- Expected vs actual:
- Lỗi và giả thuyết nguyên nhân:
- Kiểm tra tiếp theo:

## Failure analysis

Cùng văn bản không tự chứng minh phụ thuộc; cần thông tin lineage ground truth.

## Connection to future Multi-Agent

Hỏi điều gì xảy ra nếu hai agent nhận các bản nguồn khác nhau hoặc chia sẻ nguồn phụ thuộc. Đây là câu hỏi tương lai, không phải thử nghiệm giao tiếp. [Problem map](../../../future_multi_agent/problem_map.md).

[Checklist](CHECKLIST.md).
