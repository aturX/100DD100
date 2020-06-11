import hashlib
from random import randint

# 简单实现PoS 共识算法

nextBlocks = ['1a6562590ef19d1045d06c4055742d38288e9e6dcd71ccde5cee80f1d5a774eb']

class Block(object):
	def __init__(self, Timestamp, PrevHash, Hash, NodeAddress, Data):
		self.Timestamp = Timestamp
		self.PrevHash = PrevHash
		self.Hash = Hash
		self.NodeAddress = NodeAddress
		self.Data = Data
		self.Confirmed = 0

	def __str__(self):
		print("-"*30)
		return f"Timestamp = {self.Timestamp},\nPrevHash = {self.PrevHash},\nHash = {self.Hash},\nNodeAddress = {self.NodeAddress},\nData = {self.Data}"


def getCoinBalance(block, NodeAddress):
	# 随机返回一个值当余额， 只做演示
	return randint(0, 100)

def getNodeAddress():
	# 随机返回一个地址， 只做演示
	num = str(randint(0, 100))
	address = hashlib.sha256(num.encode("utf-8")).hexdigest()

	return address

stackRecord = []
def AddressNodeRun():
	NodeAddress = getNodeAddress()
	for block in nextBlocks:
		coinNum = getCoinBalance(block, NodeAddress)  # 币数量
		for i in range(coinNum):
			stackRecord.append(NodeAddress)
AddressNodeRun()  # 节点一
AddressNodeRun()  # 节点二
AddressNodeRun()  # 节点三
print(stackRecord)

# 然后 ，随机从 stackRecord 中 随机选一个地址，作为胜利者，币越多， 股权越大，被选中概率越大

winner = stackRecord[randint(0, len(stackRecord))]

print(winner)
