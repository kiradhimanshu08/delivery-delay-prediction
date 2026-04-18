# 📊 Delivery Delay Prediction Model

> Predicting shipment delays using machine learning on logistics data.

---

## 🎯 Objective  
Predict whether a shipment will be delayed using real ERP logistics data.

---

## 🛠 Tech Stack  
- Python  
- Pandas  
- Scikit-learn  
- Logistic Regression  
- Decision Tree  

---

## 📁 Dataset  
- Real ERP logistics dataset  
- **Features:** Origin, Destination, Goods Type  
- **Target:** Delayed (0 = On-Time, 1 = Delayed)  

---

## ⚙️ Approach  
- Cleaned and preprocessed logistics data  
- Removed **data leakage** (`delay_days`)  
- Handled class imbalance using `class_weight='balanced'`  
- Trained and compared:
  - Logistic Regression  
  - Decision Tree  

---

## 📈 Results  
- Achieved ~80% accuracy  
- Improved detection of delayed shipments (**recall increased**)  
- Decision Tree performed better  

---

## 🔍 Key Insights  
- Certain destinations show higher delay probability  
- Location significantly impacts delivery timelines  
- Model helps identify high-risk shipments early  

---

## 💼 Business Impact  
- Enables proactive logistics planning  
- Helps reduce delivery delays  
- Supports data-driven decision-making  

---

## ▶️ How to Run  

```bash
pip install -r requirements.txt
python model.py

## 📊 Model Output
![Output](model_output.png)


