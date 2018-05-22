import os
import sys
filename=sys.argv[1]
os.system("python /home/manoj/system/code_cleaner/remove_quotation.py "+ filename)
os.system("python /home/manoj/system/code_cleaner/remove_single_q.py "+filename+"_wq")
os.system("python /home/manoj/system/code_cleaner/remove_mlc.py "+filename+"_wq_sq \'/*\' \'*/\'")
os.system("python /home/manoj/system/code_cleaner/remove_slc.py "+filename+"_wq_sq_wmlc \'//\'")
os.system("python /home/manoj/system/code_cleaner/bracket_checker.py "+filename+"_wq_sq_wmlc_wslc '{'")
os.system("python /home/manoj/system/code_cleaner/bracket_checker.py "+filename+"_wq_sq_wmlc_wslc_bc '}'")
os.system("python /home/manoj/system/code_cleaner/remove_el.py "+filename+"_wq_sq_wmlc_wslc_bc_bc")
os.system("mv "+filename+"_wq_sq_wmlc_wslc_bc_bc_wel "+filename+"_cr")
os.system("rm "+filename+"*c")
os.system("rm "+filename+"*q")
