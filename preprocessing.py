import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

YEARS = [2016,2017,2018,2019,2020,2021,2022]

def create_peak_hours():
    all_peak_hours = []

    for year in YEARS:
        file_path = f'./data/peak-hours/{year}-peak-hours.xlsx'
        try:
            df = pd.read_excel(file_path, sheet_name=f'{year} Peak Hour Report')
            df['YEAR'] = year  # Add year column for reference
            # print(df.shape)
            all_peak_hours.append(df)
        except FileNotFoundError:
            print(f"File not found for year {year}, skipping...")

    # Concatenate all years into a single DataFrame
    peak_hours_df = pd.concat(all_peak_hours, ignore_index=True)
    # print(peak_hours_df.columns)
    return peak_hours_df

def correlation_matrices(los_angeles):
    la_numeric_cols = los_angeles.select_dtypes(include=[np.number]).columns

    # correlation matrix 
    corr_matrix = los_angeles[la_numeric_cols].corr()
    plt.figure(figsize=(12, 12))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix - Los Angeles")
    plt.show()

    # predictive values matrix 
    highly_correlated = ['AM_WAY_PHV','PM_WAY_PHV','AM_K_FACTOR_AMT','AM_D_FACTOR_AMT','AM_KD_FACTOR','PM_K_FACTOR_AMT','PM_D_FACTOR_AMT','PM_KD_FACTOR']
    corr_matrix = los_angeles[highly_correlated].corr()
    plt.figure(figsize=(12,12))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix - Los Angeles")
    plt.show()

def scatter_plots(los_angeles):
    # scatterplots
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=los_angeles, x='AM_HOUR', y='AM_WAY_PHV', alpha=0.5, edgecolor=None)
    plt.xlabel("Morning Hour (AM_HOUR)")
    plt.ylabel("Volume of Cars")
    plt.title("Traffic Volume by Morning Hour in Los Angeles")
    plt.grid(True)
    plt.show()

    # scatterplot with trend-line
    plt.figure(figsize=(10, 6))
    sns.regplot(data=los_angeles, x='AM_HOUR', y='AM_WAY_PHV', scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
    plt.xlabel("Morning Hour (AM_HOUR)")
    plt.ylabel("AM Peak Hour Volume (AM_WAY_PHV)")
    plt.title("Traffic Volume by Morning Hour in Los Angeles (with Trendline)")
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    peak_hours = create_peak_hours()
    peak_hours.drop(columns=['RTE_SFX','PM_SFX','PM_PFX','PRE','CS'],inplace=True)
    # print(peak_hours.shape)
    # print(peak_hours.isna().sum())

    los_angeles = peak_hours[peak_hours['CO'] == 'LA']

    print(los_angeles.shape)

    AM_TIME_BASED_FEATURES = ['AM_HOUR', 'AM_DAY', 'AM_MONTH','PM']
    PM_TIME_BASED_FEATURES = ['PM_HOUR', 'PM_DAY', 'PM_MONTH','PM']

    AM_DIRECTION_FEATURES = ['AM_DIR','AM_WAY_PHV','AM_K_FACTOR_AMT','AM_D_FACTOR_AMT','AM_KD_FACTOR']
    PM_DIRECTION_FEATURES = ['PM_DIR','PM_WAY_PHV','PM_K_FACTOR_AMT','PM_D_FACTOR_AMT','PM_KD_FACTOR']


    feature_columns = ['PM_HOUR', 'BACK_PEAK_HOUR', 'AHEAD_PEAK_HOUR', 'BACK_AADT', 'AHEAD_AADT']
    target_column = 'PEAK_HOUR_VOLUME'

    # EDA - uncomment to check
    # correlation_matrices()
    # scatter_plots()

    """ CHECKING MORNINGS """




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