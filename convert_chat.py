#讀取、存取檔案並試印在cmd上
def read_file(filename):
	with open(filename, 'r', encoding = 'utf-8-sig') as f:	#可惜限制名字跟開始說話者
		choose = False	#True 代表 Allen, False 代表 Tom
		A = []			#Allen的說話清單
		a = []			#Allen的說話清單是二微陣列
		T = []			#Tom的說話清單
		t = []			#Tom的說話清單是二微陣列
		ca = False		#False是還沒遇到Allen

		for line in f:								#掃描input檔
			if 'Allen' in line and ca == False:		#第一次遇到Allen
				choose = True
				ca = True
				continue
			elif 'Allen' in line and ca == True:	#如果掃描到了Allen這個名字就把choose代表改成Allen
				choose = True
				T.append(t)							#並且存入目前所有Tom單次講過的話到T[]
				t = []
			elif 'Tom' in line:						#如果掃描到了Tom這個名字就把choose代表改成Tom
				choose = False
				A.append(a)							#並且存入目前所有Allen單次講過的話到A[]
				a = []
			elif choose == True:					#如果choose代表Allen: 就把Allen說話內容記錄下來並印出來
				print('Allen:', line)
				a.append(line.strip())
			elif choose == False:					#如果choose代表Tom: 就把Tom說話內容記錄下來
				print('Tom:', line)
				t.append(line.strip())

		if len(a) != 0:								#存入結尾最後講話的人的對話(不管是Allen或是Tom都可以)
			A.append(a)
			a = []
		if len(t) != 0:
			T.append(t)
			t = []
		return A, T

#建立檔案並改寫進txt檔
def write_file(A, T):
	with open('output.txt', 'w', encoding = 'utf-8-sig') as f:
		if len(A) > len(T):
			for i in range(len(T)):
				for a in A[i]:
					f.write('Allen: ' + a + '\n')
				for t in T[i]:
					f.write('Tom: ' + t + '\n')
			for a in A[len(A)-1]:
				f.write('Allen: ' + a + '\n')

		elif len(A) < len(T):
			for i in range(len(A)):
				for a in A[i]:
					f.write('Allen: ' + a + '\n')
				for t in T[i]:
					f. write('Tom' + t + '\n')
			for t in T[len(T)-1]:
				f.write('Tom: ' + t + '\n')
		else:
			for i in range(len(A)):
				for a in A[i]:
					f.write('Allen: ' + a + '\n')
				for t in T[i]:
					f.write('Tom: ' + t + '\n')

#主程式
def main():
	filename = input('請輸入你要讀取的聊天紀錄: ')
	A, T = read_file(filename)
	write_file(A, T)



main()