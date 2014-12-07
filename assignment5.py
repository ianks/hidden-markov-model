# HMM involves a hidden state that changes over time, as well as observable
# evidence that is used to make an inference about a hidden state.
#
# An HMM is define by three sets of probabilities:
#    1. Probability of observing each output o at that state:
#        - P(E[t]=o | X[t]=s)
#    2. Probability of moving from current state to every other state:
#        - P(X[t+1]=s' | X[t]=s)
#    3. Distrubution over the start state P(X[0])

try:
    from IPython import embed
except:
    pass

import getopt, sys
from run_viterbi import run_viterbi
import src
from hmm import Hmm


debug = False

def main():

    #Setup Variables
    data = None
    hmm = None

    #Import arguments and parse into options.
    try:
        optlist, remainder = getopt.getopt(sys.argv[1:], 'p:o:vh')
        #If no arguments profided
        if len(optlist) == 0:
            print "***Options required***"
            usage()
    #if inappropriate argument provided
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for option, argument in optlist:
        if option == "-v":
            debug = True
            if debug:
                #view input
                print "\nProvided Arguments: "
                print str(optlist) + "\n"
        elif option == "-h":
            usage()

        elif option == "-p":
            if argument not in ('1', '2', '3'):
                print "You must input a problem number"
                usage()
            if argument == '1':
                data = src.Robot('data/robot_no_momemtum.data')
            elif argument == '2':
                print "Functionality not implemented"
            elif argument == '3':
                print "Functionality not implemented"

        elif option == '-o':
            if argument not in ('1', '2'):
                print "You must input a valid hmm order"
                usage()
            if argument == '1':
                # call HMM process
                hmm = Hmm(data)
                run_viterbi(data, hmm)
            elif argument == '2':
                print "Functionality not implemented"
                exit()

def usage():
    print """

    Usage:
    ---
        Flags
        -p  Problem Number (1,2,3)
        -o  HMM Order (1, 2)
        -v  verbose
        -h  help
    ---
        Problem number
         1  Toy Robot
         2  Typo Correction
         3  Topic Change
    ---
        HMM order
         1  First-order HMM
         2  Second-order HMM
    ---
        Example Usage
        python assignment5.py -p 2 -o 1
        (Run with Typo Correction and first-order HMM)

    """
    sys.exit(2)

if __name__ == "__main__":
    main()
