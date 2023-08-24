import cv2
import easyocr
import pyttsx3
import threading

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def webcam_display():
    cap = cv2.VideoCapture(0)  

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Webcam Capture', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    
    reader = easyocr.Reader(lang_list=['en'], gpu=False)

    
    display_thread = threading.Thread(target=webcam_display)
    display_thread.start()

    while True:
        
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  
        ret, frame = cap.read()  

        if not ret:
            break

        detected_text = reader.readtext(frame)

        
        extracted_text = ' '.join([result[1] for result in detected_text])

        cap.release()  

        if extracted_text.strip():
            
            text_to_speech(extracted_text)

    display_thread.join()

if __name__ == "__main__":
    main()
