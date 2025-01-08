# Exercises - Pandas

# Load needed module(s)
import pandas as pd
import os

## 1. Read the hacker_news.csv file from [here](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv)
news_df = pd.read_csv(os.path.join("ancillary", "hacker_news.csv"))

## 2. Get the first five rows
news_df.head(n = 5)

## 3. Get the last five rows
news_df.tail(n = 5)

## 4. Get the title column as pandas series
title_ser = news_df["title"]
title_ser
type(title_ser)

## 5. Work with the data in the following ways:
### 5A. Count the number of rows and columns
print("5A: There are", len(news_df.columns), "columns")
print("5A: There are", len(news_df), "rows")

### 5B. Filter the titles which contain python
py_news = news_df[news_df["title"].str.contains("[Pp]ython")]
print("5B:", len(py_news), "titles include 'Python' (case insensitive)")

### 5C. Filter the titles which contain JavaScript
js_news = news_df[news_df["title"].str.contains("[Jj]ava[Ss]cript")]
print("5B:", len(js_news), "titles include 'JavaScript' (case insensitive)")

### 5D. Explore the data and make sense of it
news_df.dtypes
news_df.shape
