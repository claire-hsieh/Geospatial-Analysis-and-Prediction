import gzip as gz
import argparse 
import pandas as pd

# Reads raw NOAA ISD data and displays it in a pandas dataframe
# Input: raw NOAA ISD data file in gz format

parser = argparse.ArgumentParser(description='Display ISD data')
parser.add_argument('-i', '--input_file',  type=str, help='Input file name')
args = parser.parse_args()



offset = [0, 4, 10, 15, 23, 28, 34, 41, 46, 51, 56, 60, 64, 65, 69, 70, 75, 76, 77, 78, 84, 85, 86, 87, 92, 93, 98, 99, 104]
line_len = [4,  6,  5,  8,  4,  6,  7,  5,  5,  5,  4,  3,  1,  4,  1,  5,  1,  1,  1,  6,  1,  1,  1,  5,  1,  5,  1,  5,  1]
col_name = ['var_length', 'usaf_id', 'wban', 'date', 'gmt', 'lat', 'long', 'report_type', 'elev', 'call_letters', 'qc_level', 'wind_dir', 'wind_type', 'wind_speed', 'wind_speed_flag', 'sky_ceiling', 'sky_ceil_flag', 'sky_ceil_determ', 'sky_cavok', 'visibility', 'vis_flag', 'vis_var', 'vis_var_flag', 'air_temp', 'air_temp_flag', 'dew_point', 'dew_point_flag', 'sea_lev_press', 'sea_levp_flag']
df = pd.DataFrame(columns=col_name)

def display_data(input_file):
    with gz.open(input_file, 'rt') as f:
        for i, line in enumerate(f.readlines()):
            for col, j in zip(df.columns, range(len(offset))):
                # df.at[i, col] = line[offset[i]:offset[i]+line_len[i]].strip()
                # print(col, line[offset[i]:offset[i]+line_len[i]].strip())
                df._set_value(i, col, line[offset[j]:offset[j]+line_len[j]].strip())
    print(df.head())
    return df            


if __name__ == '__main__':
    display_data(args.input_file)
