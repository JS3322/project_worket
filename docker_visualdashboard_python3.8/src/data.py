import pandas as pd

conditions = ["confirmed", "deaths", "recovered"]

apple_df = pd.read_csv('src/data/2014_apple_stock.csv')
jobs_df = pd.read_csv("src/data/jobs.csv")
daily_df = pd.read_csv("src/data/daily_report.csv")

getJob_df = jobs_df[["ID", "TITLE", "COMPANY_NAME", "COMPANY_LOC", "SALARY"]]

totals_df = (
    daily_df[["Confirmed", "Deaths", "Recovered"]
             ].sum().reset_index(name="count")
)
totals_df = totals_df.rename(columns={"index": "condition"})

countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()


def make_country_df(country):
    def make_df(condition):
        df = pd.read_csv("src/data/time_confirmed.csv")
        df = df.loc[df["Country/Region"] == country]
        df = (
            df.drop(columns=["Province/State",
                    "Country/Region", "Lat", "Long"])
            .sum()
            .reset_index(name=condition)
        )
        df = df.rename(columns={"index": "date"})
        return df

    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df


def make_global_df():
    def make_df(condition):
        df = pd.read_csv(f"src/data/time_{condition}.csv")
        df = (
            df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
            .sum()
            .reset_index(name=condition)
        )
        df = df.rename(columns={"index": "date"})
        return df

    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df
