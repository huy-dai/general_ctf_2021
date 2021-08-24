from Crypto.Util.number import getPrime, long_to_bytes
from pwn import *
import random, binascii
import os

os.chdir("./cor_ctf/Crypto/supercomputer/task")

flag = open('flag.txt').read()

def v(p, k):
	ans = 0
	while k % p == 0:
		k /= p
		ans += 1
	return ans

#p, q, r = getPrime(2048), getPrime(2048), getPrime(2048)
line1 = "20936670545375210972091706288423179494163425035286134775773514440843943493090886819895346572945288304582498268271507942037581752184819846906869395551921930704321251130746547888224652316226957634541702883599286787839982090615950687496752999645558331533314682453610929822041558882012483238149288762974740347582024050756443700107245858419316423473568526347559377124536218894368962796664914408327949348396038507355935608178392088898784474582354438590711083089253977971653913217304360725716982473871023235180637867588860233011122300656470435644430602412710493441965130162664981423496370539240693045312454250776393871037539 19872523115298089612152987731023453644084277408261276810219001288407280019889227914287760742936580023163800626696116882213533508813201232707621762739857924392306902336092739272758773377952936022982446120177174082641600741522817135305633293579042208014735900229922142564590095968054337719254632703676737069746032384348392244892496672044899073391936273280270753785076044108870166304800552404013519058026991588856235381264192387525832530187004466616791531223421070547342377071358044704265893255021275811622959301157507095984825182110574434699593886509171425701861331576642311553357835312334349976576969220483604368671153 18342695102288954165224207958150786487860883752676419020596228714991017967256173183699487408637445601341687447489432163178271335469203559084363600703497940503946684342504933131623546315643648637992201226732630680112575643707020017139390225257319697353426087369722671485915571962910153169877358046375850132351117527591675467417925944135644417622440847857598273517926844822766083086147088819776687612745404553608100705862181700054385028096749375873889019995159762301115707945396140178370414857973922007665218670792403129624089144668480280115489465764431016721028424152163659378120333071194425845370101841510224643446231"
arr = [int(entry) for entry in line1.split(" ")]

p, q, r = arr #Destructuring
print("p, q, r:",p, q, r)

print(v(p,r))
print(p>r)
'''
n = pow(p, q) * r
print("N:",n)

a1 = random.randint(0, n)
a2 = n - a1
assert a1 % p != 0 and a2 % p != 0

t = pow(a1, n) + pow(a2, n)
print(binascii.hexlify(xor(flag, long_to_bytes(v(p, t)))))
'''
enc = b'6255a505b969be8175a5c578fd6e856ecd85faa1a22fdf38d2d11851211676fd3047ed12c4027e66ed2173495877180e3d49a387b74701fbbbdce00a2248c7812b157626c95e7cf5727ee90cc9a6a98d84ee50f106b11245d65b87a27bbd7ab94b0d82eeb6e49e81249ae880c150ff87d8da701e9d317932fa2b27b64eb894a112d942d7d269478a6c120be885f3fbd065c38e70498c2f294b47bb08da09fb63c05070248079fe4311c9821dd8d3a08b15f13cdb0b7a8d406790c4796e0218851b496a11bf1ad7575be6d9999d5f1c73080d724c66a116f865ffcd3048be5d59dae55a4a063629d30429765733521702ec36d3f111b015934d15d620ad0e35ee56'
byte_enc = binascii.unhexlify(enc)

print(xor(byte_enc,long_to_bytes(2*q)))