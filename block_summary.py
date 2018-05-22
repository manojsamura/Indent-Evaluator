import sys
import math
import os

def num_spaces(k):
	if(k=='\t'):
		return 8
	else:
		return 1

def check_extra_line(a):
	semi=0
	for i in a:
		if(i==';'):
			semi+=1
	_for=0
	for i in range(len(a)):
		if(a[i]=='f'):
			if(i<len(a)-2):
				if(a[i+1]=='o' and a[i+2]=='r'):
					_for+=1
	if('for' in a):
		semi-=2*_for
	return semi-1

def isswitch(a):
	if('switch' in a):
		a=a.strip(' ')
		a=a.strip('\t')
		a=a.strip(' ')
		a_list=a.split(' ')
		flag=0
		for i in a_list:
			i=i.strip('\t')
			if(flag==1 and len(i)>0):
				if(i[0]=='('):
					return True
				else:
					return False
			elif(flag==0):
				if('switch' in i):
					if( i[0]=='s' and i[1]=='w' and i[2]=='i' and i[3]=='t' and i[4]=='c' and i[5]=='h'):
						if(len(i)>6):
							if(i[6]=='('):
								return True
							elif(i[6]=='\t'):
								for k in range(7,len(i)):
									if(i[k]=='('):
										return True
									elif(i[k]!='\t'):
										return False
							else:
								return False
						else:
							flag=1
		return False
	else:
		return False


def isif(a):
	if('if' in a):
		a=a.strip(' ')
		a=a.strip('\t')
		a=a.strip(' ')
		a_list=a.split(' ')
		flag=0
		for i in a_list:
			i=i.strip('\t')
			if(flag==1 and len(i)>0):
				if(i[0]=='('):
					return True
				else:
					return False
			elif(flag==0):
				if('if' in i):
					if( i[0]=='i' and i[1]=='f'):
						if(len(i)>2):
							if(i[2]=='('):
								return True
							elif(i[2]=='\t'):
								for k in range(3,len(i)):
									if(i[k]=='('):
										return True
									elif(i[k]!='\t'):
										return False
							else:
								return False
						else:
							flag=1
		return False
	else:
		return False

def iswhile(a):
	if('while' in a):
		a=a.strip(' ')
		a=a.strip('\t')
		a=a.strip(' ')
		a_list=a.split(' ')
		flag=0
		for i in a_list:
			i=i.strip('\t')
			if(flag==1 and len(i)>0):
				if(i[0]=='('):
					return True
				else:
					return False
			elif(flag==0):
				if('while' in i):
					if( i[0]=='w' and i[1]=='h' and i[2]=='i' and i[3]=='l' and i[4]=='e'):
						if(len(i)>5):
							if(i[5]=='('):
								return True
							elif(i[5]=='\t'):
								for k in range(6,len(i)):
									if(i[k]=='('):
										return True
									elif(i[k]!='\t'):
										return False
							else:
								return False
						else:
							flag=1
		return False
	else:
		return False

def isfor(a):
	if('for' in a):
		a=a.strip(' ')
		a=a.strip('\t')
		a=a.strip(' ')
		a_list=a.split(' ')
		flag=0
		for i in a_list:
			i=i.strip('\t')
			if(flag==1 and len(i)>0):
				if(i[0]=='('):
					return True
				else:
					return False
			elif(flag==0):
				if('for' in i):
					if( i[0]=='f' and i[1]=='o' and i[2]=='r'):
						if(len(i)>3):
							if(i[3]=='('):
								return True
							elif(i[3]=='\t'):
								for k in range(4,len(i)):
									if(i[k]=='('):
										return True
									elif(i[k]!='\t'):
										return False
							else:
								return False
						else:
							flag=1
		return False
	else:
		return False


def iselse(a):
	if('else' in a):
		a=a.strip(' ')
		a=a.strip('\t')
		a=a.strip(' ')
		a_list=a.split(' ')
		flag=0
		for i in a_list:
			i=i.strip('\t')
			if(flag==1 and len(i)>0):
				if(i[0]=='('):
					return True
				else:
					return False
			elif(flag==0):
				if('else' in i):
					if( i[0]=='e' and i[1]=='l' and i[2]=='s' and i[3]=='e' ):
						if(len(i)>4):
							if(i[4]=='('):
								return True
							elif(i[4]=='\t'):
								for k in range(5,len(i)):
									if(i[k]=='('):
										return True
									elif(i[k]!='\t'):
										return False
							else:
								return False
						else:
							flag=1
		return False
	else:
		return False


