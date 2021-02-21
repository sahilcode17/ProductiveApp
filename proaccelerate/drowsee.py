import os
import cv2
import dlib
from scipy.spatial import distance



def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear_aspect_ratio = (A+B)/(2.0*C)
    return ear_aspect_ratio


def drowsiness(path, hog_face_detector, dlib_facelandmark):
    print("enter drowsiness")
    frame = cv2.imread(path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    faces = hog_face_detector(gray)
    if(not faces):
        cv2.destroyAllWindows()
        return 0

    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        leftEye = []
        rightEye = []

        for n in range(36,42):
        	x = face_landmarks.part(n).x
        	y = face_landmarks.part(n).y
        	leftEye.append((x,y))
        	next_point = n+1
        	if n == 41:
        		next_point = 36
        	x2 = face_landmarks.part(next_point).x
        	y2 = face_landmarks.part(next_point).y
        	cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        for n in range(42,48):
        	x = face_landmarks.part(n).x
        	y = face_landmarks.part(n).y
        	rightEye.append((x,y))
        	next_point = n+1
        	if n == 47:
        		next_point = 42
        	x2 = face_landmarks.part(next_point).x
        	y2 = face_landmarks.part(next_point).y
        	cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)

        EAR = (left_ear+right_ear)/2
        EAR = round(EAR,2)
        if EAR<0.26:
            cv2.destroyAllWindows()
            return 0

    cv2.destroyAllWindows()
    # print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBbbb")
    return 1


def mainn():

    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor("C:/Users/Hp/Desktop/hackathon/ProductiveApp/proaccelerate/shape_predictor_68_face_landmarks.dat")
    os.chdir("C:/Users/Hp/Downloads")
    all_files = os.listdir()
    face_files = []
    count = 0
    for path in all_files:
        if(path.startswith("face")):
            face_files.append(path)
            count+= drowsiness(path,hog_face_detector, dlib_facelandmark)
    total = len(face_files)
    for i in face_files:
        os.remove(i)
    # print("CCCCCCCCCCCCSS")
    return (count/total)

