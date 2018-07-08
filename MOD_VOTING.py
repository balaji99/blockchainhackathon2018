import FILE_FUNCTIONS

class PEER_VOTING:
	
	def __init__(self):
		peerlist_return_0=[]
		peerlist_return_1=[]
		winner_ans=None
		dishonest_node_list=[]
		peerlist=[]

	def identify_dishonest_nodes(self):
		if len(peerlist_return_0)<len(peerlist_return_1):
			winner_ans=1
			dishonest_node_list=copy.deepcopy(peerlist_return_0)
		else:
			winner_ans=0
			dishonest_node_list=copy.deepcopy(peerlist_return_1)

	def match_id(self,DOCID,peer):
		return 1

	def match_hash(self,DOCID,hash):
		return 1

	def is_DocID_present(self,DOCID):
		read_from_file("peerlist.txt",peerlist)
		for peer in peerlist:
			match_id_val=match_id(DOCID,peer)
			if match_id_val==0:
				peerlist_return_0.append(peer)
			elif match_id_val==1:
				peerlist_return_1.append(peer)

	def match_hashes_of_all_peers(self,DOCID):
		read_from_file("peerlist.txt",peerlist)
		match_hash_val=match_hash(DOCID,hash)
		for peer in peerlist:
			if match_hash_val==0:
				peerlist_return_0.append(peer)
			elif match_hash_val==1:
				peerlist_return_0.append(peer)
