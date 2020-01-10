# coding: utf-8
import decimal


if __name__ == '__main__':
    a =-100
    print(abs(a))
    b = 0.395214
    print(round(b,2))#四舍五入保留两位小数
    # c = decimal.Decimal(b)
    d = decimal.Decimal(b).quantize(decimal.Decimal('0.00'))#四舍五入保留两位小数#精度更高
    print(d)
