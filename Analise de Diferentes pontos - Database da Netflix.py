# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

##First Part:
#Subset the netflix_df to a Movie collum
netflix_sbst = netflix_df[netflix_df["type"] == "Movie"]

#Subset the new netflix_sbst to movies of 1990 to 2000
m_1990 = netflix_sbst[(netflix_sbst["release_year"] >= 1990) & (netflix_sbst["release_year"] < 2000)]

#Plot all of this in a Histogram called "Distribution of Movie Durations in the !990s"
plt.hist(m_1990["duration"])
plt.title("Distribution of Movie Durations in the 1990s")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.show()

##Second Part:
#Subset the netflix_sbst (used in the first part) to take Action movies
sbst = netflix_sbst[netflix_sbst["genre"] == "Action"]

#Set short_movie_count to 0 and start the for loop
short_movie_count = 0

#The for loop is gonna take the l (Label) and the r (Rows) in m_1990 (used in the first part) and use that to make an if statement
for l, r in m_1990.iterrows() :
    
    #If the duration of a movie (selected in r) is less than 90, it will be accounted in the short_movie_count and plus 1, updating the old variable
    if r["duration"] < 90 :
        short_movie_count = short_movie_count + 1

#Show the result in a form of a print in the terminal
print(short_movie_count)