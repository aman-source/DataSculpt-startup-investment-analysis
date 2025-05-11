import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('data/cleaned_startups_v2.csv')

st.title("Predictive Insights")

df_ml = df[['funding_total_usd', 'funding_rounds', 'status']]
df_ml['status_binary'] = df_ml['status'].apply(lambda x: 1 if x == 'operating' else 0)

X = df_ml[['funding_total_usd', 'funding_rounds']]
y = df_ml['status_binary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)
preds = model.predict(X_test)

st.subheader("Startup Success Prediction")
st.write("Accuracy:", accuracy_score(y_test, preds))
st.write("Classification Report:")
st.text(classification_report(y_test, preds))

funding_input = st.number_input("Funding Amount (USD)", value=5000000)
rounds_input = st.number_input("Number of Funding Rounds", value=3)

prediction = model.predict([[funding_input, rounds_input]])

if st.button("Predict Success"):
    if prediction[0] == 1:
        st.success("High chance of startup operating successfully!")
    else:
        st.warning("Startup may not sustain long-term.")
