#Basketball coach Phil Jackson says that in order for an NBA
#team to be a contender for a championship, they need to win
#40 games before they lose 20 games.
#
#Write a function called is_a_contender that will take three
#parameters: a team name (a string), a number of wins (an
#integer), and a number of losses (an integer).
#
#Based on these parameters, the function should return one
#of three strings:
#
# - If the team is a contender (at least 40 wins and fewer
#   than 20 losses), return "The [team name] are a contender!"
# - If the team is not a contender (less than 40 wins and at least
#   20 losses), return "The [team name] are not a contender!"
# - If it cannot be determined (both values are higher or both
#   values are lower), return "The [team name] might be a contender!"


#team name, a number of wins, and a number of losses:
def is_a_contender(team, wins, losses):
    
    #The team is a contender if it reaches 40 wins before it
    #reaches 20 losses. So, if wins is >= 40, and losses is
    #still less than 20, the team is a contender:
    if wins >= 40 and losses < 20:
        return "The " + team + " are a contender!"
    
    #The team is not a contender if it reaches 20 losses
    #before it reaches 40 wins. So, if losses is >= 20, and
    #wins is still below 40, the team is not a contender:
    elif wins < 40 and losses >= 20:
        return "The " + team + " are not a contender!"
    
    #What if wins is greater than 40 and losses is greater
    #than 20? We don't actually know which came first. Or,
    #what if wins is less than 40 and losses is less than
    #20? We don't know what will happen. So, we're unsure.
    #
    #This is the only other possible result from the
    #expressions above, so we just wrap it in an else. If
    #neither of the above were true, then we don't know if
    #the team is a contender:
    else:
        return "The " + team + " might be a contender!"



