total_vic = 0
donation = float(input())

while donation != -1.0:
    total_vic+=donation
    donation = float(input())

total_price = total_vic * 2.50
print(f'VC$ {total_vic:.2f}') 
print(f'R$ {total_price:.2f}')