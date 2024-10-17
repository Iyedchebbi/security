import cv2

# Ouvrir la caméra
cap = cv2.VideoCapture(0)  # 0 est l'ID par défaut de la webcam

while True:
    ret, frame = cap.read()  # Lire l'image de la caméra
    
    if not ret:
        print("Impossible de lire la caméra")
        break

    # Afficher le flux vidéo
    cv2.imshow('Video Stream', frame)

    # Appuyez sur la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Relâcher la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
