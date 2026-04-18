import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# STEP 1: Load Data
# -----------------------------
data = pd.read_excel(r"D:\HIMANSHU\Research project\Data\Jan-Dec 2025 data.xlsx")

# -----------------------------
# STEP 2: Clean Column Names
# -----------------------------
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[()/-]", "", regex=True)

print("Columns:", data.columns)

# -----------------------------
# STEP 3: Create Target Variable
# -----------------------------
# delayed = 1 if delay_days > 0 else 0
data['delayed'] = data['delay_days'].apply(lambda x: 1 if x > 0 else 0)

# -----------------------------
# STEP 4: Select Features (NO LEAKAGE)
# -----------------------------
# ❌ DO NOT use delay_days as feature
data = data[['origin', 'destination', 'goods_type', 'delayed']]

# -----------------------------
# STEP 5: Convert Categorical → Numeric
# -----------------------------
data = pd.get_dummies(data, columns=['origin', 'destination', 'goods_type'], drop_first=True)

# -----------------------------
# STEP 6: Define Features & Target
# -----------------------------
X = data.drop(columns=['delayed'])
y = data['delayed']

# -----------------------------
# STEP 7: Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# -----------------------------
# STEP 8: Train Model
# -----------------------------
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# -----------------------------
# STEP 9: Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# STEP 10: Evaluation
# -----------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# STEP 11: Feature Importance
# -----------------------------
importance = pd.DataFrame({
    'Feature': X.columns,
    'Impact': model.coef_[0]
}).sort_values(by='Impact', ascending=False)

print("\nTop Factors Influencing Delay:\n", importance.head(10))