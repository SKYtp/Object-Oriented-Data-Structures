def most_common(lst):
    return max(set(lst), key=lst.count)
def keep(item):
    return item in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print("*** Election ***")
nVote  = int(input("Enter a number of voter(s) : "))
vote = list(input().split())
for i in range(nVote):
    vote[i] = int(vote[i])
newlist = list(filter(keep, vote))
qList = []
if(newlist == qList):
    print("*** No Candidate Wins ***")
else:
    print(most_common(newlist))