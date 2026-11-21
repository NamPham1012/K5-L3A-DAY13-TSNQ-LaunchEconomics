# Kiểm số độc lập — Lab 13

Đối chiếu bằng cách đọc trực tiếp hai CSV và cộng số liệu, độc lập với hàm `mo_hinh` trong `src/lab13.py`. Đây là kiểm tra theo công thức và giả định của lab, không phải dữ liệu đo thực tế. Các chi phí dùng phút nhân viên mang nhãn **simulated**.

## A — Kiểm tra bằng tay

- Đếm được 1.624 lượt chạy, 1.200 yêu cầu; 978 thành công, 74 làm lại và 148 chuyển nhân viên.
- Tiền token = Σ(token vào × 26/1.000 + token ra × 130/1.000) = **245.585,132 đ**; tool = **84.000 đ**.
- Xem lại = 890 phút × 2.000 = **1.780.000 đ [simulated]**; làm lại = 1.132 phút × 2.000 = **2.264.000 đ [simulated]**.
- Tổng = 245.585,132 + 84.000 + 1.780.000 + 2.264.000 = **4.373.585,132 đ [simulated]**. Chia 978 thành công = **4.471,97 đ/việc [simulated]**; khớp output A2.
- Chi phí cả hệ thống theo quy ước B3 của đề = (4.373.585,132 + 222 × 12.000) / 1.200 = **5.864,65 đ/yêu cầu [simulated]**.
- A3 khớp hướng dẫn: nội địa 824 yêu cầu, CPS 2.696 đ; hàng nặng 158, 8.221 đ; quốc tế 150, 22.515 đ; đối tác 68, 10.215 đ [tất cả CPS simulated].
- A4: 45.000 × 900/1.200 = 33.750 thành công/tháng trong phạm vi; 40.000.000/33.750 = 1.185,19 đ/việc; cộng CPS phạm vi ra **4.599 đ/việc [simulated]**. Giả định 45.000 là tổng lượng toàn hệ thống và cơ cấu mẫu giữ nguyên.

## B — Độ nhạy và giới hạn chạy

- Kiểm tra bằng tay: giá token gấp đôi làm CPS tăng 245.585,132/978 = **251,11 đ**, từ 4.471,97 lên **4.723,08 đ [simulated]**; mức tăng **5,61%**. Giá token giảm nửa làm mức giảm bằng một nửa mức tăng này.
- Xem lại gấp đôi: tăng 1.780.000/978 = 1.820,04 đ, tương đương **40,70% [simulated]**. Làm lại gấp đôi: tăng 2.264.000/978 = 2.314,93 đ, tương đương **51,77% [simulated]**. Lương tăng 25% làm CPS tăng **23,12% [simulated]**.
- Đọc trực tiếp CSV và áp dụng đúng quy ước đề về cắt lượt chạy cho kết quả: 1 lần **7.449.781 đ**, 2 lần **6.901.220 đ**, 3 lần **7.037.585 đ** chi phí cả hệ thống [simulated]. Như vậy 2 lần rẻ nhất theo quy ước này, còn CPS thấp nhất ở 1 lần.
- B4 theo giả định 948 ca xem lại 5 phút, 48 ca làm lại 9 phút: (224.513,29 + 948 × 5 × 2.000 + 48 × 9 × 2.000)/900 = **11.743 đ/việc [simulated]**. Nếu giả định 15,3 phút làm lại thì ra **12.415 đ/việc [simulated]** khi làm tròn; hướng dẫn ghi 12.414 đ, chênh 1 đ do làm tròn, không ảnh hưởng kết luận.
- Lưu ý diễn giải B3: phép tính cộng 12.000 đ cho *mọi* ca không thành công, trong khi chi phí trợ lý đã bao gồm phút làm lại của một số ca. Đây là quy ước của bài mẫu, không chứng minh đó là chi phí tăng thêm thực tế; muốn dự toán vận hành phải làm rõ chi phí làm lại và phần 12.000 đ có trùng nhau không.

## D1 — Kiểm tra cỡ mẫu

Theo công thức hai tỉ lệ của đề, z(0,975) ≈ 1,95996, z(0,80) ≈ 0,84162:

- p1 = 0,70; p2 = 0,75: n = 1.250,72, làm tròn lên **1.251 yêu cầu mỗi nhóm** nếu độc lập.
- Với 75 yêu cầu/nhân viên: DE = 1 + 74 × 0,02 = **2,48**. Cỡ mẫu điều chỉnh = ceil(1.251 × 2,48) = **3.103**, cần ceil(3.103/75) = **42 nhân viên mỗi nhóm**.
- 20 nhân viên/nhóm: cỡ mẫu hiệu dụng luôn nhỏ hơn 20/0,02 = **1.000**, không đạt 1.251. Sáu depot/nhóm: luôn nhỏ hơn **300**.
- Với p2 = 0,76: n = 858,27, làm tròn lên **859**. Giải 20m/(1 + (m − 1) × 0,02) ≥ 859 được **m ≥ 299**, với DE = **6,96**. Điều này chỉ là tính toán theo các giả định cỡ cụm bằng nhau và ICC của đề.

## Việc nhóm cần hoàn tất

Chuyển các số đã kiểm vào `bang_chi_phi.md`, phần D1 của `pilot_plan.yaml` và các hồ sơ liên quan; người kiểm số và người viết code cần tự giải thích công thức. Nhóm vẫn phải làm nhãn độc lập, chọn phương án pilot và thực hiện duyệt chéo thực tế.
