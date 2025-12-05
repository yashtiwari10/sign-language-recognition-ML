import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# ---- FIX CAMERA FOR WINDOWS ----
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Could not open camera with CAP_DSHOW. Trying alternative backends...")
    cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

if not cap.isOpened():
    cap = cv2.VideoCapture(0, cv2.CAP_VFW)

if not cap.isOpened():
    print("❌ No camera detected on index 0. Exiting.")
    exit()
else:
    print("✅ Camera opened successfully!")
# --------------------------------

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {j}')

    # Wait for user to press "q" to start capturing
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️  Failed to read frame from camera. Exiting.")
            cap.release()
            cv2.destroyAllWindows()
            exit()

        cv2.putText(frame, 'Ready? Press "Q" to start capturing', (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("⚠️  Failed to read frame during capture. Exiting.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        img_path = os.path.join(class_dir, f'{counter}.jpg')
        cv2.imwrite(img_path, frame)

        counter += 1
        print(f"Captured {counter}/{dataset_size} for class {j}", end='\r')

cap.release()
cv2.destroyAllWindows()
print("\n✅ Dataset collection complete.")
