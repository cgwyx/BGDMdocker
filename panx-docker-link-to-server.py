import os,sys
species = sys.argv[1]
def link_data_to_server():
	"""
	Sending json files and alignment to server for data visualization
	"""
	os.system('rsync -avz ./data/%s/meta-dict-%s.js /pan-genome-visualization/public/javascripts '%(species,species))
	os.system('rsync -avz ./data/%s/vis/ /pan-genome-visualization/public/dataset/%s/ '%(species,species))
link_data_to_server()