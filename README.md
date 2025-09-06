


### Giới thiệu 

Đề tài của báo cáo là **“Xây dựng mô hình chẩn đoán bệnh viêm gan C bằng các thuật toán máy học”**.
Trong bối cảnh hiện nay, bệnh **viêm gan C** là một trong những vấn đề y tế toàn cầu, có thể dẫn đến các biến chứng nghiêm trọng như xơ gan và ung thư gan. Việc phát hiện và chẩn đoán sớm đóng vai trò cực kỳ quan trọng để nâng cao hiệu quả điều trị và cải thiện chất lượng cuộc sống cho bệnh nhân.

Mục tiêu của đề tài là **ứng dụng các phương pháp học máy** để xây dựng một mô hình có khả năng **dự đoán nguy cơ mắc bệnh viêm gan C** dựa trên **dữ liệu y tế** của bệnh nhân. Dữ liệu bao gồm nhiều chỉ số sinh hóa và thông tin sức khỏe, chẳng hạn như:

* Tuổi, giới tính
* Các enzyme gan (ALT, AST, ALP, GGT)
* Protein (ALB, PROT, CHE)
* Bilirubin, Cholesterol, Creatinine

Các bước chính của nghiên cứu:

1. **Tiền xử lý dữ liệu**: làm sạch dữ liệu, xử lý giá trị thiếu, ngoại lai, chuẩn hóa đặc trưng.
2. **Xây dựng mô hình**: thử nghiệm 3 thuật toán phổ biến là **Support Vector Machine (SVM)**, **Decision Tree** và **Random Forest**.
3. **Đánh giá kết quả**: so sánh hiệu quả của các mô hình bằng các chỉ số Accuracy, Precision, Recall, F1-score.
4. **Triển khai ứng dụng**: tích hợp mô hình vào **Streamlit** để xây dựng một công cụ dự đoán trực quan.

Kết quả cho thấy:

* **Decision Tree** đạt độ chính xác rất cao (≈99%),
* **Random Forest** có khả năng tổng quát tốt (≈95%),
* **SVM** hoạt động khá ổn định (≈90%) nhưng kém hơn hai mô hình còn lại.

Đề tài không chỉ giúp người học rèn luyện kỹ năng xử lý dữ liệu và xây dựng mô hình học máy, mà còn cho thấy **tiềm năng ứng dụng Machine Learning trong lĩnh vực y tế**, hỗ trợ bác sĩ và bệnh viện trong việc sàng lọc, chẩn đoán sớm bệnh viêm gan C.


