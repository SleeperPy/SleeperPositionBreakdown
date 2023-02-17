# SleeperPositionBreakdown
This Python script queries the Sleeper API to figure out which players are owned by each team in a Sleeper fantasy football league, and then produces a graph showing how each team is broken down by position group.

You'll first need to run SleeperGetPlayers.py, IT IS IMPORTANT THAT YOU RUN THIS NO MORE THAN ONE TIME PER DAY, it produces a very large file that is used for the SleeperPositionBreakdown.py script. You'll then need to run SleeperPositionBreakdown.py from the same directory that the file produced by SleeperGetPlayers.py is in. 

You'll need the league ID for your league. This can be found in the URL of your Sleeper league: https://sleeper.com/leagues/<this_number_right_here>/matchup. Or if you open the App and go to your league -> League tab -> Settings (the gear icon) -> General, and then scroll to the bottom.

Sleeper API Documentation: https://docs.sleeper.com/#introduction

![](https://github.com/SleeperPy/SleeperPositionBreakdown/blob/main/SleeperPositionBreakdown.gif)
