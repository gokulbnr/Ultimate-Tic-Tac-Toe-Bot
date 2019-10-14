import sys
import random
import signal
import time
import copy
import random
import time
class Player46:
	def __init__(self):
		self.player='-'
		self.opponant='-'
		self.iniTime=0
		pass

	def move(self, board, old_move, flag):
		max_depth = 4
		copy_board = copy.deepcopy(board);
		cells = copy_board.find_valid_move_cells(old_move)
		self.player=flag
		if self.player == 'x':
			self.opponant = 'o'
		else:
			self.opponant = 'x'
		max_depth=0
		temp_utility = cells[0]
		self.iniTime = time.time()
		for depth in [1,2,3,4,5,6,7]:
			temp_utility = self.minimax(copy_board,(-1,-1),old_move,0,depth,flag,-10000000,10000000)
			if temp_utility[0] != 'FAIL':
				utility = temp_utility
				max_depth=depth
			if temp_utility[0] == 'FAIL':
				break;
		return (utility[1],utility[2])

	def minimax(self,copy_board,old_move,new_cell,cur_depth,max_depth,flag,alpha,beta):

		curTime = time.time()
		if curTime-self.iniTime >= 14.0:
		 	return ('FAIL',-1,-1)

		inf = 1000000000
		if flag == 'x':
			opponant = 'o'
		else:
			opponant = 'x'

		if(old_move!=(-1,-1)):
			copy_board.update(old_move,new_cell,opponant)
		next_cells = copy_board.find_valid_move_cells(new_cell)

		if cur_depth >= max_depth: #Assigning Heuristic Value, based on an evaluating function.
			 return self.evaluate(copy_board)

		status = copy_board.find_terminal_state()
		if status[1] == 'WON' or status[1] == 'DRAW': #Terminal state, when the game has ended.
			if status[1] == 'WON' and flag == self.player:
				return (100000000,-1,-1)
			elif status[1] == 'WON' and flag == self.opponant:
				return (-100000000,-1,-1)
			elif status[1] == 'DRAW':
				return (0,-1,-1)

		if len(next_cells)==0:
			return (0,-1,-1)

		mstate =0
		if cur_depth%2 ==0: #Maximizing player
			mstate = (-1)*inf
			for cell in next_cells:
				prevBoard = copy_board.board_status[cell[0]][cell[1]]
				prevBlock = copy_board.block_status[int(cell[0]/4)][int(cell[1]/4)]
				utility = self.minimax(copy_board,new_cell,cell,(cur_depth+1),max_depth,opponant,alpha,beta)
				copy_board.board_status[cell[0]][cell[1]]=prevBoard
				copy_board.block_status[int(cell[0]/4)][int(cell[1]/4)]=prevBlock
				if utility[0] == 'FAIL':
					return ('FAIL',-1,-1)
				if utility[0] > mstate:
					best_cell = cell
					mstate = utility[0]
				alpha = max(alpha,mstate)
				if beta <= alpha:
					break

		else: #Minimising player
			mstate = inf
			for cell in next_cells:
				prevBoard = copy_board.board_status[cell[0]][cell[1]]
				prevBlock = copy_board.block_status[int(cell[0]/4)][int(cell[1]/4)]
				utility = self.minimax(copy_board,new_cell,cell,(cur_depth+1),max_depth,opponant,alpha,beta)
				copy_board.board_status[cell[0]][cell[1]]=prevBoard
				copy_board.block_status[int(cell[0]/4)][int(cell[1]/4)]=prevBlock
				if utility[0] == 'FAIL':
					return ('FAIL',-1,-1)
				if utility[0] < mstate:
					best_cell = cell
					mstate = utility[0]
				beta=min(beta,mstate)
				if beta <= alpha:
					break
		return (mstate,best_cell[0],best_cell[1])



	def evaluate(self,board):
		utility = 0
		for i in range(4):
			for j in range(4):
				if(board.block_status[i][j]==self.player):
					utility+=100
				elif(board.block_status[i][j]==self.opponant):
					utility-=100
				utility+=self.partial(i,j,board.board_status,5,4)
		utility+=self.partial(0,0,board.block_status,10,4)
		return (utility,-1,-1)


	def partial(self,i,j,board,addfac,iafac):
		URet = 0
		for IT in range(4):
			flag=0
			utility=1.0
			for it in range(4):
				if(board[i*4+it][j*4+IT]!=self.player  and flag==1):
					if(board[i*4+it][j*4+IT]==self.opponant):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+it][j*4+IT]==self.player  and flag==0):
					flag=1
				elif(board[i*4+it][j*4+IT]==self.player and flag==1):
					utility*=addfac
					#addfac-=1
			URet+=utility
			flag=0
			utility=1.0
			for it in range(4):
				if(board[i*4+IT][j*4+it]!=self.player  and flag==1):
					if(board[i*4+IT][j*4+it]==self.opponant):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+IT][j*4+it]==self.player  and flag==0):
					flag=1
				elif(board[i*4+IT][j*4+it]==self.player and flag==1):
					utility*=addfac
					#addfac-=1
			URet+=utility
			flag=0
			utility=-1.0
			for it in range(4):
				if(board[i*4+it][j*4+IT]!=self.opponant  and flag==1):
					if(board[i*4+it][j*4+IT]==self.player):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+it][j*4+IT]==self.opponant  and flag==0):
					flag=1
				elif(board[i*4+it][j*4+IT]==self.opponant and flag==1):
					utility*=addfac
			URet+=utility
			flag=0
			utility=-1.0
			for it in range(4):
				if(board[i*4+IT][j*4+it]!=self.opponant  and flag==1):
					if(board[i*4+IT][j*4+it]==self.player):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+IT][j*4+it]==self.opponant  and flag==0):
					flag=1
				elif(board[i*4+IT][j*4+it]==self.opponant and flag==1):
					utility*=addfac
			URet+=utility
			################################################################
			flag=0
			utility=1.0
			for it in range(4)[::-1]:
				if(board[i*4+it][j*4+IT]!=self.player  and flag==1):
					if(board[i*4+it][j*4+IT]==self.opponant):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+it][j*4+IT]==self.player  and flag==0):
					flag=1
				elif(board[i*4+it][j*4+IT]==self.player and flag==1):
					utility*=addfac
					#addfac-=1
			URet+=utility
			flag=0
			utility=1.0
			for it in range(4)[::-1]:
				if(board[i*4+IT][j*4+it]!=self.player  and flag==1):
					if(board[i*4+IT][j*4+it]==self.opponant):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+IT][j*4+it]==self.player  and flag==0):
					flag=1
				elif(board[i*4+IT][j*4+it]==self.player and flag==1):
					utility*=addfac
					#addfac-=1
			URet+=utility
			flag=0
			utility=-1.0
			for it in range(4)[::-1]:
				if(board[i*4+it][j*4+IT]!=self.opponant  and flag==1):
					if(board[i*4+it][j*4+IT]==self.player):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+it][j*4+IT]==self.opponant  and flag==0):
					flag=1
				elif(board[i*4+it][j*4+IT]==self.opponant and flag==1):
					utility*=addfac
			URet+=utility
			flag=0
			utility=-1.0
			for it in range(4)[::-1]:
				if(board[i*4+IT][j*4+it]!=self.opponant  and flag==1):
					if(board[i*4+IT][j*4+it]==self.player):
						utility*=-1.0/iafac
						break;
				elif(board[i*4+IT][j*4+it]==self.opponant  and flag==0):
					flag=1
				elif(board[i*4+IT][j*4+it]==self.opponant and flag==1):
					utility*=addfac
			URet+=utility
			########################################################################################################################################

		flag=0
		utility=1.0
		for it in range(4):
			if(board[i*4+it][j*4+it]!=self.player  and flag==1):
				if(board[i*4+it][j*4+it]==self.opponant):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+it]==self.player  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+it]==self.player and flag==1):
				utility*=addfac
				#addfac-=1
		URet+=utility
		flag=0
		utility=-1.0
		for it in range(4):
			if(board[i*4+it][j*4+it]!=self.opponant  and flag==1):
				if(board[i*4+it][j*4+it]==self.player):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+it]==self.opponant  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+it]==self.opponant and flag==1):
				utility*=addfac
		URet+=utility
		flag=0
		utility=1.0
		for it in range(4):
			if(board[i*4+it][j*4+3-it]!=self.player  and flag==1):
				if(board[i*4+it][j*4+3-it]==self.opponant):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+3-it]==self.player  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+3-it]==self.player and flag==1):
				utility*=addfac
				#addfac-=1
		URet+=utility
		flag=0
		utility=-1.0
		for it in range(4):
			if(board[i*4+it][j*4+3-it]!=self.opponant  and flag==1):
				if(board[i*4+it][j*4+3-it]==self.player):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+3-it]==self.opponant  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+3-it]==self.opponant and flag==1):
				utility*=addfac
		URet+=utility
		#########################################################################################
		flag=0
		utility=1.0
		for it in range(4)[::-1]:
			if(board[i*4+it][j*4+it]!=self.player  and flag==1):
				if(board[i*4+it][j*4+it]==self.opponant):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+it]==self.player  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+it]==self.player and flag==1):
				utility*=addfac
				#addfac-=1
		URet+=utility
		flag=0
		utility=-1.0
		for it in range(4)[::-1]:
			if(board[i*4+it][j*4+it]!=self.opponant  and flag==1):
				if(board[i*4+it][j*4+it]==self.player):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+it]==self.opponant  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+it]==self.opponant and flag==1):
				utility*=addfac
		URet+=utility
		flag=0
		utility=1.0
		for it in range(4)[::-1]:
			if(board[i*4+it][j*4+3-it]!=self.player  and flag==1):
				if(board[i*4+it][j*4+3-it]==self.opponant):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+3-it]==self.player  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+3-it]==self.player and flag==1):
				utility*=addfac
				#addfac-=1
		URet+=utility
		flag=0
		utility=-1.0
		for it in range(4)[::-1]:
			if(board[i*4+it][j*4+3-it]!=self.opponant  and flag==1):
				if(board[i*4+it][j*4+3-it]==self.player):
					utility*=-1.0/iafac
					break;
			elif(board[i*4+it][j*4+3-it]==self.opponant  and flag==0):
				flag=1
			elif(board[i*4+it][j*4+3-it]==self.opponant and flag==1):
				utility*=addfac
		URet+=utility
		return URet
