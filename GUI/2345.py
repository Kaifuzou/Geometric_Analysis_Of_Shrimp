import tkinter as tk
import cv2
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_snapshot = tk.Button(window, text="Chụp ảnh", width=10, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.update()

        self.window.mainloop()

    def update(self):
        ret, frame = self.vid.read()

        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(10, self.update)

    def snapshot(self):
        ret, frame = self.vid.read()

        if ret:
            cv2.imwrite("captured_image.jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            print("Ảnh đã được chụp và lưu thành công.")

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Khởi tạo cửa sổ
root = tk.Tk()
app = WebcamApp(root, "Webcam App")
