cnt = 10 # 問題文の条件から10スタート

while(True):
    bin_num = format(cnt, 'b') # 2進数に変換
    re_bin_num = bin_num[::-1]

    oct_num = format(cnt, 'o') # 8進数に変換
    re_oct_num = oct_num[::-1]

    dec_num = str(cnt)
    re_dec_num = dec_num[::-1]

    if(bin_num == re_bin_num and oct_num == re_oct_num and dec_num == re_dec_num):
        break

    cnt += 1

print(cnt) # 条件をみたしたときのcnt
