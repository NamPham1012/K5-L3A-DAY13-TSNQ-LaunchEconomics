# Báo cáo nhóm — Lab 13: Launch & Economics

**Trạng thái: bản nháp.** Nhóm cần hoàn thành các mục đang chờ, thống nhất đề xuất và cập nhật kết quả duyệt chéo trước khi nộp.

## 1. Thông tin nhóm

- Tên nhóm: TSNQ. Lớp: chờ nhóm xác nhận trong [TEAM.md](../../TEAM.md).
- Thành viên và đóng góp: xem [TEAM.md](../../TEAM.md); hiện đã ghi Phạm Văn Nam — 2A202603681, các thành viên khác cần bổ sung.

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí của trợ lý hoàn phí LogiX-VN, khả năng sử dụng, rủi ro khi mắc lỗi và phương án pilot có đối chứng. Nhóm dùng dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lần chạy, tính theo giá và công thức của lab; kết quả liên quan đến phút nhân viên được ghi nhãn `simulated`.

## 3. Giải pháp và tiến độ

- **A–B — Chi phí và độ nhạy:** chương trình [lab13.py](../../src/lab13.py) chạy ba phép thử A1 đạt, tính chi phí theo loại, chi phí cố định và các kịch bản; kết quả ở [bang_chi_phi.md](bang_chi_phi.md), đối chiếu ở [kiem_so.md](kiem_so.md).
- **C — Lỗi:** chờ hai thành viên gắn nhãn độc lập 20 ca, so nhãn và điền cách khắc phục vào [bang_loi.md](bang_loi.md).
- **D — Pilot:** code đã tính các cỡ mẫu D1; nhóm cần chọn cách phân nhóm, ghi đánh đổi, luật dừng và hoàn thiện [pilot_plan.yaml](pilot_plan.yaml).
- **E — Chỉ số và hồ sơ:** code đã tính thử ba chỉ số E1; nhóm cần hoàn thiện event, rủi ro trong [chi_so.md](chi_so.md) và thống nhất đề xuất tại [ho_so_launch_v0.md](ho_so_launch_v0.md).
- **Duyệt chéo:** chờ chấm nhóm khác và ghi kết quả thực tế vào [phieu_cham.md](phieu_cham.md).

## 4. Kết quả bước đầu

- Chi phí trợ lý trên mỗi việc thành công: **4.472 đ [simulated]**; theo quy ước B3 của lab, chi phí cả hệ thống là **5.865 đ/yêu cầu [simulated]**, chưa cộng cố định.
- Phương án tối đa 2 lần chạy cho chi phí cả hệ thống thấp nhất trong ba kịch bản: **6.901.220 đ [simulated]**. Làm lại gấp đôi làm CPS tăng **51,8% [simulated]**.
- Mẫu cho thấy **82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày; **4,25%** mở lại trong 7 ngày. Không có đối chứng trong đợt chạy thử nên không suy ra tác động nhân quả.
- Theo giả định D1, cần **1.251 yêu cầu độc lập mỗi nhóm** để phát hiện chênh 5 điểm; chia theo 20 nhân viên mỗi nhóm không đạt cỡ mẫu hiệu dụng này với ICC 0,02.
- **Đề xuất cuối và kết quả duyệt chéo: chờ nhóm thống nhất và ghi theo kết quả thực tế.**

## 5. Khó khăn và cách xử lý

Môi trường Python ban đầu thiếu `scipy`; đã tạo `.venv`, cài `requirements.txt` và chạy lại chương trình thành công. Chi phí trợ lý và chi phí cả hệ thống có mẫu số, phạm vi khác nhau; nhóm cần giải thích rõ giả định B3, gồm khả năng trùng chi phí làm lại khi dự toán thực tế.

## 6. Tổng hợp đóng góp

Phạm Văn Nam phụ trách chạy code và tham gia kiểm số với hỗ trợ của Codex; chi tiết, bằng chứng và đóng góp của các thành viên khác cần được cập nhật trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

Phút xem lại và làm lại là **simulated**; cần đo thời gian thực trong pilot. Kết quả phụ thuộc giả định giá, cơ cấu yêu cầu và ICC; cần kiểm tra tính khả thi cỡ mẫu, rủi ro ảnh hưởng giữa các nhóm và chi phí thực tế trước khi đưa ra quyết định.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức của lab](../../docs/du_lieu_va_cong_thuc.md).
- [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- Hai file dữ liệu `src/logix_runs.csv`, `src/logix_requests.csv` và chương trình `src/lab13.py` trong repo.
