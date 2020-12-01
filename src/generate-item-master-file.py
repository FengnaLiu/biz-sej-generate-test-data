import sys
from datetime import datetime, timedelta, timezone

if __name__ == '__main__':
    today = datetime.now(timezone(timedelta(hours=9))).date()
    today_str = today.strftime("%Y%m%d")

    N = "000000006"

    path = 'sejitem_item_ok.dat'
    path_1 = 'sejitem_item_invalid_terms.dat'
    path_2 = 'sejitem_item_unparseable_date.dat'
    path_3 = 'sejitem_item_unexpected.dat'
    path_4 = 'sejitem_item_marker_wrong.dat'
    path_5 = 'sejitem_item_file_size_1.dat'
    path_6 = 'sejitem_item_file_size_2.dat'
    path_7 = 'sejitem_item_today_check.dat'
    path_8 = 'sejitem_item_new_guidance_image.dat'
    path_9 = 'sejitem_item_bulk_purchase_handle_flag.dat'
    header = "H" + today_str.ljust(134, " ")
    header_error = "H" + "20200101".ljust(134, " ")
    tailer = "E" + N.ljust(134, " ")
    tailer_error = "E" +"000000005".ljust(134, " ")

    entry_ok_1="D" + str(1 + 900000).rjust(6, "0") + "20190101" + "99999999" + "00B20022" + (
                            "kananame" + str(1+ 900000).rjust(6, "0")).ljust(30, " ") + (
                            "kanjiname" + str(1+ 900000).rjust(6, "0")).ljust(44,
                                                                          " ") + "11001012010980 4901777348479" + "\r\n"
    entry_ok_2 = "D" + str(2 + 900000).rjust(6, "0") + "20190101" + "20201011" + "00B20022" + (
            "kananame" + str(2 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(2 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11001012010980 4901777348479" + "\r\n"

    entry_ok_3 = "D" + str(3 + 900000).rjust(6, "0") + "20180101" + "20201011" + "00B20022" + (
            "kananame" + str(3 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(3 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11001012010980 4901777348479" + "\r\n"

    entry_ok_4 = "D" + str(4 + 900000).rjust(6, "0") + "20180101" + "99999999" + "00B20022" + (
            "kananame" + str(4 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(4 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11001012010980 4901777348479" + "\r\n"


    entry_invalid_terms_1 = "D" + str(6 + 900000).rjust(6, "0") + "20180101" + "99999999" + "00B20022" + (
            "kananame" + str(6 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(6 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11001012010980 4901777348479" + "\r\n"


    entry_invalid_terms_2 = "D" + str(6 + 900000).rjust(6, "0") + "20190101" + "99999999" + "00B20022" + (
            "kananame" + str(6 + 900000).rjust(6, "0")).ljust(30, " ") + (
                                    "kanjiname" + str(6 + 900000).rjust(6, "0")).ljust(44,
                                                                                       " ") + "11001012010980 4901777348479" + "\r\n"

    entry_unparseable_date = "D" + str(7 + 900000).rjust(6, "0") + "20181301" + "99999999" + "00B20022" + (
            "kananame" + str(7 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(7 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11001012010980 4901777348479" + "\r\n"

    #unexpected??
    entry_unexpected = "D" + str(8 + 900000).rjust(6, "0") + "20180101" + "99999999" + "00B20022" + (
            "kananame" + str(8 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(8 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11001012010980 4901777348479" + "\r\n"

    entry_marker = "H" + str(9 + 900000).rjust(6, "0") + "20180101" + "99999999" + "00B20022" + (
            "kananame" + str(9 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(9 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11001012010980 4901777348479" + "\r\n"

    entry_file_size_1 = "D" + str(10 + 900000).rjust(6, "0") + "20180101" + "99999999" + "00B20022" + (
            "kananame" + str(10 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(10 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "1100101201098 4901777348479" + "\r\n"

    entry_new_guidance_image ="D" + str(11 + 900000).rjust(6, "0") + "20180101" + "99999999" + "00B20022" + (
            "kananame" + str(11 + 900000).rjust(6, "0")).ljust(30, " ") + (
                         "kanjiname" + str(11 + 900000).rjust(6, "0")).ljust(44,
                                                                            " ") + "11002012010980 4901777348479" + "\r\n"

    entry_bulk_purchase_handle_flag = "D" + str(12 + 900000).rjust(6, "0") + "20180101" + "99999999" + "00B20022" + (
            "kananame" + str(12 + 900000).rjust(6, "0")).ljust(30, " ") + (
                                       "kanjiname" + str(12 + 900000).rjust(6, "0")).ljust(44,
                                                                                           " ") + "1100101201098024901777348479" + "\r\n"



    with open(path, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_ok_4.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_1, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_invalid_terms_1.encode(encoding='utf-8'))
        f.write(entry_invalid_terms_2.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_2, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_unparseable_date.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_3, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_unexpected.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_4, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_marker.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_5, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_file_size_1.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_6, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_ok_4.encode(encoding='utf-8'))
        f.write(tailer_error.encode(encoding='utf-8'))

    with open(path_7, mode='wb') as f:
        f.write(header_error.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_ok_4.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_8, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_new_guidance_image.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))

    with open(path_9, mode='wb') as f:
        f.write(header.encode(encoding='utf-8'))
        f.write(entry_ok_1.encode(encoding='utf-8'))
        f.write(entry_ok_2.encode(encoding='utf-8'))
        f.write(entry_ok_3.encode(encoding='utf-8'))
        f.write(entry_bulk_purchase_handle_flag.encode(encoding='utf-8'))
        f.write(tailer.encode(encoding='utf-8'))
