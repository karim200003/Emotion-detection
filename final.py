from tkinter import *
from tensorflow.keras.models import model_from_json
from tkinter import messagebox
import mysql.connector
import tkinter
import customtkinter
import tkinter as tk
from sklearn import metrics
from PIL import Image, ImageTk
import numpy as np
import cv2
from tkinter import filedialog
import ctypes
##page de creation d'un compte

def open_sign_up_page():
    sign_up_window = customtkinter.CTk()
    window_width = 1280
    window_height = 720
    screen_width = sign_up_window.winfo_screenwidth()
    screen_height = sign_up_window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    sign_up_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    sign_up_window.title('Sign Up')

    def sign_up_window_DE():
        if (entry.get() == '' or entr2.get() == '' or entr3.get() == '' or entr4.get() == ''):
            messagebox.showerror("sign_up faild", "remplir tous les champs")
        elif (entr3.get() != entr4.get()):
            messagebox.showerror("sign_up faild", "la vérification du mot de passe est incorrecte")
        else:
            if (ajouter_utilisateur(entry.get(), entr3.get(),entr2.get())) == True:
                sign_up_window.destroy()

    sign_up_window = customtkinter.CTk()
    sign_up_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    sign_up_window.title('Sign Up')
    sign_up_window.iconbitmap("icon_kR0_icon.ico")

    # Add widgets for the sign-in page
    # You can customize this part to add your sign-in form
    sign_in_label = customtkinter.CTkLabel(master=sign_up_window, text="", font=('Century Gothic', 20))
    sign_in_label.pack()
    # img = ImageTk.PhotoImage(Image.open("pattern.png"))
    # l = customtkinter.CTkLabel(master=sign_up_window, image=img)
    # l.pack()

    # creating custom frame
    frame1 = customtkinter.CTkFrame(master=sign_up_window, width=420, height=560, corner_radius=15)
    frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l = customtkinter.CTkLabel(master=frame1, text="Create your Account", font=('Century Gothic', 20))
    l.place(x=100, y=45)

    entry = customtkinter.CTkEntry(master=frame1, width=320, height=50, placeholder_text='  Username')
    entry.place(x=50, y=140)

    entr2 = customtkinter.CTkEntry(master=frame1, width=320, height=50, placeholder_text='  Email')
    entr2.place(x=50, y=220)

    entr3 = customtkinter.CTkEntry(master=frame1, width=320, height=50, placeholder_text='  Password', show="*")
    entr3.place(x=50, y=300)

    entr4 = customtkinter.CTkEntry(master=frame1, width=320, height=50, placeholder_text='  Confirm Password', show="*")
    entr4.place(x=50, y=380)

    button4 = customtkinter.CTkButton(master=frame1, width=320, height=40, text="Sign up", fg_color='#e8b000',
                                      command=sign_up_window_DE, corner_radius=6, font=('', 18))
    button4.place(x=50, y=480)
    # Run the sign-in window
    sign_up_window.mainloop()

##page de login

def login():
    app = customtkinter.CTk()  # creating cutstom tkinter window
    window_width = 1280
    window_height = 720
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    app.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    app.title('Login')
    app.iconbitmap("icon_kR0_icon.ico")
    def login_action():
        username = username_entry.get()
        password = password_entry.get()

        if check_credentials(username, password):
            app.destroy()
            main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")

    img1 = ImageTk.PhotoImage(Image.open("pattern1.png"))
    l1 = customtkinter.CTkLabel(master=app, image=img1)
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, width=420, height=480, corner_radius=15)
    frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
    l2.place(x=100, y=45)

    username_entry = customtkinter.CTkEntry(master=frame, width=320, height=50, placeholder_text='Username')
    username_entry.place(x=50, y=140)

    password_entry = customtkinter.CTkEntry(master=frame, width=320, height=50, placeholder_text='Password', show="*")
    password_entry.place(x=50, y=215)

    l3 = customtkinter.CTkLabel(master=frame, text="Forget password?", font=('Century Gothic', 12))
    l3.place(x=255, y=290)

    button1 = customtkinter.CTkButton(master=frame, width=320, height=40, text="Login", command=login_action,
                                      fg_color='#e8b000', corner_radius=6, font=('', 18))
    button1.place(x=50, y=350)
    button2 = customtkinter.CTkButton(master=frame, width=120, height=40, text="sign up", command=open_sign_up_page,
                                      corner_radius=6, font=('', 18))
    button2.place(x=150, y=410)

    app.mainloop()


##fonction de verification de login

def check_credentials(username, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="pfe"
        )

        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            return True  # Credentials are valid
        else:
            return False  # Credentials are invalid

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
        return False


##fonction pour ajouter un utilisateur

