# Biên bản xác minh — 2026-11-08

## Repository đích
[PhamNguyenMinhTam/LLM-AGENTS-EXPERIMENTS](https://github.com/PhamNguyenMinhTam/LLM-AGENTS-EXPERIMENTS) là repository duy nhất sử dụng. Origin đã trỏ đúng URL. Không tạo repository mới, không đổi tên hoặc tự thay visibility.
Đã fetch và kiểm tra remote: chưa có remote branch tại thời điểm rà soát. Trước push phải kiểm tra lại để không ghi đè thay đổi mới.

## Kiểm chứng local
- Có framework dùng chung và đầy đủ tài liệu E01–E12 bằng tiếng Việt.
- 27 unit tests trước đợt sửa đã đạt trên cả 13 branch; 36 YAML điều kiện đã qua dry-run không gọi API.
- Thêm trường timestamp UTC, lint Ruff và các yêu cầu mục lục, Mermaid, roadmap/checklist mới. Kết quả lint/tests đợt mới ghi sau khi chạy.
- Mock chỉ ghi output vào thư mục tạm pytest; không có kết quả benchmark giả trong repository.
- Có CI Ubuntu/Python 3.11–3.13 chạy lint/tests không cần Ollama/GPU; chưa xác minh Actions từ xa.
- Không commit .env hoặc token; quét mẫu token/private key phổ biến không thay thế rà soát bảo mật đầy đủ.

## Giới hạn
Chưa chạy inference thật trên hai laptop Ubuntu; máy phát triển không có Ollama. Tools, memory, feedback, streaming TTFT, resource/energy collector, coding sandbox, bootstrap/plot vẫn là scaffold. Runtime từ chối các can thiệp chưa triển khai; null/N/A chỉ trạng thái chưa đo.
Smoke datasets chỉ kiểm tra kỹ thuật, không đủ để suy luận khoa học. E08 branch có nhãn độ khó minh họa chưa được xác nhận.

## Lịch sử và đồng bộ
12 branch được tạo từ cùng commit main trước đợt sửa. Mỗi branch có commit điều kiện riêng; cập nhật framework từ main được merge có kiểm soát vào từng branch, không merge experiment về main, không rewrite/xóa lịch sử và không force-push.
Thứ tự tạo branch local đã xảy ra trước khi có quyền push; không dựng lại lịch sử chỉ để giả lập thứ tự. Push main trước, sau đó push 12 branch khi có quyền.

## Xác thực và xuất bản
Nếu chưa có quyền Git, đăng nhập bằng `gh auth login` với tài khoản có quyền push repo đích, rồi kiểm tra `gh api user --jq .login`.
```bash
git fetch origin
git push -u origin main
git push origin 'refs/heads/experiment/*:refs/heads/experiment/*'
git ls-remote --heads origin
gh run list --repo PhamNguyenMinhTam/LLM-AGENTS-EXPERIMENTS --limit 10
```
Không tạo repo, không đổi visibility. Nếu remote có lịch sử mới, fetch/đối chiếu và tích hợp bảo toàn dữ liệu trước khi push.
