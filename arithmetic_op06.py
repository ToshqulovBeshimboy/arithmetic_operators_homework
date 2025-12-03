# n  deb nomlangan o'zgaruvchi yarating va besh  xonali turli xil raqamni belgilang
n=46318
# n sonining raqamlar yig'indisni toping va uni sum deb nomlangan o'zgaruvchiga belgilang.
sum=n%10+n%100//10+n//100%10+n//1000%10+n//10000
# n sonining raqamlar ko'paymasini toping va uni k deb nomlangan o'zgaruvchiga belgilang.
k=(n%10)*(n%100//10)*(n//100%10)*(n//1000%10)*(n//10000)
# total deb nomlangan o'zgaruvchi yarating va k ning qiymatini sum qiymatiga butunli bo'ling. 
m=k//sum
# total o'zgaruvchisining natijasini chiqaring.
print(m)