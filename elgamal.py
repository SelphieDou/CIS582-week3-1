import random

from params import p
from params import g

def keygen():
	sk = random.randint(1, (p-1)/2)
	pk = pow(g, sk, p)
	return pk,sk

def encrypt(pk,m):
	r = random.randint(1, (p-1)/2)
	c1 = pow(g, r, p)
	c2 = (pow(pk, r, p) * (m % p)) % p
	return [c1,c2]

def decrypt(sk,c):
	int_list = list(map(int, c))
	m = ((int_list[1] % p) * pow(int_list[0], -sk, p)) % p
	return m

