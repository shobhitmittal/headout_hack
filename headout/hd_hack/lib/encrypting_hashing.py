from Crypto.Cipher import AES
import base64
import hashlib

def encrypt():
	msg_text = 'test some plain text here'.rjust(32)
	secret_key = '1213456789012356' # create new & store somewhere safe
	
	cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
	encoded = base64.b64encode(cipher.encrypt(msg_text))
	print encoded.strip()
	# ...
	decoded = cipher.decrypt(base64.b64decode(encoded))
	print decoded.strip()

def hashing(user_name,user_id):
	m = hashlib.md5()
	m.update(str(user_name))
	m.update(str(user_id))
	print m.hexdigest()

if __name__ == '__main__':
	hashing('123','sds')