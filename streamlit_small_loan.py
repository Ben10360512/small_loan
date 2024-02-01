import streamlit as st
import joblib
import numpy as np

st.write("# Small Loan Prediction")

col1, col2, col3 = st.columns(3)

age = col1.number_input("年齡:")
sex = col2.selectbox("性別:", ["M", "F"])
region = col3.selectbox("地區:", ["INNER_CITY", "TOWN", "SUBURBAN", "RURAL"])
income = col1.number_input("收入:")
married = col2.selectbox("是否結婚?", ["YES", "NO"])
children = col3.selectbox("小孩個數?", [0, 1, 2, 3])
car = col1.selectbox("是否有車?", ["YES", "NO"])
save_act = col2.selectbox("是否有活儲帳戶?", ["YES", "NO"])
current_act = col3.selectbox("是否有支存帳戶?", ["YES", "NO"])
mortgage = col1.selectbox("是否有房貸?", ["YES", "NO"])

input_data = np.array([[age, sex, region, income, married, children, car, save_act, current_act, mortgage]])

# 使用模型進行預測
prediction = model.predict(input_data)
prediction_prob = model.predict_proba(input_data)

# 養成使用st.button的習慣，這樣將更方便與互動
if st.button('預測'):
    if prediction[0] == 0:
        st.write('<p class="big-font">此人對小額信貸<font color="red">沒有興趣</font>.</p>', unsafe_allow_html=True)
    else:
        st.write('<p class="big-font">此人對小額信貸<font color="blue">有興趣</font>.</p>', unsafe_allow_html=True)

    # 以表格形式顯示機率分數
    st.table(pd.DataFrame(prediction_prob, columns=["沒有興趣", "有興趣"]))
