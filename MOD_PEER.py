import MOD_VOTING

class MOD_PEER:

    def __init__(self):

    def action_against_dishonest_nodes(self):
    	dishonest_nodes=MOD_VOTING.identify_dishonest_nodes()
    	new_watchlist=[]
    	read_from_file("watchlist",new_watchlist)
    	new_peerlist=[]
    	read_from_file("peerlist.txt",new_peerlist)
    	for node in dishonest_nodes:
    		if search_in_file("watchlist.txt",node):
    			append_to_file("blacklist.txt",node)
    			new_watchlist.remove(node)
    			new_peerlist.remove(node)
    		else:
    			new_watchlist.append(node)
    	write_to_file("watchlist.txt",new_watchlist)
    	write_to_file("peerlist.txt",new_peerlist)

    def match_hashes_with_other_nodes(self):
    	MOD_VOTING.match_hashes_of_all_peers()

    def add_new_user(self):
        
