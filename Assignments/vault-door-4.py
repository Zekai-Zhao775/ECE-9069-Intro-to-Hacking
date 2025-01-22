my_bytes = [
    106, 85, 53, 116, 95, 52, 95, 98,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o70, 0o146
]

password = []

for byte in my_bytes:
    password.append(chr(byte))

password.append("4a6cbf3b")

print(''.join(password))