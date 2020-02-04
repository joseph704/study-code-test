def push(n):
	list.append(n)
def pop():
	try:
		print(list.pop())
	except:
		print(-1)
def size():
	return len(list)
def empty():
	if size()==0:
		print(1)
	else:
		print(0)
def top():
	try:
		print(list[-1])
	except:
		print(-1)

case_num = int(input())
list = []
for i in range(case_num):
	cmd=input().split()
	
	if cmd[0]=="push":
		push(cmd[1])
	elif cmd[0]=="pop":
		pop()
	elif cmd[0]=="size":
		print(size())
	elif cmd[0]=="top":
		top()
	elif cmd[0]=="empty":
		empty()