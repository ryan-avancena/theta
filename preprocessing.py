import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

peak_hours_2022 = pd.read_excel('./data/2022/2022-peak-hours-ca.xlsx',sheet_name='2022 Peak Hour Report')
traffic_volumes_2022 = pd.read_excel('./data/2022/2022-traffic-volumes-ca-v2.xlsx', sheet_name='2022 AADT DATA')

""" PEAK HOURS

- Dir = Direction of traffic flow
- AADT = Average Annual Daily Traffic
- AM Peak = Morning peak hour
- CS = Control Station
- CO = County Abbreviation
- D = The percentage of traffic in the peak direction during the peak hour (Calculated by dividing the measured PHV by the sum of both directions of travel during peak hour)
- DAY = Day of the week for the peak volume
- DDHV = Directional design hour volume
- DI = 1 to 12 districts are available statewide. The abbreviation identifies the district in which the count station is located.
- HR = Ending time for the peak hour volume listed (e.g: The volume observed from 1 to 2 would be recorded as 2)
- K = The precentage of AADT in both directions during the peak hour. Values in this table are derived by dividing the measured 2-way PHV.
- KD = The product of K and D. The percentage of AADT in the peak hour. Calculated by dividing the measured 1-way PHV by the AADT.
- MNTH = Month that the peak volume occured
- PHV = Peak Hour Volume in the peak direction. A one way volume in vehicles per hour as used here. 
- PM = Post Mile, the milage measured from the county line, or from the beginning of a route.
- PM Peak = Represents the afternoon peak period for traffic analysis.
- RTE = State highway route number
- YR = Year of when the count was made, this is on a 3-year cycle

"""

