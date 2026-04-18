📊 Delivery Delay Prediction Model

🔹 Objective
To predict whether a shipment will be delayed using logistics data and machine learning models.

🔹 Tech Stack
Python
Pandas
Scikit-learn
Logistic Regression
Decision Tree

🔹 Dataset
Real ERP logistics dataset
Features used:
Origin
Destination
Goods Type
Target:
Delayed (0 = On-Time, 1 = Delayed)

🔹 Approach
Cleaned and preprocessed raw logistics data
Removed data leakage (excluded delay_days from features)
Handled class imbalance using class_weight='balanced'
Trained and compared:
Logistic Regression
Decision Tree

🔹 Results
Achieved ~80% accuracy
Improved detection of delayed shipments (recall increased)
Decision Tree performed better for delay prediction

🔹 Key Insights
Certain destinations show higher delay probability
Location-based patterns significantly impact delivery timelines
Model helps identify high-risk shipments early

🔹 Business Impact
Enables proactive logistics planning
Helps reduce delivery delays
Supports data-driven decision making in supply chain operations

🔹 How to Run
pip install -r requirements.txt
python model.py
