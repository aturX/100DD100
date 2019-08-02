#!/usr/bin/python3

import sys
import random
import math

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 0
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
# <Your feedback goes here>
#####################################################
#####################################################



# Outputs a random integer, according to a multinomial
# distribution specified by probs.
def rand_multinomial(probs):
    # Make sure probs sum to 1
    assert(abs(sum(probs) - 1.0) < 1e-5)
    rand = random.random()
    for index, prob in enumerate(probs):
        if rand < prob:
            return index
        else:
            rand -= prob
    return 0

# Outputs a random key, according to a (key,prob)
# iterator. For a probability dictionary
# d = {"A": 0.9, "C": 0.1}
# call using rand_multinomial_iter(d.items())
def rand_multinomial_iter(iterator):
    rand = random.random()
    for key, prob in iterator:
        if rand < prob:
            return key
        else:
            rand -= prob
    return 0

class HMM():

    def __init__(self):
        self.num_states = 2
        self.prior = [0.5, 0.5]
        self.transition = [[0.999, 0.001], [0.01, 0.99]]
        self.emission = [{"A": 0.291, "T": 0.291, "C": 0.209, "G": 0.209},
                         {"A": 0.169, "T": 0.169, "C": 0.331, "G": 0.331}]

    # Generates a sequence of states and characters from
    # the HMM model.
    # - length: Length of output sequence
    def sample(self, length):
        sequence = []
        states = []
        rand = random.random()
        cur_state = rand_multinomial(self.prior)
        for i in range(length):
            states.append(cur_state)
            char = rand_multinomial_iter(self.emission[cur_state].items())
            sequence.append(char)
            cur_state = rand_multinomial(self.transition[cur_state])
        return sequence, states

    # Generates a emission sequence given a sequence of states
    def generate_sequence(self, states):
        sequence = []
        for state in states:
            char = rand_multinomial_iter(self.emission[state].items())
            sequence.append(char)
        return sequence

    # Computes the (natural) log probability of sequence given a sequence of states.
    def logprob(self, sequence, states):
        ###########################################
        # Start your code
        F=log(0.5)+log(self.emission[states[0]][sequence[0]])
        i=1
        while i<len(states):
            A=log(self.transition[states[i-1]][states[i]])+log(self.emission[states[i]][sequence[i]])
            F=F+A
            i=i+1
        return F
        # End your code
        ###########################################


    # Outputs the most likely sequence of states given an emission sequence
    # - sequence: String with characters [A,C,T,G]
    # return: list of state indices, e.g. [0,0,0,1,1,0,0,...]
    def viterbi(self, sequence):
        ###########################################
        # Start your code
        P=[{}]    # 创建容器
        states=[0,1]   
        for idx,val in enumerate(states):
            P[0][val]={"prob":log(self.prior[idx])+log(self.emission[idx][sequence[0]]),"prev":None}
        for t in range(1,len(sequence)):
            P.append({})
            for idx,val in enumerate(states):
                max_tr_prob=max(P[t-1][pre_val]["prob"]+log(self.transition[i][idx]) for i,pre_val in enumerate(states))
                for i,pre_val in enumerate(states):
                    if P[t-1][pre_val]["prob"]+log(self.transition[i][idx])==max_tr_prob:
                        max_prob=max_tr_prob+log(self.emission[idx][sequence[t]])
                        P[t][val]={"prob":max_prob,"prev":pre_val}
                        break
        opt=[]
        max_prob = max(value["prob"] for value in P[-1].values())
        previous = None
        for st, data in P[-1].items():
            if data["prob"] == max_prob:
                opt.append(st)
                previous = st
                break
        for t in range(len(P) - 2, -1, -1):
            opt.insert(0, P[t + 1][previous]["prev"])
            previous = P[t + 1][previous]["prev"]
        num_0=0
        num_1=0
        for item in opt:    # 转码
            if item==0:
                num_0=num_0+1
            if item==1:
                num_1=num_1+1
        print ("Max logprob",self.logprob(sequence, opt))
        print ("Number-0: ", num_0)
        print ("Number-1: ", num_1)
        print(opt)
        return opt
        # End your code
        ###########################################

def read_sequence(filename):
    with open(filename, "r") as f:
        return f.read().strip()

def write_sequence(filename, sequence):
    with open(filename, "w") as f:
        f.write("".join(sequence))

def write_output(filename, logprob, states):
    with open(filename, "w") as f:
        f.write(str(logprob))
        f.write("\n")
        for state in range(2):
            f.write(str(states.count(state)))
            f.write("\n")
        f.write("".join(map(str, states)))
        f.write("\n")

hmm = HMM()

file = sys.argv[1]
sequence = read_sequence(file)
viterbi = hmm.viterbi(sequence)
logprob = hmm.logprob(sequence, viterbi)
name = "my_"+file[:-4]+'_output.txt'
write_output(name, logprob, viterbi)


