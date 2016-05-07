from collections import deque
import random
random.seed(0, version=2)

print("Starting Game")

def getGuessHuman():
    return input("Where is the iocane powder: my cup (1) or yours (2)? ")
    
def getGuessComp(lst,ind):
    return lst[ind]

# guess the players next choice
def next_placement(pattern_dict, pattern):
    # default if pattern doesn't exist
    if pattern not in pattern_dict:
        return  "2"
    # if more guesses for 1 in past, make it 2
    if pattern_dict[pattern][0] > pattern_dict[pattern][1]:
        return "2"
    # visa vera
    elif pattern_dict[pattern][0] < pattern_dict[pattern][1]:
        return "1"
    # default to 2
    else:
        return "2"

# record guess
def record_guess(pattern_dict, pattern, guess):
    """Updates the `pattern_dict` dictionary by either creating a new entry
    or updating an existing entry for key `pattern`, increasing the count 
    corresponding to `guess` in the list."""
    
    # failed attempts at more pythonic implementation
    #print(pattern_dict.get(pattern, [0,0]))
    #print(int(guess))
    #pattern_dict[pattern] = pattern_dict.get(pattern, [0,0])[int(guess)-1] + 1
    
    # if pattern not in dict,
    # create new empty list
    if pattern not in pattern_dict:
        pattern_dict[pattern] = [0,0]
    # add one to guess in dict pattern key
    pattern_dict[pattern][int(guess)-1] += 1

# return queue as string
def queueToString(queue):
    ret = "";
    for x in queue:
        ret = ret+x
    return ret
    
def play_interactive(pattern_length=4,lst=None,ind=0):
    # hold queue of recent quesses
    queue = deque([])
    
    # keep track of how many times the computer
    # wins or looses
    numLost = 0
    numWin = 0
    
    # pattern dictionary
    patterns = {}
    
    # while there is no interuption
    while True:
        # if there is no set list of inputs
        # get some from the player
        if lst == None:
            guess = input("Where is the iocane powder: my cup (1) or yours (2)? ")
        # else, get the current guess in the
        # provided list
        else:
            # if at end of provided list, break out of loop
            if ind == len(lst):
                break
            # else, get guess and increase list index counter
            guess = lst[ind]
            ind+=1
        # place next poison cup based on patterns (default to 2)
        compPlace = next_placement(patterns,queueToString(queue))
        # if the queue matches the pattern length,
        # record the current guess
        if len(queue) == pattern_length:
            record_guess(patterns, queueToString(queue), guess)
        # append guess to queue
        queue.append(guess)
        # if queue is filled,
        # pop the first value
        if len(queue) > pattern_length:
            queue.popleft()
        # if guess is valid, proceed,
        # else break
        if guess == "1" or guess == "2":
            # if human guessed correctly
            # human wins
            if compPlace == guess:
                print("Good guess! Ack! I drank the poison!")
                numLost+=1
            # else, computer wins
            else:
                print("Wrong! Ha! Never bet against a Sicilian!")
                numWin+=1
             
            # print total wins/loses   
            print("You died",numWin,"times, and I drank the poison",numLost,"times")
        else:
            break
    # return total number of wins and loses
    return numLost, numWin

# play in batch
def play_batch(guesses, pattern_length=4):
    return play_interactive(pattern_length=pattern_length,lst=list(guesses))

#print(play_batch((random.choice(['1', '2']) for _ in range(10000)), 4))
print(play_batch(['1', '2', '1', '2', '1', '2'], 4))
#print(play_batch(['1', '1', '2', '1', '2', '1'] * 100, 2))