# Web Traffic Prediction for Enhanced Ad Revenue
![Header image](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/132069152/6261c761-b7f6-4f29-bdbd-675a1df9a2e2)

Jambojet, strives to optimize its advertising spaces to maximize revenue and advertiser satisfaction. The unpredictable nature of web traffic patterns poses a significant challenge and hindered effective ad placement, leading to missed revenue opportunities and decreased advertiser satisfaction. Our project aims to revolutionize ad placement strategies through advanced Time Series Forecasting.

You can test our deployed app using this link https://web-traffic-prediction.streamlit.app/

# Data Collection:
We will utilize data that simulates the web traffic behaviours of a websites such as www.jambojet.com taking into account their marketing campaigns, travel restrictions and other industry factors that may affect web traffic.

To do such a project you can use scraping techniques to extract real-time time series data from Google Analytics, ensuring accuracy and relevance for forecasting models within the context of total and new users per day.

## Dataset Overview: 
This dataset captures daily fluctuations in user engagement, essential for precise forecasting and ad optimization. 

## Data Features
The dataset includes variables such as **total users**, **new users**, **time stamps**, and **travel-related indicators**. 
These features enable a granular analysis of daily user patterns, essential for understanding travel-specific behaviours.

## Success Criteria: Metric for Success: 
Root Mean Squared Error (RMSE) This metric serves as a robust measure to evaluate the accuracy of our time series forecasting models, specifically focusing on predicting daily total users and new users. The significance of achieving a low RMSE lies in its ability to reflect the precision of our forecasting models.

Achieving a low RMSE aligns with the broader goal of contributing to the sustainable development of Jambojet's online advertising ecosystem. By providing precise forecasts, the project facilitates strategic decision-making, ensuring that resources are efficiently allocated to enhance the user experience and sustain a thriving advertising platform.

## Project Structure
1. Exploratory Data Analysis
2. Data Preprocessing for Modelling
3. Modelling
4. Model Evaluation
5. Deployment

## Exploratory Data Analysis
### Effects of Promotions and Announcements
![promotions](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/133201112/844006eb-2a73-42c5-ae74-16d0533b8ceb)
Promotional events triggering substantial spikes in user engagement on Jambojet's website. Notable instances include a 72-hour special fare in April 2018, resulting in the highest recorded traffic, a 35% discount promotion in August 2018 correlating with a significant spike, and a February 2019 anniversary promotion leading to increased activity throughout the month. Additionally, the sale of 100 tickets for KES 50 each in April 2019, initiation of flights to Kigali in November 2019, and a New Year's sale in January 2020 marked key moments of heightened web traffic. Collaborations with Cellulant in November-December 2021 and June 2022, introducing incentive programs, further contributed to increased user engagement. These findings showcase the effectiveness of promotional efforts in driving Jambojet's web traffic.

### Effects of Covid-19
![covid impact](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/133201112/534e3228-85d2-4e46-868b-cd55f2833da2)
The COVID-19 pandemic significantly impacted Jambojet's web traffic and operations as travel bans and restrictions led to a decline in user engagement and flights. Key moments include the initial restrictions announced in March 2020, resulting in a notable decline in website visitors. The subsequent intensification of measures in April 2020, including a movement cessation and curfew, further contributed to decreased user traffic. May recorded the lowest user numbers during this period. However, with the easing of restrictions in July 2020, especially the resumption of air travel, there was a remarkable upswing in web traffic, showcasing a positive trend that continued in the following months. Nevertheless, the airline faced challenges again in March 2021 with the temporary suspension of operations due to renewed restrictions, leading to a spike in website visits followed by a decline as the impact of COVID-19 persisted.

### Effects of Public and School Holidays
![yearly trend](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/133201112/4d50b147-f174-4139-8c60-b1b55ba6a3c9)
Analyzing Jambojet's web traffic, it is evident that the highest spikes in 'Simulated_Users' and 'New_Simulated_Users' consistently occur during the Winter season, particularly in December. Notable peaks were observed during public and school holidays in 2018, 2019, and 2020, showcasing a pattern of increased engagement during this time. Despite the challenges posed by the COVID-19 pandemic, signs of recovery were evident in the Winter months of 2020, aligning with the December holidays. In 2021, a general upward trend in web traffic followed the lifting of travel restrictions in May, with notable spikes in September and throughout the holiday season. The highest levels of web traffic in 2022 were observed from June to August, aligning with the resumption of international tourism. Over a six-year period, Winter consistently attracted the highest web traffic, followed by Autumn and Summer, aligning with broader travel patterns in the country. The findings suggest a strong correlation between promotions, increased travel interest, and heightened web traffic during Autumn and Winter seasons.

## Results
### Baseline Model
![Baseline model](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/133201112/34b96d47-d0a5-4ea8-911a-86c842e5138a)

The baseline ARIMA model with parameters (2,0,0) demonstrates a relatively low Test Data RMSE (Root Mean Squared Error) of 0.5977. While this value signifies reasonable accuracy in predicting the test data, it's important to note that it is not the lowest among the models considered. 

### Auto ARIMA
![AutoARIMA](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/133201112/22361341-ef90-4b52-97ab-75835962acb3)

