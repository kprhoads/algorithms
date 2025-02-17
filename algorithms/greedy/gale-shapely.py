"""
The Gale-Shapely algorithm is a greedy approach to solving the stable matching problem.

The stable matching problem seeks the most desirable matching of two equal sets using preferences from each participant.
The outcome must be mutually desirable, meaning there should be no unpaired set of participants who prefer eachother more than their actual pairing.

An example of the stable matching problem would be a set of employers and a set of potential employees.
Each employer sets a desired preference for each candidate, and each candidate orders their preference of workplaces.
The Gale-Shapely algorithm assigns each participant to the highest possible mutual outcome.

This is solved by performing iterations where one set's preferences are offered to be paired, in order.
The set that is recieving the offers takes the most optimal offer. 
For example, if a participant is not yet paired and they are offered a pair, they take it.
Otherwise, if they are offered a pair they prefer more than their current pair, they accept it, and if they do not prefer it, they deny it.

This process repeats until no participant is left unpaired.
"""

def gale_shapely(arr_x, arr_y):
    '''
    Both arrays are 2-D arrays. Each row represents a participant's preferences. In this example, participants of arr_x are proposing to arr_y.
    Participants are numbered 1-n.
    '''
    # initialize additional containers
    unmatched_x = {i+1 for i in range(len(arr_y))}  # set for participants in x not yet matched
    next_preferences = [0 for i in range(len(arr_y))]   # array indexed by participant x, value = next preference index
    current_match = [0 for i in range(len(arr_x))]      # array indexed by participant y, value = current pair (0=no pair)

    # stable matching
    while len(unmatched_x) > 0:
        for participant_x in unmatched_x.copy():
            # offer pair to next participant_y in order of preference
            index_offered = next_preferences[participant_x-1]
            participant_offered = arr_x[participant_x-1][index_offered]

            # check if participant_offered is unmatched
            if current_match[participant_offered-1] == 0:
                # participant_offered has no pair, offer accepted
                current_match[participant_offered-1] = participant_x
                unmatched_x.remove(participant_x)
            else:
                # particpant_offered is matched, check their preferences
                for preference in arr_y[participant_offered-1]:
                    if preference == participant_x:
                        # make new pair
                        unmatched_x.add(current_match[participant_offered-1])
                        current_match[participant_offered-1] = participant_x
                        unmatched_x.remove(participant_x)
                        break
                    elif preference == current_match[participant_offered-1]:
                        # keep old pair
                        break
            next_preferences[participant_x-1] += 1
            #print(current_match)
    
    # print resulting pairs
    print("Pairs: X Y")
    for x in range(len(arr_y)):
        y = current_match.index(x+1)
        print(x+1, y+1)
                        



gale_shapely([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]], [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
#gale_shapely([[3,2,1,4],[2,4,3,1],[1,4,3,2],[3,4,1,2]], [[1,4,2,3],[2,1,3,4],[1,2,4,3],[3,4,2,1]])
