# Election-analysis by Ketaki
## Overview of Election Audit
The main purpose of the election audit analysis is to help the users Tom and Seth submit them to the Election Commission. Such type of audit is done using a Python script that is faster than manual work and useful to understand certain election statistics of voter turnaround, total votes per region, candidate,etc. 
## Election Audit Results
- A total of 369,711 votes were casted in the election.
- County-wise summary is as follows:
  -  Jefferson county got 38,855 number of votes that was 10.5% of the total vote count.
  -  Denver county got 306,055 number of votes that was 82.8% of the total vote count.
  -  Arapahoe county got 24,801 number of votes that was 6.7% of the total vote count. the least number of votes.
- **Denver** county got the highest number of votes (306,055)  with an overall percentage of 82.8% .
- Candidate-wise summary is as follows:
  - Charles Casper Stockham received 23.0%  of total votes with a vote count of 85,213.
  - Diana DeGette received 73.8% of total votes with a vote count of 272,892.
  - Raymon Anthony Doane received 3.1%  of total votes with a vote count of 11,606.
- **Diana DeGette** won the election with a whopping 272,892 votes which accounted for 73.8% of the total vote count.
## Election Audit Summary
This Python script used for election analysis makes reading and analyzing large election data easier and quick. 
It can be extended for reading similar other election files and performing the required analysis. 
Some use cases such as :
- Find any duplicate/(or missing?) Ballot IDs( voters that voted more than once from different counties or different candidates).
- Compare the percentage of voter turnaround to previous years elections and to the overall population.
