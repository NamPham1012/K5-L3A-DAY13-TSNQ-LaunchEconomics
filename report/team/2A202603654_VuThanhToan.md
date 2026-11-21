# Báo cáo cá nhân — Vũ Thành Toàn — 2A202603654

## 1. Thông tin thành viên

- Họ tên: Vũ Thành Toàn
- MSSV: 2A202603654
- Email: thanhtoana7hha@gmail.com
- Vai trong nhóm: Người gắn nhãn 1; đọc đề và theo dõi điều kiện "Xong khi" của các checkpoint.

## 2. Phần việc phụ trách

- Gắn nhãn 20 ca lỗi ở nhiệm vụ C theo năm loại của Google PAIR (Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm), so với bộ nhãn của người 2.
- Đọc đề, rà điều kiện hoàn thành từng checkpoint và checklist nộp bài.
- Viết công cụ đối chiếu hai phiếu nhãn `src/doi_chieu_nhan.py`.

## 3. Đóng góp cụ thể

- Gắn nhãn 20 ca (cột "Nhãn người 1" trong [bang_loi.md](bang_loi.md), chép lại ở [nhan_nguoi_1_ToanVT.md](nhan_nguoi_1_ToanVT.md)). Phân bố: Hệ thống 6, Do người dùng 4, Ngữ cảnh 4, Giới hạn hệ thống 4, Ngầm 3.
- So với nhãn người 2 (Sơn): trùng 20/20 = 100%, vượt ngưỡng 80% (16/20); không có ca bất đồng nên không cần sửa định nghĩa.
- Viết `src/doi_chieu_nhan.py`: đọc hai phiếu, kiểm tra đủ 20 ca và nhãn hợp lệ, in tỉ lệ trùng và ca bất đồng; chỉ đọc, không sửa dữ liệu đầu vào. Chạy trên hai phiếu cho kết quả 20/20, khớp số đếm tay.
- Rà điều kiện hoàn thành so với [CHECKPOINTS.md](../../CHECKPOINTS.md) và [SUBMISSION.md](../../SUBMISSION.md):

| Checkpoint | Điều kiện | Trạng thái khi rà |
| --- | --- | --- |
| CP1 · A | A1 đạt 3 phép thử (1,20 · 1,25 · 1,25); A2, A3 đủ dòng; số giả lập có nhãn `simulated` | Đạt theo output đã lưu `src/ket_qua_lab13.txt` |
| CP2 · B | B1 đủ 9 kịch bản; B2, B3, B4 có số; xếp hạng 3 yếu tố | Đã có trong `bang_chi_phi.md` |
| CP3 · C | Hai bộ nhãn, ≥ 16/20 trùng; bảng khắc phục đủ 5 loại, có vai trò phụ trách | 20/20; bảng khắc phục đủ 5 loại |
| CP4 · D | YAML đọc được bằng `yaml.safe_load`, không còn `?`; ≥ 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ | `safe_load` đọc được, không còn `?`, có 4 luật dừng |
| CP5 · E | 3 chỉ số có số; ≥ 6 event có `trace_id`; 2 dòng rủi ro; hồ sơ 7 mục; đề xuất là Go / Go có điều kiện / No-go | Đủ; đề xuất No-go |
| Nộp bài | Không có từ bị cấm (RULES.md); đủ báo cáo cá nhân; phiếu duyệt chéo | Không có từ bị cấm; đủ 3 báo cáo; `phieu_cham.md` chờ buổi duyệt chéo |

## 4. Bằng chứng

- [bang_loi.md](bang_loi.md): cột "Nhãn người 1" và kết quả đối chiếu 20/20.
- [nhan_nguoi_1_ToanVT.md](nhan_nguoi_1_ToanVT.md): phiếu nhãn người 1 (bản chép lại).
- [src/doi_chieu_nhan.py](../../src/doi_chieu_nhan.py): lệnh chạy:
  `python src/doi_chieu_nhan.py --nguoi-1 report/team/nhan_nguoi_1_ToanVT.md --nguoi-2 report/team/nhan_nguoi_2_SonLNH.md` → `Tỉ lệ trùng: 20/20 = 100%`, `Ngưỡng 80%: ĐẠT`.
- Commit: nhánh `2A202603654_VuThanhToan` (điền hash sau khi commit).

## 5. Công cụ AI đã dùng

- Codex và Claude Code: giải thích định nghĩa năm loại lỗi, gợi ý và soát code `doi_chieu_nhan.py`, rà điều kiện hoàn thành theo đề.
- Nhãn 20 ca do tôi tự chọn; AI không chọn nhãn thay.
- Tự kiểm tra: đếm tay số ca trùng giữa hai cột nhãn (20/20) và so với output của công cụ; tự chạy `yaml.safe_load` và tìm từ bị cấm theo RULES.md trong hồ sơ.
- Lưu ý trung thực: không còn phiếu gốc ghi giờ, nên tính độc lập của hai bộ nhãn dựa trên khai báo của hai người gắn nhãn, chưa xác minh được bằng tài liệu.

## 6. Tự đánh giá

- Hoàn thành phần gắn nhãn, đối chiếu và rà điều kiện; công cụ so nhãn chạy được trên cả hai phiếu.
- Hạn chế: không lưu phiếu gốc có giờ trước khi so nhãn. Lần sau sẽ ghi nhãn vào file riêng, commit trước khi xem nhãn người kia.