def iscase(a):
	if('case' in a):
		a=a.strip(' ')
		a=a.strip('\t')
		a=a.strip(' ')
		a_list=a.split(' ')
		flag=0
		for i in a_list:
			i=i.strip('\t')
			if(flag==1 and len(i)>0):
				if(i[0]!=' ' and i[0]!='\t'):
					if(i[0]=='\n'):
						return False
					else:
						return True
			elif(flag==0):
				if('case' in i):
					if( i[0]=='c' and i[1]=='a' and i[2]=='s' and i[3]=='e' ):
						if(len(i)>4):
							if(i[4]=='\n'):
								return False
							elif(i[4]=='\t'):
								for k in range(5,len(i)):
									if(i[k]=='\n'):
										return False
									elif(i[k]!='\t'):
										return True 
							else:
								return True
						else:
							flag=1
		return False
	else:
		return False


def isdefault(a):
	if('default' in a):
		a=a.strip(' ')
		a=a.strip('\t')
		a=a.strip(' ')
		a_list=a.split(' ')
		flag=0
		for i in a_list:
			i=i.strip('\t')
			if(flag==1 and len(i)>0):
				if(i[0]!=' ' and i[0]!='\t'):
					if(i[0]=='\n'):
						return False
					else:
						return True
			elif(flag==0):
				if('default' in i):
					if( i[0]=='d' and i[1]=='e' and i[2]=='f' and i[3]=='a'  and i[4]=='u' and i[5]=='l' and i[6]=='t'):
						if(len(i)>7):
							if(i[7]=='\n'):
								return False
							elif(i[7]=='\t'):
								for k in range(8,len(i)):
									if(i[k]=='\n'):
										return False
									elif(i[k]!='\t'):
										return True 
							else:
								return True
						else:
							flag=1
		return False
	else:
		return False


#---------------------------------------------------block seperation -------------------------------------


filename=sys.argv[1]
blocks=[[]]
top=0
switch_flag=0
switch_internal=-1
fp=open(filename,'r')
string=fp.readline()
statements=blocks[top]
prevblock=[]
prevblock.append(-1)
bflag=0
prev_statement=''
while(string):
	if(isswitch(string)):
		switch_flag+=1
	if('{' in string or '}' in string):
		if('}' in string):
			pre=""
			seq=""
			flag_check=1
			check_flag=0
			for i in string:
				if(i=='}'):
					flag_check=0
					seq='\n'
				if(i!=' ' and i!='\t'and flag_check==1):
					flag_check=-1
				if(flag_check==1):
					if(i=='\t'):
						seq+='\t'
					else:	
						seq+=' '
					pre+=i
				if(flag_check<0):
					pre+=i
					seq=""
					check_flag=1
				else:
					seq+=i
			if(check_flag==1):
				statements.append(pre)
			if(check_flag==0):
				top=prevblock[top]
				statements=blocks[top]
				statements.append(string)
			else:	
				top=prevblock[top]
				if(switch_flag>0):
					if(switch_internal==0):
						if(bflag==1):
							top=prevblock[top]
						switch_flag=0
						switch_internal=-1
						top=prevblock[top]
					if(switch_internal%2==0):
						switch_flag-=2
						if(switch_internal==(switch_flag/2)-1):
							switch_flag-=2
							blfag=1
					if(switch_internal>0):
							switch_internal-=1
							b_flag=1
				statements=blocks[top]
				if(check_flag==1):
					statements.append(seq)
		if('{' in string):
			bflag=0
			if(switch_flag>0):
				switch_internal+=1
			s=blocks[top]
			if(s!=[]):
				if(string!=s[len(blocks[top])-1]):
					statements.append(string)
			else:
				statements.append(string)
			blocks.append([])
			prevblock.append(top)
			top=len(blocks)-1
			statements=blocks[top]
	elif(iscase(string) or isdefault(string)):
		bflag=0
		if(switch_flag%2==1):
			switch_flag+=1
			if(switch_internal==-1):
				switch_internal=0
		elif(switch_flag%2==0):
			top=prevblock[top]
			statements=blocks[top]
                flag=0
                a=""
                a1=""
                for i in string:
                        if(flag==0):
                                a+=i
                                if(i=='\t'):
                                        a1+='\t'
                                else:

                                        a1+=" "
                        if(flag==1):
                                a+='\n'
                                flag=2
                                statements.append(a)
                                blocks.append([])
                                prevblock.append(top)
                                top=len(blocks)-1
                                statements=blocks[top]
                        if(flag==2):
                                if(i!='\t' and i!='\n' and i!=' '):
                                        flag=3
                                a1+=i
                        if(flag==3):
                                a1+=i
                        if(i==':'):
                                flag=1

                if(flag==3):
                        statements.append(a1)

	else:
		bflag=0
		if(len(statements)==0):
			statements.append(string)
		else:
			check_if_else=prev_statement.strip()
			if(isfor(check_if_else) or iselse(check_if_else) or isif(check_if_else) or iswhile(check_if_else) ):
				blocks.append([])
				prevblock.append(top)
				top=len(blocks)-1
				statements=blocks[top]
				statements.append(string)
				top=prevblock[top]
				statements=blocks[top]
			else:
				statements.append(string)
	prev_statement=string
	string=fp.readline()
