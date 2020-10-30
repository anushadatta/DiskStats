#!/usr/bin/python3
import sys
import os
import pandas as pd

# Determine disk space used by each directory
def get_size(path):
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size
        except  Exception as e:
            print("exception:  ",e)
            total+=0
    return total

if __name__ == '__main__':
    path = '/home'
    print("total arguments passed: " , len(sys.argv))

    directory = sys.argv[1] if len(sys.argv) >= 2 else path

    usage = []
    paths = []

    # Access each sub-directory
    for entry in os.scandir():
        print(entry.path)
        
        # Generate report in CSV format
        if (entry.is_dir(follow_symlinks=False)):
            print (entry.path  + " is a dirctory")
            print(get_size(entry.path))
            total= get_size(entry.path)
            print (total)
            paths.append(entry.path)
            usage.append(total)
            usage_dict = {'directory' : paths, 'usage' : usage}
            df = pd.DataFrame(usage_dict)
            print (df)
            print (df)
            df.to_csv("disk_home_usage.csv")
