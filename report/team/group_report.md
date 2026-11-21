# Báo cáo nhóm — Lab 13: Launch & Economics

**Trạng thái: bản nháp chờ hoàn tất.** Cần hoàn thành duyệt chéo thực tế, báo cáo cá nhân của Toàn, xác nhận nhãn gốc và thống nhất kế hoạch trước khi nộp.

## 1. Thông tin nhóm

- Tên nhóm: TSNQ. Lớp: L3A, xem [TEAM.md](../../TEAM.md).
- Thành viên và đóng góp: xem [TEAM.md](../../TEAM.md); nhóm 3 thành viên: Phạm Văn Nam (2A202603681), Vũ Thành Toàn (2A202603654), Lê Nguyễn Hoàng Sơn (2A202603686).

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí của trợ lý hoàn phí LogiX-VN, khả năng sử dụng, rủi ro khi mắc lỗi và phương án pilot có đối chứng. Nhóm dùng dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lần chạy, tính theo giá và công thức của lab; kết quả liên quan đến phút nhân viên được ghi nhãn `simulated`.

## 3. Giải pháp và tiến độ

- **A–B — Chi phí và độ nhạy:** chương trình [lab13.py](../../src/lab13.py) chạy ba phép thử A1 đạt, tính chi phí theo loại, chi phí cố định và các kịch bản; kết quả ở [bang_chi_phi.md](bang_chi_phi.md), đối chiếu ở [kiem_so.md](kiem_so.md).
- **C — Lỗi:** [bang_loi.md](bang_loi.md) có hai cột nhãn, bảng khắc phục 5 loại và kết quả đối chiếu 20/20 theo xác nhận của nhóm. Chưa xác minh được hai bộ nhãn có gắn độc lập hay không, và chưa có phiếu gốc; cần lưu phiếu gốc trước khi cộng nhãn thống nhất.
- **D — Pilot:** [pilot_plan.yaml](pilot_plan.yaml) đề xuất chia theo nhân viên 20 + 20, mức chênh 6 điểm, 4 luật dừng và rollback 30 phút; đánh đổi và lịch còn chờ xác nhận.
- **E — Chỉ số và hồ sơ:** [chi_so.md](chi_so.md) có ba chỉ số, 10 event, 3 dòng rủi ro; đề xuất hiện tại ở [ho_so_launch_v0.md](ho_so_launch_v0.md) là No-go.
- **Duyệt chéo:** chờ chấm nhóm khác và ghi kết quả thực tế vào [phieu_cham.md](phieu_cham.md).

## 4. Kết quả bước đầu

- Chi phí trợ lý trên mỗi việc thành công: **4.472 đ [simulated]**; theo quy ước B3 của lab, chi phí cả hệ thống là **5.865 đ/yêu cầu [simulated]**, chưa cộng cố định.
- Phương án tối đa 2 lần chạy cho chi phí cả hệ thống thấp nhất trong ba kịch bản: **6.901.220 đ [simulated]**. Làm lại gấp đôi làm CPS tăng **51,8% [simulated]**.
- Mẫu cho thấy **82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày; **4,25%** mở lại trong 7 ngày. Không có đối chứng trong đợt chạy thử nên không suy ra tác động nhân quả.
- Theo giả định D1, cần **1.251 quan sát độc lập mỗi nhóm** cho mức chênh 5 điểm; với 20 nhân viên/nhóm và ICC 0,02 thì không đạt. Phương án 6 điểm cần **859 quan sát hiệu dụng/nhóm**, tương đương tối thiểu **5.980 yêu cầu thực tế/nhóm** nếu có 20 nhân viên và 299 yêu cầu/người, DE 6,96.
- **Đề xuất của hồ sơ: No-go**, chờ nhóm thống nhất (xem [ho_so_launch_v0.md](ho_so_launch_v0.md)). Chưa có kết quả duyệt chéo thực tế; ghi vào [phieu_cham.md](phieu_cham.md) sau khi chấm nhóm được phân công.

## 5. Khó khăn và cách xử lý

Nhóm chỉ có 3 thành viên (Phạm Văn Nam, Vũ Thành Toàn, Lê Nguyễn Hoàng Sơn), ít hơn 4 người theo SUBMISSION.md, nên một người kiêm hai vai: Nam viết code và kiểm số; Toàn gắn nhãn 1; Sơn gắn nhãn 2 và giữ hồ sơ. Chưa có phiếu gốc của hai người gắn nhãn, nên không khẳng định hai bộ nhãn độc lập.

Môi trường Python ban đầu thiếu `scipy`; đã tạo `.venv`, cài `requirements.txt` và chạy lại chương trình thành công. Chi phí trợ lý và chi phí cả hệ thống có mẫu số, phạm vi khác nhau; nhóm cần giải thích rõ giả định B3, gồm khả năng trùng chi phí làm lại khi dự toán thực tế.

## 6. Tổng hợp đóng góp

Nam phụ trách chạy code và kiểm số; Toàn gắn nhãn lỗi người 1; Sơn gắn nhãn người 2 và giữ hồ sơ launch. Chi tiết trong [TEAM.md](../../TEAM.md); cả ba dùng Codex hỗ trợ.

## 7. Hạn chế và hướng cải thiện

Phút xem lại và làm lại là **simulated**; cần đo thời gian thực trong pilot. Kết quả phụ thuộc giả định giá, cơ cấu yêu cầu và ICC; cần kiểm tra tính khả thi cỡ mẫu, rủi ro ảnh hưởng giữa các nhóm và chi phí thực tế trước khi đưa ra quyết định.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức của lab](../../docs/du_lieu_va_cong_thuc.md).
- [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- Hai file dữ liệu `src/logix_runs.csv`, `src/logix_requests.csv` và chương trình `src/lab13.py` trong repo.
