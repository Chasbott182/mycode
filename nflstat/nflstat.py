#!/usr/bin/env python3

import pandas as pd
from pandas.core.indexes.base import Index


def main():

    data_file= "nfl2020.csv"
    columnfilter = ["GAMEID", "GAMEDATE", "QUARTER", "MINUTE", "SECOND", "OFFENSETEAM", "DEFENSETEAM", "DOWN", "TOGO", "YARDLINE", "SERIESFIRSTDOWN", "NEXTSCORE", "SEASONYEAR", "YARDS", "FORMATION", "PLAYTYPE", "ISRUSH", "ISPASS", "ISINCOMPLETE", "ISTOUCHDOWN", "PASSTYPE", "ISSACK", "ISCHALLENGE", "ISCHALLENGEREVERSED", "CHALLENGER", "ISMEASUREMENT", "ISINTERCEPTION", "ISFUMBLE", "ISPENALTY", "ISTWOPOINTCONVERSION", "ISTWOPOINTCONVERSIONSUCCESSFUL", "RUSHDIRECTION", "YARDLINEFIXED", "YARDLINEDIRECTION", "ISPENALTYACCEPTED", "PENALTYTEAM", "ISNOPLAY", "PENALTYTYPE", "PENALTYYARDS"]
    
    # Reading in a csv file"
    dataframeobj = pd.read_csv(data_file, usecols=lambda x: x.upper() in columnfilter)


    print(dataframeobj.shape)
    team = input("What NFL teams season do you want: ").split().upper()

    datasort = dataframeobj.sort_values(["GameId"], ascending=True)
    datafilter = datasort.query(f"OffenseTeam == {team} | DefenseTeam == {team}")

    print(datasort.head())
    # Print first five rows
    
    datafilter.to_csv("buffalobills2020season.csv")



if __name__ == "__main__":
    main()

 