def ajouter_utilisateur(username, password, email):
    # Connexion à la base de données MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="pfe"
    )
    cursor = conn.cursor()

    # Vérifier si l'utilisateur existe déjà
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        messagebox.showerror("sign_up faild", "l'utilisateur est deja existe")
        return False
    else:
        cursor.execute("INSERT INTO users (username, password,email) VALUES (%s, %s,%s)", (username, password,email))
        conn.commit()
        messagebox.showinfo("succès", "succès")
        return True
    conn.close()



def main_app():
    

    w = customtkinter.CTk()
    window_width = 1280
    window_height = 720
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    w.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    w.title('Welcome')

    def vid_mode():
        def withraw():
          img.withdraw()
          w.iconify()
        w.deiconify()
        def load_model(model_path, weights_path):
            with open(model_path, 'r') as json_file:
                loaded_model_json = json_file.read()
                loaded_model = model_from_json(loaded_model_json)
                loaded_model.load_weights(weights_path)
            return loaded_model

        # Load Haarcascade frontalface
        def load_haarcascade():
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            return face_cascade

        # Map emotion labels to human-readable names
        EMOTIONS_LIST = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

        # Detect emotions in a video
        def detect_emotions(video_path, model, face_cascade):
            cap = cv2.VideoCapture(video_path)

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=4, minSize=(20,20))
                #cv2.rectangle(frame, (290, 70), (0, 0), (204, 102, 0), cv2.FILLED)
                for (x, y, w, h) in faces:
                    face_roi = gray[y:y + h, x:x + w]
                    face_roi = cv2.resize(face_roi, (48, 48))
                    face_roi = np.expand_dims(face_roi, axis=0)
                    face_roi = np.expand_dims(face_roi, axis=-1)
                    emotion = model.predict(face_roi)
                    emotion_label = EMOTIONS_LIST[np.argmax(emotion)]

                    # Draw rectangle around face
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (204, 102, 0), 4)

                    cv2.putText(frame, f"{emotion_label}", (x+5, y+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (204, 102, 0), 2, cv2.LINE_AA)

                cv2.imshow("Emotion Detection", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        # Create a simple GUI
        def select_video():
            file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
            if file_path:
                model_path = "model_a.json"
                weights_path = "modelkarim.weights.h5"
                model = load_model(model_path, weights_path)
                face_cascade = load_haarcascade()
                detect_emotions(file_path, model, face_cascade)

        img = customtkinter.CTk()
        window_width = 1280
        window_height = 720
        screen_width = img.winfo_screenwidth()
        screen_height = img.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        img.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        img.title('Video mode')
        img.iconbitmap("icon_kR0_icon.ico")
        l1 = customtkinter.CTkLabel(master=img, text="Video mode", font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        fr = customtkinter.CTkFrame(master=img, width=720, height=450, corner_radius=15)
        fr.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        back= customtkinter.CTkButton(master=img, width=100, height=60, text="home", compound=tk.TOP,
                                         corner_radius=15, font=('Century Gothic', 25),command=withraw)
        back.place(relx=0.07, rely=0.07)
        botona = customtkinter.CTkButton(master=img, width=100, height=60, text="Upload", compound=tk.TOP,
                                         corner_radius=15, font=('', 25), command=select_video)
        botona.place(relx=0.47, rely=0.85)
        img.mainloop()

    def live_mode():
        
        def start():
            emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

            def load_model(json_file, weights_file):
                with open(json_file,"r") as file:
                    loaded_model_json = file.read()
                    model = model_from_json(loaded_model_json)

                model.load_weights(weights_file)
                model.compile(optimizer ='adam', loss='categorical_crossentropy', metrics = ['accuracy'])

                return model

            emotion_model = load_model('model_a.json', 'modelkarim.weights.h5')


            cap = cv2.VideoCapture(0)
            while True:
                # Find haar cascade to draw bounding box around face
                ret, frame = cap.read()
                frame = cv2.resize(frame, (1280, 720))
                if not ret:
                    print(ret)
                # Create a face detector
                face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # detect faces available on camera
                num_faces = face_detector.detectMultiScale(gray_frame, 
                                                        scaleFactor=1.3, minNeighbors=5)

                # take each face available on the camera and Preprocess it
                for (x, y, w, h) in num_faces:
                    cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (204, 102, 0), 4)
                    roi_gray_frame = gray_frame[y:y + h, x:x + w]
                    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, 
                                                                            (48, 48)), -1), 0)

                        # predict the emotions
                    emotion_prediction = emotion_model.predict(cropped_img)
                    maxindex = int(np.argmax(emotion_prediction))
                    cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (204, 102, 0), 2, cv2.LINE_AA)

                cv2.imshow('', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.cap('', cv2.WND_PROP_FULLSCREEN)
            cap.release()
            cv2.destroyAllWindows()

        img = customtkinter.CTk()
        window_width = 1280
        window_height = 720
        screen_width = img.winfo_screenwidth()
        screen_height = img.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        img.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        img.title('Live mode')
        img.iconbitmap("icon_kR0_icon.ico")
        l1 = customtkinter.CTkLabel(master=img, text="Live mode", font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        fr = customtkinter.CTkFrame(master=img, width=720, height=450, corner_radius=15)
        fr.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        back= customtkinter.CTkButton(master=img, width=100, height=60, text="home", compound=tk.TOP,
                                         corner_radius=15, font=('Century Gothic', 25))
        back.place(relx=0.07, rely=0.07)
        botona = customtkinter.CTkButton(master=img, width=100, height=60, text="Start", compound=tk.TOP,
                                         corner_radius=15, font=('', 25), command=start)
        botona.place(relx=0.47, rely=0.85)
        img.mainloop()

    def img_mode():
        w.destroy()

        def FacialExpressionModel(json_file, weights_file):
            with open(json_file, "r") as file:
                loaded_model_json = file.read()
                model = model_from_json(loaded_model_json)

            model.load_weights(weights_file)
            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

            return model

        top = customtkinter.CTk()
        window_width = 1280
        window_height = 720
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        top.title('Welcome')
        top.iconbitmap("icon_kR0_icon.ico")
        frame = customtkinter.CTkFrame(master=top, width=750, height=480, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label1 = customtkinter.CTkLabel(master=top, text='', font=('', 20), corner_radius=60)
        sign_image = Label(top)

        facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        model = FacialExpressionModel("model_a.json", "modelkarim.weights.h5")

        EMOTIONS_LIST = ["Angry", "Disgusted", "Fear", "Happy", "Neutral", "Sad", "Surprised"]

        def Detect(file_path):
            global Label_packed

            image = cv2.imread(file_path)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = facec.detectMultiScale(gray_image, 1.3, 5)
            try:
                for (x, y, w, h) in faces:
                    fc = gray_image[y:y + h, x:x + w]
                    roi = cv2.resize(fc, (48, 48))
                    pred = EMOTIONS_LIST[np.argmax(model.predict(roi[np.newaxis, :, :, np.newaxis]))]
                print("Predicted Emotion is" + pred)
                label1.configure(text=pred)
            except:
                label1.configure(text="Unable to detect")

        def show_Detect_button(file_path):
            detect_b = customtkinter.CTkButton(master=top, width=100, height=60, text="Detect emotion", compound=tk.TOP,
                                               corner_radius=15, fg_color='#e8b000', font=('', 25),
                                               command=lambda: Detect(file_path))
            detect_b.place(relx=0.8, rely=0.46)

        def upload_image():

            try:
                file_path = filedialog.askopenfilename()
                uploaded = Image.open(file_path)
                uploaded.thumbnail(((top.winfo_width() / 2), (top.winfo_height() / 2)))
                im = ImageTk.PhotoImage(uploaded)
                sign_image.configure(image=im)
                sign_image.image = im
                label1.configure(text='')
                show_Detect_button(file_path)
            except:
                pass

        upload = customtkinter.CTkButton(master=top, width=150, height=60, text="upload", compound=tk.TOP,
                                         corner_radius=15, font=('', 25), command=upload_image)
        upload.place(relx=0.45, rely=0.89)
        sign_image.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        label1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        heading = customtkinter.CTkLabel(master=top, text="Image mode", font=('Century Gothic', 60))
        heading.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        back= customtkinter.CTkButton(master=top, width=100, height=60, text="home", compound=tk.TOP,
                                         corner_radius=15, font=('Century Gothic', 25))
        back.place(relx=0.07, rely=0.07)
        top.mainloop()

    w.iconbitmap("icon_kR0_icon.ico")
    image = Image.open("icons8-image-96.png")
    resized_image = image.resize((100, 100), Image.LANCZOS)
    converted_image = ImageTk.PhotoImage(resized_image)
    image1 = Image.open("icons8-video-96.png")
    resized_image1 = image1.resize((100, 100), Image.LANCZOS)
    converted_image1 = ImageTk.PhotoImage(resized_image1)

    image2 = Image.open("icons8-video-conference-100.png")
    resized_image2 = image2.resize((100, 100), Image.LANCZOS)
    converted_image2 = ImageTk.PhotoImage(resized_image2)

    image3 = Image.open("icons8-shutdown-64.png")
    resized_image3 = image3.resize((50, 50), Image.LANCZOS)
    converted_image3 = ImageTk.PhotoImage(resized_image3)

    l1 = customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    btn = customtkinter.CTkButton(master=w, width=300, height=400, text="Image", font=('Century Gothic', 40),
                                  image=converted_image, compound=tk.TOP, command=img_mode)
    btn.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    btn2 = customtkinter.CTkButton(master=w, width=300, height=400, text="Video", font=('Century Gothic', 40),
                                   image=converted_image1, compound=tk.TOP, command=vid_mode)
    btn2.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)
    btn3 = customtkinter.CTkButton(master=w, width=300, height=400, text="Live cam", font=('Century Gothic', 40),
                                   image=converted_image2, compound=tk.TOP, command=live_mode)
    btn3.place(relx=0.8, rely=0.6, anchor=tkinter.CENTER)


    w.mainloop()

login()
