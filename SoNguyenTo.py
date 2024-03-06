""" by nnminh
Số nguyên tố là số nguyên lớn hơn 1 và chỉ chia hết cho 1 và chính nó.
Dựa vào định nghĩa này ta rút ra được những tính chất sau: Số 2 là SNT chẵn duy nhất, bởi vì những số chẵn lớn hơn 2 luôn chia hết cho 1, 2 và chính nó.
Nếu một số thỏa 2 tính chất trên thì đó là số nguyên tố.
Dựa vào đây ta có thể phân tích toán như sau: Giả sử N là số cần kiểm tra.
	1. Kiểm tra nếu N bằng 2 thì là SNT => Break
	2. Nếu N <= 1 thì không phải SNT => Break
	3. Nếu N là số chẵn thì không phải SNT => Break
	4. Lặp qua các số lẻ từ 2 -> (N - 1), nếu tồn tại số nào mà N chia hết thì không phải là SNT, nếu không thì đó là SNT.
"""

def NhapN():
	n = int(input())
	return n

def IsSoNguyenTo(n):
	if(n < 2):
		return False
	if(n == 2):
		return True
	if(n % 2 == 0):
		return False
	# Lặp qua các số lẻ nên bắt đầu từ 3 với bước nhảy là 2
	for i in range (3, n, 2):
		if(n % i == 0):
			return False
	return True

def main():
    n = NhapN()
    if(IsSoNguyenTo(n)):
        print(str(n) + " là số nguyên tố")
    else:
        print(str(n) + " không là số nguyên tố")

main()
