
import cv2
import face_recognition

# Initialize video capture
cap = cv2.VideoCapture(0)

# List to store face encodings of already captured faces
captured_faces_encodings = []

# Counter for screenshots
counter = 0

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Convert the frame from BGR to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            # Check if this face is already captured
            matches = face_recognition.compare_faces(captured_faces_encodings, face_encoding, tolerance=0.6)

            if not any(matches):
                # If no match found, this is a new face
                captured_faces_encodings.append(face_encoding)
                cv2.imwrite(f'C:\\Users\\CHIJINDU\\Desktop\\newface\\screenshot{counter}.png', frame)
                counter += 1

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()


'''HOW IT WORKS
Key Points:
Face Recognition:
The face_recognition library detects and encodes faces in the frame.
Each face is converted into a 128-dimensional vector (encoding) that uniquely represents the face.

Checking for Matches:

The compare_faces function compares the encoding of a newly detected face with the encodings
of faces that have already been captured. The tolerance parameter controls the sensitivity;
lower values mean stricter matching.

Capturing New Faces:

If the newly detected face doesn't match any stored encodings,
it is considered "new," and its encoding is stored, and a screenshot is taken.
Notes:
Tolerance Value: Adjust the tolerance value based on your application's needs.
A lower tolerance is more strict and will only match faces that are very similar.
Performance Consideration: This method requires more processing power than simple face detection since
it involves calculating and comparing face encodings.
By following this approach, the system will only take a screenshot the first time it
encounters a new face, avoiding duplicate screenshots of the same face.'''
