


"""
There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, you must determine the maximum number of topics a 2-person team can know. Also find out how many ways a team can be formed to know that many topics. Lists will be in the form of bit strings, where each string represents an attendee and each position in that string represents a field of knowledge, 1 if its a known field or 0 if not.
Complete the acmTeam function in the editor below. It should return an integer array with two elements: the maximum number of topics any team can know and the number of teams that can be formed that know that maximum number of topics.
"""
from itertools import combinations,permutations
def acmTeam(topic):
    x=(list(combinations(topic,2)))
    y=[]
    z=[]
    for i in x:
        y.append(int(i[0])+int(i[1]))
    s=0
    for i in y:
        for j in str(i):
            if j=='2' or j=='1':
                s=s+1
        z.append(s)
        s=0
    return([max(z),z.count(max(z))])
nm = input().split()

n= int(nm[0])
m = int(nm[1])
topic = []
for _ in range(n):
    topic_item = input()
    topic.append(topic_item)
result = acmTeam(topic)
print(result)