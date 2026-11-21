import argparse
from pathlib import Path
import re
import sys
import unicodedata


NHAN = (
    'Do người dùng',
    'Hệ thống',
    'Ngữ cảnh',
    'Giới hạn hệ thống',
    'Ngầm',
)


def chuan_hoa(value):
    return ' '.join(unicodedata.normalize('NFC', value).split()).casefold()


def doc_phieu(path):
    text = Path(path).read_text(encoding='utf-8-sig')
    nhan_hop_le = {chuan_hoa(nhan): nhan for nhan in NHAN}
    ket_qua = {}
    loi = []
    for line in text.splitlines():
        if not re.match(r'^\s*\|\s*\d+\s*\|', line):
            continue
        cols = [col.strip() for col in line.strip().strip('|').split('|')]
        if len(cols) not in (3, 4):
            raise ValueError(f'{path}: bảng phải có 3 cột (Ca, Nhãn, Lý do) hoặc 4 cột (Ca, Mô tả, Nhãn, Lý do)')
        ca = int(cols[0])
        if ca not in range(1, 21) or ca in ket_qua:
            raise ValueError(f'{path}: số ca ngoài 1–20 hoặc bị lặp: {ca}')
        ket_qua[ca] = nhan_hop_le.get(chuan_hoa(cols[len(cols) - 2]))
        if ket_qua[ca] is None:
            loi.append(str(ca))
    if set(ket_qua) != set(range(1, 21)):
        raise ValueError(f'{path}: phải có đúng 20 ca, đánh số 1–20')
    if loi:
        raise ValueError(f'{path}: chưa điền hoặc nhãn không hợp lệ ở ca {", ".join(loi)}')
    return ket_qua


def doi_chieu(nguoi_1, nguoi_2):
    trung = [ca for ca in range(1, 21) if nguoi_1[ca] == nguoi_2[ca]]
    bat_dong = [ca for ca in range(1, 21) if nguoi_1[ca] != nguoi_2[ca]]
    return trung, bat_dong


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description='So hai phiếu 20 ca đã gắn nhãn; chỉ đọc và in kết quả.')
    parser.add_argument('--nguoi-1', required=True, type=Path)
    parser.add_argument('--nguoi-2', required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.nguoi_1.resolve() == args.nguoi_2.resolve():
            raise ValueError('Cần hai phiếu riêng, không dùng cùng một file cho cả hai người')
        nguoi_1 = doc_phieu(args.nguoi_1)
        nguoi_2 = doc_phieu(args.nguoi_2)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f'Chưa tính: {exc}')
        return 2
    trung, bat_dong = doi_chieu(nguoi_1, nguoi_2)
    print(f'Tỉ lệ trùng: {len(trung)}/20 = {len(trung) / 20:.0%}')
    print('Ngưỡng 80%: ' + ('ĐẠT' if len(trung) >= 16 else 'CHƯA ĐẠT; cần ghi định nghĩa đã sửa'))
    print('Ca bất đồng: ' + (', '.join(map(str, bat_dong)) or 'Không có'))
    print('\n| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |')
    print('| --: | --- | --- | --- | --- |')
    for ca in range(1, 21):
        print(f'| {ca} | {nguoi_1[ca]} | {nguoi_2[ca]} | {"Có" if ca in trung else "Không"} | ... |')
    print('\nĐây là mức trùng nhãn; công cụ không xác minh quá trình gắn nhãn độc lập.')
    print('Giữ nguyên hai phiếu gốc; ghi nhãn thống nhất và lý do bất đồng riêng sau khi trao đổi.')
    return 0 if len(trung) >= 16 else 1


if __name__ == '__main__':
    raise SystemExit(main())
