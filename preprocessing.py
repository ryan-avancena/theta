import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

peak_hours_2022 = pd.read_excel('./data/2022/2022-peak-hours-ca.xlsx',sheet_name='2022 Peak Hour Report')
traffic_volumes_2022 = pd.read_excel('./data/2022/2022-traffic-volumes-ca-v2.xlsx', sheet_name='2022 AADT DATA')

""" DATASETS

peak_hours_2022 - (1340, 26)
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

traffic_volumes_2022 - (7116, 14)
- FRONT = traffic going NORTH or EAST
- BACK = traffic going SOUTH or WEST
"""

if __name__ == '__main__':
    # print(peak_hours_2022.columns)
    # print(traffic_volumes_2022.columns)
    # print(peak_hours_2022['CO'].unique())
    # print(traffic_volumes_2022['COUNTY'].unique())
    

    # focusing on Los Angeles right now
    los_angeles = peak_hours_2022[peak_hours_2022['CO'] == 'LA'].drop(columns=['RTE_SFX','PM_PFX','PM_SFX'])
    orange = peak_hours_2022[peak_hours_2022['CO'] == 'ORA'].drop(columns=['RTE_SFX','PM_PFX','PM_SFX'])

    la_numeric_cols = los_angeles.select_dtypes(include=[np.number]).columns
    
    # correlation matrix
    corr_matrix = los_angeles[la_numeric_cols].corr()
    plt.figure(figsize=(12, 12))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix - Los Angeles")
    plt.show()

