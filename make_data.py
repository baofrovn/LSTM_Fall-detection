import cv2
import mediapipe as mp
import pandas as pd

# Đọc ảnh từ webcam
cap = cv2.VideoCapture('Stand-20240602T124953Z-001/Stand/istockphoto-827423352-640_adpp_is.mp4')
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 10
# Khởi tạo thư viện mediapipe
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

lm_list = []
label = "STAND3"

def make_landmark_timestep(results):
    print(results.pose_landmarks.landmark)
    c_lm = []
    for id, lm in enumerate(results.pose_landmarks.landmark):
        c_lm.append(lm.x)
        c_lm.append(lm.y)
        c_lm.append(lm.z)
        c_lm.append(lm.visibility)
    return c_lm

for i in range(frame_count):
    ret, frame = cap.read()
    if ret:
        # Nhận diện pose
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frameRGB)

        if results.pose_landmarks:
            # Ghi nhận thông số khung xương
            lm = make_landmark_timestep(results)
            lm_list.append(lm)
            
        cv2.imshow("image", frame)
        if cv2.waitKey(1) == ord('q'):
            break


# Write vào file csv


# df1  = pd.DataFrame(lm_list) # Adjust the path if necessary
# df2 = pd.read_csv(label + ".txt")  # Adjust the path if necessary
# merged_df = pd.concat([df1, df2])
# with open(label + ".txt", 'w') as file:
#     pass  
# merged_df.to_csv(label + ".txt", index=False)
# cap.release()
# cv2.destroyAllWindows()
df  = pd.DataFrame(lm_list)
df.to_csv(label + ".txt")
cap.release()
cv2.destroyAllWindows()
