# Crime-Analysis-

## Roadmap:

### For sure need to get done for a suitable project:


- [ ] JOIN DATASETS (In progress - Eric)
- [ ] Two ML assignments (Emily M taking lead on regression ML assignment. Shawn taking lead on classification ML assignment)

- [ ] If we want to use police sentiment data, we need to find a way to get police beats and districts to fit into communities. Would say its optional but it also has good census type data that would be helpful. (In progress - Eric)


- [ ] Maybe need to do some label encoding where appropriate
- [ ] Explore which features we want to specifically use for regression/prediction. Identify variables with highest correlation to crime. Organize and create dataset(s) just looking at these variables and crime(s) (we can choose specific types of crime too if we want)
- [ ] Create a regression model with training and testing data. Experiment with different simple regression models
- [ ] As Emily suggested, need to choose which time level we want our regression model to predict at. Probably monthly. 
- [ ] Create some kind of prediction model looking at crime and socioeconomic trends to predict future crimes in each area. 
- [ ] Start and finish final paper and presentation
- [ ] Add population counts for each sector to calculate crime per capita

### Optional but would make our project better:


- [ ] Need to figure out how certain things are relevant like housing, grocery stores and transportation (Could use things like quantity of in each community area, distance from transportation areas, density of grocery stores etc.) Would have to create our own quantifiable data to use these which will be difficult. (This is probably the hardest thing we have to do. Can begin creating a model with more straight forward, already quantifiable data like census data, police sentiment scores, etc.) 

### Optional only if we have time:

- [ ] Use Chicago to create our regression model and find data from other cities looking at similar socioeconomic factors and assess regression model against this data. Could then improve model by integrating other cities crime data as well. Could also be used to create and improve any prediction model as well.

- Eric

  

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
