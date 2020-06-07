import collections

# cards = ["LLZKE",'LCXEA','CVPPS','EAVSR','FXPFP']
# word = 'APPLE'
cards = ['ZZBZ','BAZB','XBXB','XBAX']
word = 'BAB'
import collections
from itertools import permutations
def solution(word,cards):
    words = collections.Counter(word)
    for i in range(len(cards)):
        cards[i] = list(cards[i])

    # [['L', 'L', 'Z', 'K', 'E'], ['L', 'C', 'X', 'E', 'A'], ['C', 'V', 'P', 'P', 'S'], ['E', 'A', 'V', 'S', 'R'], ['F', 'X', 'P', 'F', 'P']]
    
    # 열 permutaions 만들기
    row= list(range(len(cards[0])))

    row_candidate = list(map(list,permutations(row)))

    cnt = 0


    for i in range(len(row_candidate)):
        cand_word = []
        for j in range(len(cards)):
            cand_word.append(cards[j][row_candidate[i][j]])
        if collections.Counter(cand_word) == words:
            cnt += 1
    return cnt



print(solution(word,cards))