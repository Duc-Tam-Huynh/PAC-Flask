import requests

# Gửi yêu cầu POST đến API với dữ liệu đầu vào
response = requests.post('http://127.0.0.1:5000/predict_api', json={'nhietDo': 1, 'pH': 2, 'doDuc':1,'doMau':1, 'chatLoLung':1, 'doDan':1 })

# Kiểm tra mã trạng thái của phản hồi
if response.status_code == 200:
    # Dự đoán được trả về trong body của phản hồi
    prediction = response.json()

    # In dự đoán ra màn hình
    print(prediction)
    print(f'{prediction:.2f}')


else:
    # Có lỗi xảy ra
    print(response.status_code)
