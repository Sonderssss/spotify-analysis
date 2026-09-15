import pandas as pd

def clean_streaming_data(raw_path):
    spotify_df = pd.read_csv(raw_path)

    #convert column to a date time from string
    spotify_df['ts'] = pd.to_datetime(spotify_df['ts'])

    spotify_df['ts'].dtypes
    spotify_df['ts'].head()

    # use local time 
    spotify_df['ts_localized'] = spotify_df['ts'].dt.tz_localize('UTC').dt.tz_convert('Africa/Nairobi').dt.tz_localize(None)

    #create the date and time columns separately
    spotify_df['year'] = spotify_df['ts_localized'].dt.year

    spotify_df['month'] = spotify_df['ts_localized'].dt.month

    spotify_df['day_of_week'] = spotify_df['ts_localized'].dt.day_name()

    spotify_df['localized_hour'] = spotify_df['ts_localized'].dt.hour

    spotify_df[['reason_start', 'reason_end']].isna().sum()

    spotify_df[['reason_start', 'reason_end']] = spotify_df[['reason_start', 'reason_end']].fillna('Unknown')

    return spotify_df

if __name__ == "__main__":  
    df = clean_streaming_data("data/raw/spotify_history.csv")
    print(df.dtypes)
    print(df.head())