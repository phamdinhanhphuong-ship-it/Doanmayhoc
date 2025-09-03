import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load và chuẩn bị dữ liệu
@st.cache_data
def load_data():
    # Tải dataset và bỏ cột index nếu có
    data = pd.read_csv("HepatitisC  Liver (đã edit).csv", index_col=None)
    
    # Xóa cột đầu tiên (cột thứ tự)
    data = data.drop(data.columns[0], axis=1)
    
    # Xử lý cột Category và Sex
    data['Category'] = pd.to_numeric(data['Category'].replace(
        {'Blood Donor': 0, 'suspect Blood Donor': 1, 'Hepatitis': 2, 'Fibrosis': 3, 'Cirrhosis': 4}),
        errors='coerce')
    data['Sex'] = data['Sex'].replace({'M': 0, 'F': 1}).astype(bool)

    # Điền giá trị thiếu bằng trung bình
    data.fillna(data.mean(), inplace=True)
    return data

data = load_data()

# Chuẩn bị dữ liệu
X = data.drop('Category', axis=1)
y = data['Category']

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, shuffle=True)

# Huấn luyện các mô hình
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X_train, y_train)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Tạo giao diện Streamlit
st.title("Chẩn đoán bệnh viêm gan C")

# Nhập các thông số
age = st.number_input("Age", min_value=0, max_value=100, value=30, step=1)
sex = st.selectbox("Sex", options=["M", "F"])
alb = st.number_input("Albumin (ALB)", min_value=0.0, value=40.0)
alp = st.number_input("Alkaline Phosphatase (ALP)", min_value=0.0, value=85.0)
alt = st.number_input("Alanine Transaminase (ALT)", min_value=0.0, value=20.0)
ast = st.number_input("Aspartate Transaminase (AST)", min_value=0.0, value=20.0)
bil = st.number_input("Bilirubin (BIL)", min_value=0.0, value=1.0)
che = st.number_input("Cholinesterase (CHE)", min_value=0.0, value=7.0)
chol = st.number_input("Cholesterol (CHOL)", min_value=0.0, value=200.0)
crea = st.number_input("Creatinine (CREA)", min_value=0.0, value=1.0)
ggt = st.number_input("Gamma-Glutamyl Transferase (GGT)", min_value=0.0, value=50.0)
prot = st.number_input("Protein (PROT)", min_value=0.0, value=70.0)

# Xử lý đầu vào
sex = 1 if sex == "F" else 0  # Mã hóa giới tính
input_data = np.array([[age, sex, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot]])
input_data_scaled = scaler.transform(input_data)

# Dự đoán khi nhấn nút Predict
if st.button('Dự đoán'):
    # Dự đoán với 3 mô hình
    svm_prediction = svm_model.predict(input_data_scaled)[0]
    dt_prediction = decision_tree_model.predict(input_data_scaled)[0]
    knn_prediction = knn_model.predict(input_data_scaled)[0]
    
    # Tính toán accuracy cho các mô hình
    svm_accuracy = svm_model.score(X_test, y_test) * 100
    dt_accuracy = decision_tree_model.score(X_test, y_test) * 100
    knn_accuracy = knn_model.score(X_test, y_test) * 100

    # Hiển thị kết quả cho từng mô hình trong 3 cột
    categories = {0: "Blood Donor", 1: "Suspect Blood Donor", 2: "Hepatitis", 3: "Fibrosis", 4: "Cirrhosis"}

    # Messages based on the prediction
    def get_health_message(prediction):
        if prediction == 0:  # Blood Donor
            return "Bạn là người hiến máu, không có bệnh."
        elif prediction == 1:  # Suspect Blood Donor
            return "Bạn là người nghi ngờ hiến máu, cần kiểm tra thêm."
        elif prediction == 2:  # Hepatitis
            return "Bạn có thể bị viêm gan. Cần đến bệnh viện kiểm tra thêm."
        elif prediction == 3:  # Fibrosis
            return "Bạn có thể bị xơ gan. Cần tham khảo ý kiến bác sĩ."
        elif prediction == 4:  # Cirrhosis
            return "Bạn có thể bị xơ gan nặng. Cần điều trị và theo dõi thường xuyên."
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Mô hình SVM")
        st.write(f"Chẩn đoán: **{categories[svm_prediction]}**")
        st.write(f"Độ chính xác: **{svm_accuracy:.2f}%**")
        st.write(get_health_message(svm_prediction))

    with col2:
        st.subheader("Mô hình Cây Quyết Định")
        st.write(f"Chẩn đoán: **{categories[dt_prediction]}**")
        st.write(f"Độ chính xác: **{dt_accuracy:.2f}%**")
        st.write(get_health_message(dt_prediction))

    with col3:
        st.subheader("Mô hình KNN")
        st.write(f"Chẩn đoán: **{categories[knn_prediction]}**")
        st.write(f"Độ chính xác: **{knn_accuracy:.2f}%**")
        st.write(get_health_message(knn_prediction))
