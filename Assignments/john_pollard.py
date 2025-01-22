from sympy import factorint, mod_inverse

# Subject Public Key Info:
#             Public Key Algorithm: rsaEncryption
#                 Public-Key: (53 bit)
#                 Modulus: 4966306421059967 (0x11a4d45212b17f)
#                 Exponent: 65537 (0x10001)

# public key
n = 4966306421059967
e = 65537

# Factorize n to get p and q
factors = factorint(n)
p, q = factors.keys()

# phi(n)
phi_n = (p - 1) * (q - 1)

# private key (d)
d = mod_inverse(e, phi_n)

print("p = ", p)
print("q = ", q)
print("phi(n):", phi_n)
print("Private key (d):", d)