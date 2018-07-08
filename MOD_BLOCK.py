import FILE_FUNCTIONS
import hashlib
import binascii

class BLOCK:
	def __init__(self):
		DOCID=""
		DOCHash=""
		PrevBlockHash=""

	def set_dochash(self,filename) :
		sha256_hash = hashlib.sha256()
		with open(filename,"rb") as f:
		    # Read and update hash string value in blocks of 4K
		    for byte_block in iter(lambda: f.read(4096),b""):
		        sha256_hash.update(byte_block)
		    h1=sha256_hash.hexdigest()
		DOCHash=str(h1)

	def set_docid(self):
		dt=datetime.now()
		year=dt.strftime("%Y")
		month=dt.strftime("%m")
		day=dt.strftime("%d")
		hour=dt.strftime("%H")
		minute=dt.strftime("%M")
		second=dt.strftime("%S")
		microsecnd=dt.strftime("%f")
		timestamp=year+month+day+hour+minute+second+microsecnd
		DOCID=doc_timestamp()+doc_ip()

	def set_prevblockhash(self):
		blockchain=[]
		read_from_file("blockchain.txt",blockchain)
		PrevBlockHash=blockchain[-1]

	def block_to_binary(block):
		# Return the binary data represented by the hexadecimal string
		# Input must contain an even number of hexadecimal digits
		out = binascii.unhexlify(block['DOCID'] + block['DOCHash'] + block['PrevBlockHash'])
		return out


	def load_blockchain():
		blockchain = []
		with open(BLOCKCHAIN_FILE, 'r') as f_bc:
			for line in f_bc.read().split():
				block = {}
				block['DOCID'], block['DOCHash'], block['PrevBlockHash'] = line.split(',')
				blockchain.append(block)
		return blockchain


	def retr_block(DOCID):
		''' Search through the blockchain for the 
		specified DocID and return its DOCHash'''
		blockchain=load_blockchain()
		prevblock = None
		for curblock in blockchain:
			print(curblock['DOCID'])
			if prevblock and curblock['PrevBlockHash'] != hashfn(block_to_binary(prevblock)):
				print('BLOCKCHAIN_TAMPERED')
				return (BLOCKCHAIN_TAMPERED, None)
			if curblock['DOCID'] == DOCID:
				print('RETRIEVAL SUCCESS')
				return (SUCCESS, curblock['DOCHash'])
			prevblock = curblock
		print('DOC_NOT_PRESENT')
		return (DOC_NOT_PRESENT, None)

	def add_block(DOCID, document,Username):
		''' Adds a new block to the blockchain'''
		blacklist=read_from_file("blacklist.txt")
		if Username in blacklist:
			print("USER ALREADY BLACKLISTED")
			return 1
		blockchain=load_blockchain()
		for block in blockchain:	# checks for duplicate DOCID
			if block['DOCID'] == DOCID:
				print('DUP_DOCID')
				return DUP_DOCID
		new_block = {
			'DOCID' : DOCID,
			'DOCHash' : hashfn(doc_to_binary(document))
		}
		if blockchain:
			new_block['PrevBlockHash'] = hashfn(block_to_binary(blockchain[-1]))
		else:
			new_block['PrevBlockHash'] = hashfn(b'0') # PrevBlockHash is a fixed value for genesis block
		blockchain.append(new_block)
		f_bc.write(new_block['DOCID']+','+new_block['DOCHash']+','+new_block['PrevBlockHash']+'\n')
		print('ADDING SUCCESS')
		return SUCCESS