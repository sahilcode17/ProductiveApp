import os







def i():
    os.chdir("C:\Users\Hp\Downloads")
    all_files = os.listdir()
    face_files = []
    for i in lis:
        if(i.startswith("face")):
            face_files.append(i)
            drowsiness(i)


    map(face_files,os.remove)