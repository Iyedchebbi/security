import cv2
from simple_facerec import SimpleFacerec

# Encoder les visages à partir du dossier d'images
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Ouvrir la caméra
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Détecter les visages
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    # Afficher le flux vidéo
    cv2.imshow("Camera", frame)

    # Appuyez sur 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Relâcher la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
