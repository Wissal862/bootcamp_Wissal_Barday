\# NYC Subway Delay Forecasting



\## Problem Statement 



Daily commuters in New York City lose time and face frustration because subway service alerts are vague and inconsistent across apps. The MTA communications team is the decision maker, while the end users are commuters planning their daily routes. A descriptive + predictive analysis of historical subway reliability and short-term delay forecasts would improve commuter decision-making.



\## Stakeholder \& User 



* Stakeholder/Decider: MTA communications team  
* End User: Commuters during rush hour (morning/evening) 
* Decision Point: When users choose a subway line before or during travel 



\## Useful Answer \& Decision  



* Type: Descriptive + Predictive 
* Metric: Average delay minutes, forecast accuracy (within 5 minutes)
* Artifact: 1-page slide summarizing reliability by line, Reproducible notebook that outputs expected delays during peak hours 



\## Assumptions \& Constraints - 



Assumptions:

* Historical delay data is available and reliable 
* Forecasting model can run daily with minimal compute needs 
* Privacy not a concern (aggregate transit data)



Constraints: real-time latency (must update quickly), data quality 



\## Known Unknowns / Risks 

* Alerts may be inconsistent or incomplete 
* External shocks (weather, strikes) may reduce forecast accuracy
* Limited access to MTA APIs or datasets could constrain scope 



\## Lifecycle Mapping  



Goal: Reduce commuter uncertainty through thr following: 

* Identify patterns in subway delays
* Build and evaluate forecasting models
* Communicate findings in a clear, structured way

&nbsp;

Deliverables: A cleaned and structured dataset of subway delay events, visual analyses of reliability patterns, and a forecasting notebook with performance evaluation. Final outputs include a concise report with line reliability and stakeholder memo

Stages:



* Data Collection: Gather subway delay data (e.g., MTA feeds, public datasets) and store it in +'/data/raw/'.  
* Data Cleaning \& Preprocessing: Handle missing or inconsistent alerts, standardize timestamps and determining delay times per lines
* Data Analysis: Calculate average delay minutes by line and by time of day and Visualize patterns with charts (daily/weekly reliability, rush-hour vs. off-peak, seasonal effect) 
* Modeling: Apply statistical models to forecast short-term delays. 
* Evaluation: Determine the level of accuracy by comparing predictions to actual outcomes  
* Reporting: Document findings and limitations.
* Stage :Data collection \& EDA 



\## Repo Plan :



/data/raw — historical subway alerts 

/data/processed — cleaned data for modeling 

/src/ — scripts for cleaning and forecasting 

/notebooks/ — Jupyter notebooks showing analysis done, descriptive trends, and forecasts  

/docs/ — stakeholder memo ( final report \& Slides) 



