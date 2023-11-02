#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_avg = len(sys.argv) -1 
    if num_avg == 1:
        print("{} arguments:".format(num_avg))
    elif num_avg == 0:
        print("{} arguments:".format(num_avg))
    else:
        print("{} arguments:".format(num_avg))
    
    if num_avg >= 1:
        num_avg = 0
        for i in sys.argv:
            if num_avg != 0:
                print("{}: {}".format(num_avg, i))
            num_avg += 1
