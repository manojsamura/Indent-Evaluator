import sys
import os
import time
for i in range(1,len(sys.argv)):
	filename=sys.argv[i]
	string="python /home/manoj/system/indent_checker/code_cleaner.py "+filename
	print("code cleaning done ...")
	os.system(string)
	time.sleep(1)
	string="python /home/manoj/system/indent_checker/block_summary.py "+filename+"_cr > "+filename+"_ic"
	os.system(string)
