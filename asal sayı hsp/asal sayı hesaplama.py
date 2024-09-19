#asal sayı hesaplama
sayi = int(input('Sayı giriniz: '))

if sayi <= 1:
    print('Girdiğiniz sayı asal değildir.')
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            print('Girdiğiniz sayı asal değildir.')
            break
    else:
        print('Girdiğiniz sayı asaldır.')
