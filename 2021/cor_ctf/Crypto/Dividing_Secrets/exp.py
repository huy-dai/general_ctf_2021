from pwn import *
from Crypto.Util.number import long_to_bytes

res = 5207851285831991069018664616693415824195562260751582516097806772363284738507980478829791747964096025668757404599258689372930479386523996608148861164794492

print(long_to_bytes(res))
print(long_to_bytes(res+2))
print(long_to_bytes(res+1))

r = remote('crypto.be.ax',6000)

res = r.recvuntil(b">").decode('utf-8')
print(res)


#Chose random p for hi
i = 0
hi = 12123011818658592223829585444463227444387063694309686111263422100048399811440660891168952304033795717311157503302903808212679523140543340266855141269464379
low = 1

#Last trial
hi = 5207851285831991069018664616693415824195562260751582516097806772363284738507980478829791747964096025668757404599258689372930479386523996608148861164794494
low = 5207851285831991069018664616693415824195562260751582516097806772363284738507980478829791747964096025668757404599258689372930479386523996608148861164794492

while hi - low != 1:
    print("Trial:",i)
    print("High:",hi)
    print("Low:",low)
    avg = (hi + low) // 2
    r.sendline(str(avg).encode('utf-8'))
    res = r.recvline().decode('utf-8')
    if i == 0:
        res = int(res)
    elif "no more tries" in res:
        #Close current r and make new connection
        r.close()
        r = remote('crypto.be.ax',6000)
        res = r.recvuntil(b">").decode('utf-8')
        i = 0
        continue
    else:
        res = int(res[res.index("> ")+2:])
    print("Result:",res)
    print(type(res))
    if res == 1: #avg >= flag
        hi = avg
    else: #avg < flag
        low = avg
    i+=1


r.close()