The auto ARIMA model outperformed the baseline ARIMA model, as indicated by the lower Test Data RMSE of 0.3687 compared to 0.5977 for the baseline model. The auto ARIMA model, fitted using the pmdarima package, utilizes an automated process to determine the best ARIMA model, resulting in a more accurate fit to the data. The significantly lower RMSE suggests improved performance and better predictive capabilities with the auto ARIMA model relative to the baseline ARIMA model with parameters (2,0,0).

### SARIMA Model
![SARIMA Model](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/133201112/4b8fbae9-c94f-4582-a61f-8c4c9246c293)

The SARIMA model outperformed the Auto ARIMA model, as evidenced by the lower Test Data RMSE of 0.3272. The SARIMA model incorporates seasonal components, allowing it to capture and model the seasonal patterns in the data more effectively. The reduced RMSE indicates that the SARIMA model provides a better fit to the data, resulting in improved predictive performance compared to the automated Auto ARIMA approach.

### Facebook Prophet
![Facebook Prophet](https://github.com/Mwenda-Mugambi/Web_Ad_campaign_optimization/assets/133201112/6b77bb6f-28bd-40fe-b963-19a5953044d2)

The Facebook Prophet model surpasses even the SARIMA, achieving the lowest Test Data RMSE of 0.2966. This indicates that the Facebook Prophet model, developed by Facebook's Core Data Science team, is the best-performing model among those evaluated. The lower RMSE value suggests that the Facebook Prophet model provides a more accurate forecast and a superior fit to the given data, making it a preferred choice for forecasting in this context.

## Conclusion
Among the evaluated models, the Facebook Prophet model (Model 5) emerges as the most accurate, as evidenced by its lower RMSE values. This suggests that Prophet is well-adapted for forecasting the simulated user data in this specific scenario, outperforming not only traditional ARIMA and SARIMA models but also the auto ARIMA approach.

## Business Recommendations
1. **Leverage Facebook Prophet Model for Forecasting:** Implement the Facebook Prophet model for web traffic predictions, considering its lowest RMSE, indicating high accuracy. Use forecasts to anticipate peak web traffic periods, enabling dynamic ad placement and pricing strategies.

2. **Marketing and Communication Strategy:** Enhance communication around promotional events to drive web traffic by:
 - **Calendar Integration:** Align marketing efforts with Jambojet's event calendar, focusing on peak travel periods, holidays, and special occasions.
 - **Advance Planning:** Plan campaigns well in advance to build anticipation and awareness.
 - **Utilize Social Media and Email Marketing:** Alert potential customers to upcoming deals and promotions using social media and email marketing to boost web traffic during predicted low seasons.

3. **Promotion and Event-Driven Marketing:** Align ad campaigns with promotional events and peak travel periods (e.g., school holidays, public holidays, special fare promotions) to maximize engagement. Develop partnerships with tourism boards and travel agencies for joint promotions and implement real-time marketing strategies like flash sales during high traffic periods.

4. **Segmentation and Targeted Advertising:** Use segmentation analysis to understand different user groups (e.g., new users vs. returning, domestic vs. international travelers). Tailor dynamic ads to these segments, offering relevant and personalized promotions. For example, during the winter period, customize ads for international travelers.

5. **Advertiser Dashboard and Real-Time Insights:** Introduce an advertiser dashboard providing real-time insights into ad performance, web traffic patterns, and ROI metrics. Enable advertisers to adjust campaigns in real-time based on data-driven insights.

6. **Enhancing User Experience:** Optimize the website for user experience, especially during predicted high traffic periods, to prevent slowdowns or crashes. Integrate user feedback to improve the website and advertising experience.

7. **Dynamic Ad Space Pricing:** Develop a dynamic pricing strategy aligned with seasonality trends to maximize revenue. Implement premium prices during high seasons and adjust pricing based on demand.

8. **Response to External Factors:** Monitor external factors like travel restrictions or economic changes impacting web traffic. Adjust strategies accordingly and develop contingency plans for sudden changes in travel patterns due to global events, such as a pandemic.

## Recommendations for Future Modeling

1. **Adapting to Future Trends with Log Transformation:** Consider employing log transformation to stabilize variance for outliers. As data trends evolve, especially with increasing visitors to the Jambojet website, the model should dynamically adapt to these changes. Implement methods to identify and adjust for shifts in data distribution, ensuring continued accuracy and relevance in the analysis.

2. **Utilizing the Facebook Prophet Model:** Prioritize the use of the Facebook Prophet model for time series forecasting. Its capability to handle various seasonality patterns and holiday effects makes it well-suited for predicting web traffic. Leverage advanced features like automatic trend and seasonality detection for accurate forecasting. However, it's advisable to compare its performance with other models to validate its suitability for Jambojet's specific data and forecasting requirements.

3. **Continuous Monitoring of Exponential Trends and Seasonality:** Identify and monitor exponential trends and annual seasonality in the user data continuously. This proactive approach allows for timely adjustments in forecasting models, ensuring their relevance and accuracy amidst evolving market conditions and data trends. Regular updates and revisions based on ongoing data analysis will contribute to sustained predictive accuracy.

4. **Continuous Monitoring and Optimization:** Regularly review and optimize forecasting models with updated data. Conduct A/B testing on different ad placements and formats to refine the advertising strategy continually. For Jambojet, focus on improving key metrics such as click-through rates (CTR), maximizing ad revenue, and enhancing user engagement with ads. Implement A/B testing with different versions to identify the most effective elements, ensuring a data-driven approach to advertising optimization.
