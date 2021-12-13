from hashlib import md5, sha256
from Cryptodome.Cipher import AES

ciphertext = bytearray([152, 52, 210, 108, 209, 182, 69, 150, 153, 40, 64, 133, 135, 200, 181, 146, 187, 125, 217, 241, 62, 251, 72, 128, 232, 134, 143, 221, 236, 15, 120, 21, 213, 43, 99, 72, 163, 243, 21, 217, 41, 81, 246, 174, 229, 49, 10, 200, 70, 138, 103, 174, 160, 80, 66, 99, 250, 166, 73, 217, 220, 94, 146, 153, 150, 43, 120, 46, 150, 203, 20, 198, 211, 89, 35, 134, 89, 132, 190, 205, 141, 237, 201, 119, 178, 47, 211, 182, 156, 56, 17, 111, 146, 167, 228, 133, 51, 187, 48, 213, 206, 208, 254, 71, 205, 76, 36, 119, 32, 204, 50, 217, 167, 42, 224, 80, 91, 102, 225, 152, 14, 94, 73, 60, 145, 152, 240, 188, 182, 190, 182, 166, 98, 5, 234, 116, 229, 27, 90, 255, 109, 15, 219, 83, 34, 15, 22, 147, 170, 234, 184, 109, 28, 1, 3, 178, 98, 31, 49, 250, 163, 196, 139, 204, 177, 95, 239, 172, 138, 50, 189, 238, 57, 177, 110, 206])
text = b'Sleeperio Sleeperio Disappeario Instanterio!'
iv = md5(text).digest()
key = sha256(text).digest()

cipher = AES.new(key, AES.MODE_CBC, iv)
flag = cipher.decrypt(ciphertext)
print(flag)
# b'Our seven dwarves have dropped the final \nSleeperio snapshot on our CTF web portal!\n\nMeanwhile, take this:\n\ncorctf{4l1c3_15_1n_d33p_tr0ubl3_b3c4us3_1_d1d_n0t_s4v3_h3r!!:c}\x05\x05\x05\x05\x05'