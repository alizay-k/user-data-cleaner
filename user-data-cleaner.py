import pandas as pd

df=pd.read_csv(r"c:/Users/Alizaayk/Desktop/dirty_user.csv")
rows_before=len(df)
df=df.drop_duplicates()
print(df.isnull().sum())
df_filled=df.fillna({
    "name":"unknown",
    "email":"noemail@example.com",
    "age":0,
    "country":"unknown"
})
rows_after=len(df_filled)

print(f"total rows left:{rows_before}-{rows_after}={rows_before-rows_after}")
df_filled.to_csv("cleaned_user.csv",index=False)

