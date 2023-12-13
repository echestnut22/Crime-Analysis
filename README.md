# Crime-Analysis-

TODO

High Priority:

- Finish aggregating and cleaning data. Upload to database
- Start statistical EDA once all datasets can be joined (regression to start looking for relationships with crime)

Medium Priority:
- Find another city with good data on public goods, housing, access to transportation and other public services etc. as well as crime data to eventually be used for our prediction model

Lower priority:
- Find more Chicago socioeconomic datasets
- From my understanding, it will be a lot simpler for a machine learning model to digest numerical data, so we should at some assign point assign categories to number values (ie. Assault is 0, Theft is 1, Narcotics is 2, etc.). This is called label encoding. There is also one-hot encoding, a different type of encoding to look into. - Eric 

Questions/Concerns about Datasets (Emily M):

Grocery Store Data
- This data apparently only applies to 2013 so I'm not sure if it will be useful for our overall model. If we wanted to do a snapshot analysis of 2013, we still have time series data that could be frequent enough for analysis. We can discuss this more.
We could identify which areas are food deserts and create a 'Y'/'N' column for this using distance between the crime location and a grocery store. Food deserts are defined as areas in Chicago which are more than 0.5 or 1 mile from a grocery store, depending on the grocery store size. This is represented by the 'A' or 'B' buffer size. We could also represent this as the count of grocery stores within 0.5 or 1 mile.
- We could also simply provide the count of grocery stores for each community area, but we would probably need to control for population size using census data that can give us population numbers by Community Area. I think we could try this first, see if any correlation exists, and if one does, we can investigate further and focus in on food deserts.
  
Housing Data:
- This data is clean enough and we can provide the number of affordable housing units per community area, but since there is no time column, I'm unsure how we could use this to train our model. This data was updated in October 2023, but there is no easy way to tell when each apartment/unit was built, so these numbers would likely only be reliable for the past 5-10 years. The grocery store data presents the same problem. We may need to think about separate analyses for time series vs. regression since some of our independent variables are so time restricted.

Overall:
- We need to think about what we want our dependent variable to be and how we can structure the data for a regression model. Y could be the crime level per capita, the crime level for a specific type of crime, or the relative proportion of crime types. We should structure the data in a way will allow us to perform regression and serve as training data.
- We need to think about what frequency level we want for regression. Our supplemental datasets that have a measure of time only go to the Year-Month level, so this could be a good choice. We could aggregate the data based on community area and year-month for a specific timeframe.
