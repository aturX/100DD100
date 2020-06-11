# DPoS 共识算法 简单实现

# 引入 见证者 节点
import hashlib
from random import randint

# 见证人数量 N
N = 3

class WitnessNode(object):
	def __init__(self, NodeAddress):
		self.NodeAddress = NodeAddress


def getNodeAddress():
	# 随机返回一个地址， 只做演示
	num = str(randint(0, 100))
	address = hashlib.sha256(num.encode("utf-8")).hexdigest()
	return address

class Block(object):
	def __init__(self):
		self.Votes = randint(0, 100)
		self.Timestamp = None
		self.PrevHash = None
		self.Hash = None
		self.NodeAddress = getNodeAddress()
		self.Data = None


# 当前见证人列表
WitnessList = [
Block(),
Block(),
Block()
]

NodeLists = [
Block(),
Block(),
Block(),
Block(),
Block(),
Block(),
Block()
]

# 投票选选择见证者
def vote():
	for block in NodeLists:
		vote = randint(0, 100)
		block.Votes = vote

	# 根据 票数 排序 , 找到最多的一个点
	maxVote = 0
	nextWitness = NodeLists[0]
	for block in NodeLists:
		if block.Votes > maxVote:
			maxVote = block.Votes
			nextWitness = block

	return nextWitness


# 增加新 见证者
def addNewWitness():
	nextWitness = vote()
	WitnessList.append(nextWitness)

	print("新投票选举后，见证人列表：")
	for one in WitnessList:
		print(one.NodeAddress, "票数：", one.Votes)


# 踢出 见证者中坏节点
def removeBadWitness():

	if len(WitnessList) > N:
		# 排序踢出最低点
		minVote = 100
		badWitnessIndex = 0
		for index, block in enumerate(WitnessList):
			if block.Votes < minVote:
				minVote = block.Votes
				badWitnessIndex = index
		print("投票数最少：", minVote)
		WitnessList.pop(badWitnessIndex)

	print("新见证人列表： ")
	for one in WitnessList:
		print(one.NodeAddress, "票数：", one.Votes)



addNewWitness()
removeBadWitness()