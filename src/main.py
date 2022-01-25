# Check that all modules needed are put in your requirements.txt file
 
import pandas as pd
import argparse
import pandas as pd

from pathlib import Path
from datetime import datetime

import twitter
import logging
logging.basicConfig(level=logging.DEBUG)



def main(dataframe: pd.DataFrame, token, usercol: str='user',sizeofspeech=10) -> pd.DataFrame:        
    client = twitter.Twio(token)
    dataframe["speech"] = [client.speechof(client.getuser(twittos,sizeofspeech=sizeofspeech)).replace("\n","") for twittos in df[usercol]]
    today = datetime.now()
    dataframe["dt"]=str(today)
    dataframe["nboftweet"]=sizeofspeech
    return dataframe



if __name__ == '__main__':
    # Test your component
    # By executing your script with a python main [ARGS]

    # Put meaningful description and args for your user
    parser = argparse.ArgumentParser(description='Parse content from an url and a query selector')
    
    # do not use positionnal argument, always use the --arg syntax
    # note all the args name are they must be reported in the yaml component file
    parser.add_argument('--src', required=True, type=str, help='Path of the local file containing the Input data.')
    parser.add_argument('--dst', required=True, type=str, help='Path of the local file for output data.')
    parser.add_argument('--token', required=True, type=str, help='Twitre Bearer Token')
    parser.add_argument('-u', '--user-col', required=False, default="user", type=str, help='Column containing twitter user ( not the username )')
    parser.add_argument('-s', '--size', required=False, default=10, type=int, help='Cnb of tweet to get ( 10<s<100 ) ')        
        

    args = parser.parse_args()
    src = args.src
    dst=args.dst
    
    # Warning : remember that argparse will convert any - to _ ( https://docs.python.org/dev/library/argparse.html#dest 
    usercol = args.user_col
    size = args.size
    
    df = pd.read_csv(src)
    token = args.token
    # entry point of your transformation
    ef = main(df, token, usercol,sizeofspeech=size)

    # if you save some data , your component must create the output path
    # Even if a file as pipeline may required to create a temp path
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    ef.to_csv(dst, index=False)

