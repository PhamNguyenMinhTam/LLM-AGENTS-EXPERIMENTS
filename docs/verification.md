# Biên bản xác minh — 2026-11-08

## Đã kiểm tra tại local
- Tạo cấu trúc 12 thí nghiệm với đủ README, CHECKLIST, EVALUATION, YAML, runner và results/.gitkeep.
- Tài liệu nghiên cứu bằng tiếng Việt; 12 bảng tiêu chí có công thức, đơn vị, nguồn, giới hạn; không có kết quả benchmark.
- 27 unit tests vượt qua trên Windows/Python 3.14.7: config, parsing Ollama, metric, schema, dry-run, mock export, timeout, chống rò rỉ đáp án và final/adaptation.
- Mock chỉ dùng trong thư mục tạm của pytest; không commit output mock.
- CI cấu hình Ubuntu/Python 3.11–3.13, không gọi Ollama/GPU. Chưa có lần chạy GitHub Actions để xác minh từ xa.
- .env không được commit; .env.example chỉ có placeholder. Các raw output bị gitignore.

## Branch và xuất bản
Tạo main và 12 branch trực tiếp từ cùng main, mỗi branch có commit điều kiện riêng; xem [branches.md](branches.md). Không merge về main. Kết thúc ở main, worktree sạch.
GitHub connector có login mWorkSTE-Tech nhưng không có công cụ tạo repository/push Git. `gh auth status` cho biết CLI chưa đăng nhập. Danh sách repository connector trả về cho owner này rỗng; không có bằng chứng repository đích đã được tạo.
Vì thiếu xác thực CLI, chưa tạo private repository, chưa đặt default branch từ xa, chưa push main/12 branch và chưa chạy Actions. Yêu cầu push main trước khi tạo branch chỉ có thể hoàn tất sau khi xác thực; lịch sử local vẫn giữ mỗi branch xuất phát trực tiếp main.

## Trạng thái chức năng
Chạy được: validate YAML/dataset, dry-run không gọi API, Ollama non-streaming có timeout/preflight digest/quantization, exact-match, JSONL/CSV/manifest.
Chưa xác minh thật: Ollama trên hai laptop Ubuntu, model tags và phần cứng thực tế. Máy phát triển không có Ollama.
Scaffold: các điều kiện cần model/dataset/hardware nghiên cứu; tool loop, memory, feedback, streaming TTFT, collector resource/energy, coding sandbox, bootstrap/plot chưa triển khai. Live từ chối can thiệp tools/memory/feedback. Không diễn giải control thành kết quả adaptation.
Smoke datasets chỉ có ví dụ tự soạn, không đủ suy luận thống kê; E08 trên branch dùng ví dụ độ khó tạm thời chưa được người chấm xác nhận.

## Xuất bản sau khi đăng nhập
```bash
gh auth login
gh api user --jq .login
gh repo view mWorkSTE-Tech/llm-agent-experiments
```
Chỉ khi xác minh repo đích chưa tồn tại (HTTP 404 với tài khoản có quyền), tạo mới:
```bash
gh repo create mWorkSTE-Tech/llm-agent-experiments --private --description "Experimental evaluation of independent LLM agents across models, hardware, domains, and adaptation strategies." --source . --remote origin --push
git push origin 'refs/heads/experiment/*:refs/heads/experiment/*'
gh repo edit mWorkSTE-Tech/llm-agent-experiments --default-branch main
gh run list --limit 5
```
Nếu repo tồn tại, fetch và so sánh nội dung/lịch sử trước; không force-push, không chạy tạo mới và không ghi đè dữ liệu. Nếu tài khoản CLI khác owner dự kiến, xác định đúng owner trước khi xuất bản.

## Ki?m tra b? sung cu?i
- 36 YAML ?i?u ki?n tr?n c?c experiment branch qua dry-run; kh?ng g?i API.
- CLI module v? wrapper E01 qua dry-run v?i bi?n m?u; setup_ubuntu.sh qua bash -n (ki?m tra c? ph?p, ch?a ch?y c?i Ubuntu).
- C?c li?n k?t Markdown n?i b? tr?n main h?p l?; 130 t?p ???c theo d?i.
- Qu?t c?c t?p theo d?i tr?n c? 13 branch: kh?ng c? .env/private key, kh?ng ph?t hi?n m?u token GitHub/OpenAI ph? bi?n; ??y kh?ng ph?i b?o ??m ph?t hi?n m?i d?ng secret.
- C?p nh?t bi?n b?n cu?i tr?n main r?i rebase c? ki?m so?t 12 commit ?i?u ki?n l?n main m?i, gi? m?i branch c? ??ng m?t commit ri?ng v? cha tr?c ti?p l? main.
