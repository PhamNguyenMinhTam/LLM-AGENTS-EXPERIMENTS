# Quy ước thí nghiệm
Đọc [ma trận](experiment_matrix.md). Mỗi E có kế hoạch, checklist, tiêu chí và runner dùng chung.
Main chứa protocol và điều kiện đối chứng. Mỗi experiment branch có kế hoạch điều kiện riêng xuất phát trực tiếp từ main; chưa merge về main.
Đổi điều kiện bằng bản sao YAML, không sửa file sau khi chạy. Các trường liên quan model/hardware/prompt cần thay trên từng agent khi thích hợp.
E10–E12 mới có protocol cho can thiệp, runtime can thiệp chưa triển khai. Chạy control không kiểm chứng giả thuyết adaptation.
