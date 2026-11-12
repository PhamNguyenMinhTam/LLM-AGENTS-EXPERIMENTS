# Coding Agent

## Trạng thái

Scaffold: chỉ đọc file và ast.parse; không sinh code bằng model trong CLI này, không import/exec/subprocess code. Có thể dùng slice riêng để quan sát phản hồi model, sau đó review thủ công.

## Setup và chạy

Từ repository root, tạo venv và `python -m pip install -r requirements.txt` theo [setup](../../README.md). Không cần Ollama cho demo.

```bash
python -m apps.coding_agent.app --source apps/coding_agent/fixtures/example.py
```

`config.yaml` mô tả kế hoạch, CLI chưa nạp file này; thay model qua config slice E01 hiện có.

## Workflow mục tiêu

Task → kế hoạch ngắn → sinh code → sandbox unit tests → feedback → sửa có giới hạn → kết quả/logs.

## Tiêu chí hoàn thành

Có trace mỗi bước, negative tests, stopping condition, dữ liệu development/final tách biệt và phân tích ít nhất một lỗi. Planning/tool loop, sandbox và test/repair loop đều Planned Q2. Không coi ast.parse là sandbox hoặc bộ kiểm chứng an toàn.

Theo dõi [checklist](CHECKLIST.md), [mini-mOS](../../mini_mos/README.md) và [roadmap](../../ROADMAP.md).
