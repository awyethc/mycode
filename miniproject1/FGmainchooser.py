#!/usr/bin/env python3

"""This script is intended, through the use of weighted questions to suggest a fighting game character archetype,
    as well as a short list of example characters to a user. To keep it simple, a maximum of 5 multiple choice will
    be asked, resulting in one of four archetypes suggested to the user as a return. 
    Archetypes to be used: BALANCED, RUSHDOWN, ZONER, GRAPPLER. """

def main():

    # main loop section, store question number (named "qnum") here, while condition is "while qnum <=5"
    # print("Question #", qnum)
    # ask Bard/GPT for code
    # name archetype variables as follows
        bal_arc # BALANCED
        rsh_arc # RUSHDOWN
        znr_arc # ZONER
        grp_arc # GRAPPLER

    # REQUIREMENTS:
    # need dictionaries(?) that list 3 example characters in a single string
    # need question bank, copy format from flowcharts, listicles, etc
    # scoring for questions?
        #3 pts for closest match answer                  
        #2 pts for medium matching answer
        #1 pt for least matching
        #0 pt for opposite arc_type
            # example: Swords or Guns?
            #          a)Swords! (+3 bal_arc, +2 rsh_arc, +1 grp_arc)
            #          b)Guns!   (+3 znr_arc, +2 bal_arc, +1 rsh_arc)
            #          c)FISTS!  (+3 rsh_arc, +2 grp_arc, +1 bal_arc)

    # after each question add pts to arc variables and continue on to next question, repeat while qnum <=5
    # point totals kept hidden
    # need a tie breaker?

    # BONUS OBJECTIVES: more than 5 questions
                      # randomly positioned answers
                      # more archetypes
                      # random comments from "questioner"
                      # mixed "top 3" style character results based on final arc_weights (COMPLICATED?)

"""ALTERNATIVE IDEA, GENERATE RANDOM OPPONENT, PRESENT OPTIONS, COMPARE RESULT ACCORDING TO OPPONENT ARCTYPE, THEN CONTINUE FOR 4 MORE ROUNDS. BASICALLY YOMIHUSTLE?"""


if __name__ == "__main__":
    main()