#	for i in blocks:
#		print("--------------------------------------------------------------------")
#		for j in i:
#			print(j)
#		print("--------------------------------------------------------------------")
#	print(string)
#	input()
#	os.system("clear")
fp.close()
# ---------------- block seperation ------------------------------------------
# ---------------- done ------------------------------------------------------

block_space=[]
block_error_dist=[]
percent_correctness=[]
len_block=[]
prevspace=-1
wp=open(filename+"_indent_feedback",'w')
wp1=open(filename+'_ic','w')
for i in range(len(blocks)):
	e_flag=0
	eb_flag=0
	if(prevblock[i]==-1):
		prevspace=-2
	else:
		prevspace=block_space[prevblock[i]]
	start=[]
	occurences=[]
	lines=[]
	if(blocks[i]==[]):
		eb_flag=1
		block_space.append(0)
	if(eb_flag==0):
		for j in blocks[i]:
			check=check_extra_line(j)
			if(check>0):
				if(-1 in start):
					for q1 in range(len(start)):
						if(start[q1]==-1):
							occurences[q1]+=check
				else:
					start.append(-1)
					occurences.append(check)
				lines.append([])
				lines[len(lines)-1].append(j)
			spaces=0
			for k in j:
				if(k!=' ' and k!='\n' and k!='\t'):
					if(spaces not in start):
						start.append(spaces)
						occurences.append(1)
						lines.append([])
						lines[len(lines)-1].append(j)
					else:
						for j1 in range(len(start)):
							if(start[j1]==spaces):
								occurences[j1]+=1
								lines[j1].append(j)
					break
				else:
					spaces+=num_spaces(k)
		max_v=0
		max_v_i=0
		for i1 in range(len(start)):
			if(start[i1]<prevspace+1 or start[i1]>prevspace+8):
				start[i1]=-1
		for i1 in range(len(occurences)):
			if(occurences[i1]>max_v and start[i1]>=0):
				max_v=occurences[i1]
				max_v_i=i1
		ideal=start[max_v_i]
		if(start[max_v_i]<0):
			max_v=prevspace+2
			ideal=max_v
		if(start[max_v_i]==-1):
			block_space.append(prevspace+2)
		else:
			block_space.append(start[max_v_i])
		error=0
		dist=0
		for i1 in range(len(start)):
			dist+=((ideal-start[i1])*(ideal-start[i1])*occurences[i1])
		dist=dist/5
		error=math.sqrt(dist)
		percent=100/(error+1)
		percent_correctness.append(percent)
		len_block.append(len(blocks[i]))
		if(start[max_v_i]==-1):
			occurences[max_v_i]=0
			e_flag=1
		if(percent<100):
			wp.write("block : \n\n")
			for k in blocks[i]:
				wp.write(k)
			wp.write("\nThe ideal start point for this block is : "+str(ideal)+"\n")
			wp.write("The total number of lines in the block : "+str(len(blocks[i]))+"\n")
			wp.write("The number of lines that are at ideal starting point is : "+str(occurences[max_v_i])+"\n")
			wp.write("The number of lines that are not at the ideal starting points is : "+str((len(blocks[i])-occurences[max_v_i]))+"\n")
			wp.write("The lines that are not properly indented : \n\n")
			if(e_flag==1):
				max_v_i=prevspace+2
			for q in range(len(lines)):
				if(q!=max_v_i):
					for w in lines[q]:
						wp.write(w)
			wp.write("\n\n")
			wp.write("block percent : "+str(percent)+"\n")
		block_error_dist.append(percent)
	else:
		percent_correctness.append(0)
		len_block.append(1)
wp.close()
# -------------------------------- block summary ------------------------
# ------------------------------------- done ----------------------------

total=0
total_length=0
for i in range(len(percent_correctness)):
	total+=(100-percent_correctness[i])*(100-percent_correctness[i])*len_block[i]
	total_length+=len_block[i]
total=math.sqrt(total/(10000*total_length))
total=total-1
total=total*-100
wp1.write(str(total))
wp1.close()
