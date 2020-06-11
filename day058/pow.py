from datetime import datetime
import hashlib

# 简单实现 PoW共识算法

NodesCount = 7

class Blockchain(object):
	def __init__(self, nodeAddress):
		self.globalBlocks = []
		self.nextBlock = None
		self.difficulty = 1
		self.height = 0
		self.nodeAddress = nodeAddress

	def generateBlock(self):
		Timestamp = str(datetime.now())
		if self.globalBlocks > 0:
			PrevHash = self.globalBlocks[-1].Hash
		else:
			self.generateFirstBlock()
			return
		Hash = hashlib.sha256((PrevHash + Timestamp).encode("utf-8")).hexdigest()
		NodeAddress = self.nodeAddress
		Data = "new block"
		self.nextBlock = Block(Timestamp, PrevHash, Hash, NodeAddress, Data)


	def generateFirstBlock(self):
		Timestamp = str(datetime.now())
		PrevHash = "0x0"
		Hash = hashlib.sha256((PrevHash + Timestamp).encode("utf-8")).hexdigest()
		NodeAddress = self.nodeAddress
		Data = "Start PoW Blockchain"
		self.globalBlocks.append(Block(Timestamp, PrevHash, Hash, NodeAddress, Data))

	def isBlockHashMatchDifficulty(self,hashStr, difficulty) -> bool:
		prefix = difficulty * "0"
		return prefix == hashStr[:difficulty]

	def confirmed_next_block(self):
		if self.isBlockHashMatchDifficulty(self.nextBlock.Hash, self.difficulty):
			self.nextBlock.Confirmed = self.nextBlock.Confirmed + 1

	def pow_add_next_block(self, otherNodeBlockchain):
		if otherNodeBlockchain.nextBlock.Confirmed > self.nextBlock.Confirmed:
			self.globalBlocks = otherNodeBlockchain.globalBlocks
			self.nextBlock = otherNodeBlockchain.nextBlock

		if self.nextBlock.Confirmed > NodesCount / 2:
			# 半数节点确认通过
			self.globalBlocks.append(self.nextBlock)


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



def test_isBlockHashMatchDifficulty():
	hashStr = 'a1534392279bddbf9d43dde8701cb5be14b82f76ec6607bf8d6ad557f60f304e'
	difficulty = 1

	print(Blockchain(0).isBlockHashMatchDifficulty(hashStr, difficulty))


def test_blockchain1():
	blockchain = Blockchain(0)

	blockchain.generateFirstBlock()

	print(blockchain.globalBlocks[0].__str__())

def test_blockchain2():
	blockchain = Blockchain(1)
	blockchain.generateFirstBlock()
	blockchain.generateBlock()


if __name__ == "__main__":
	test_isBlockHashMatchDifficulty()
	test_blockchain1()