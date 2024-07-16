import cv2
from simple_facerec import SimpleFacerec
import os
import datetime
import face_recognition  # Import face_recognition module

# Encode faces from images
sf = SimpleFacerec()
sf.load_encoding_images("images/")

cap = cv2.VideoCapture(0)

def add_new_face(face_image, timestamp):
    filename = f"images/unknown_{timestamp}.jpg"
    cv2.imwrite(filename, face_image)
    print(f"Saved {filename}")

    new_name = input("Enter the name of the person: ")
    if new_name:
        new_filename = f"images/{new_name}.jpg"
        os.rename(filename, new_filename)
        print(f"Renamed {filename} to {new_filename}")

        try:
            # Add new encoding
            img = cv2.imread(new_filename)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_encodings = face_recognition.face_encodings(rgb_img)
            if len(img_encodings) > 0:
                img_encoding = img_encodings[0]
                sf.known_face_encodings.append(img_encoding)
                sf.known_face_names.append(new_name)
                print(f"Added new face encoding for {new_name}")
            else:
                print(f"Could not encode face for {new_name}. No face detected.")
        except Exception as e:
            print(f"Error encoding face for {new_name}: {e}")

while True:
    ret, frame = cap.read()

    # Detect faces
    face_locations, face_names = sf.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        top, right, bottom, left = face_loc
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)

    if key == 27:  # Esc key to exit
        break
    elif key == ord('n'):  # 'n' key to capture and save unknown face
        for face_loc, name in zip(face_locations, face_names):
            if name == "Unknown":
                top, right, bottom, left = face_loc
                face_image = frame[top:bottom, left:right]
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                add_new_face(face_image, timestamp)

cap.release()
cv2.destroyAllWindows()
