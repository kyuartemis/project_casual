import cv2

# เปิดการเชื่อมต่อกับกล้อง
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ไม่สามารถเปิดกล้องได้")
    exit()

while True:
    # อ่านภาพจากกล้อง
    ret, frame = cap.read()
    
    if not ret:
        print("ไม่สามารถรับภาพจากกล้องได้")
        break

    # แสดงภาพ
    cv2.imshow('กล้อง', frame)

    # กด 'q' เพื่อออกจากการแสดงผล
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดการเชื่อมต่อกับกล้อง
cap.release()
cv2.destroyAllWindows()