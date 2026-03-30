import cv2
import face_recognition
import pickle
import threading
import time

# --- 1. The Background Camera Thread ---
class WebcamStream:
    def __init__(self):
        self.stream = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        threading.Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped: return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

# --- 2. Setup Data ---
data = pickle.loads(open("encodings.pickle", "rb").read())
vs = WebcamStream().start()
time.sleep(1.0) # Let the camera warm up

face_locations = []
face_names = []
last_processed_time = 0

while True:
    frame = vs.read()
    
    # --- 3. Process every 0.5 seconds to keep CPU cool ---
    # This makes the boxes follow you slightly slower, but the VIDEO stays 33 FPS
    if time.time() - last_processed_time > 0.5:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        face_locations = face_recognition.face_locations(rgb_small_frame, model="cnn")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(data["encodings"], face_encoding)
            name = "Unknown"
            if True in matches:
                # Basic matching logic
                first_match_index = matches.index(True)
                name = data["names"][first_match_index]
            face_names.append(name)
        
        last_processed_time = time.time()

    # --- 4. Draw the boxes ---
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4; right *= 4; bottom *= 4; left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Smooth Unlock", frame)
    if cv2.waitKey(15) & 0xFF == 27: break

vs.stop()
cv2.destroyAllWindows()