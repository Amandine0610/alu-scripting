#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
<<<<<<< HEAD
        top_ten(sys.argv[1])
=======
        top_ten(sys.argv[1])
>>>>>>> 68b8ce230a4d3e06aa135669e86952be8f53256b
