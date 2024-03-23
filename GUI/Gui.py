import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np


class MyWindow:
    def __init__(self):
        # Tạo một cửa sổ mới
        self.window = tk.Tk()
        self.window.title("kaifuzou")

        # Tạo một Table Notebook
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(expand=True, fill="both")

        # Tạo Tab "Webcam"
        self.webcam_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.webcam_tab, text="Webcam")

        self.image_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.image_tab, text="Image")

        # Label frame cho webcam
        self.webcam_frame = tk.LabelFrame(self.webcam_tab, text="Webcam", width=350, height=350)
        self.webcam_frame.pack(side="left", padx=10, pady=10)

        # Label frame cho kết quả
        self.result_frame = tk.LabelFrame(self.webcam_tab, text="Kết quả", width=350, height=350)
        self.result_frame.pack(side="left", padx=10, pady=10)

        # Label frame cho điều khiển
        self.control_frame = tk.LabelFrame(self.webcam_tab, text="Điều khiển", width=350, height=350)
        self.control_frame.pack(side="left", padx=10, pady=10)

        # Tạo nút On và Off
        self.on_button = tk.Button(self.control_frame, text="On", command=self.turn_on_webcam)
        self.on_button.grid(row=0, column=0, padx=5, pady=5)

        self.off_button = tk.Button(self.control_frame, text="Off", command=self.turn_off_webcam)
        self.off_button.grid(row=0, column=1, padx=5, pady=5)

        # Tạo thanh trượt HSV
        self.hue_scale = tk.Scale(self.control_frame, label="Hue", from_=0, to=179, orient="horizontal")
        self.hue_scale.grid(row=1, column=0, padx=5, pady=5)

        self.saturation_scale = tk.Scale(self.control_frame, label="Saturation", from_=0, to=255, orient="horizontal")
        self.saturation_scale.grid(row=1, column=1, padx=5, pady=5)

        self.value_scale = tk.Scale(self.control_frame, label="Value", from_=0, to=255, orient="horizontal")
        self.value_scale.grid(row=1, column=2, padx=5, pady=5)

        # Tạo thanh trượt phân ngưỡng
        self.threshold_scale = tk.Scale(self.control_frame, label="Phân ngưỡng", from_=0, to=255, orient="horizontal")
        self.threshold_scale.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        # ========================================================================================================================

        self.image_frame = tk.LabelFrame(self.image_tab, text="picture", width=350, height=350)
        self.image_frame.pack(side="left", padx=10, pady=10)

        # Label frame cho kết quả
        self.image_result_frame = tk.LabelFrame(self.image_tab, text="Kết quả", width=350, height=350)
        self.image_result_frame.pack(side="left", padx=10, pady=10)

        # Label frame cho điều khiển
        self.image_control_frame = tk.LabelFrame(self.image_tab, text="Điều khiển", width=350, height=350)
        self.image_control_frame.pack(side="left", padx=10, pady=10)

        self.choose_image_button = tk.Button(self.image_control_frame, text="Chọn ảnh", command=self.choose_image)
        self.choose_image_button.grid(row=0, column=0, padx=5, pady=5)

        # Tạo thanh trượt HSV
        self.hue_scale_image = tk.Scale(self.image_control_frame, label="Hue", from_=0, to=179, orient="horizontal",
                                        command=self.update_image)
        self.hue_scale_image.grid(row=1, column=0, padx=5, pady=5)

        self.saturation_scale_image = tk.Scale(self.image_control_frame, label="Saturation", from_=0, to=255,
                                               orient="horizontal", command=self.update_image)
        self.saturation_scale_image.grid(row=1, column=1, padx=5, pady=5)

        self.value_scale_image = tk.Scale(self.image_control_frame, label="Value", from_=0, to=255, orient="horizontal",
                                          command=self.update_image)
        self.value_scale_image.grid(row=1, column=2, padx=5, pady=5)

        self.threshold_scale_image = tk.Scale(self.image_control_frame, label="Phân ngưỡng", from_=0, to=255,
                                              orient="horizontal",
                                              command=self.update_threshold_image)
        self.threshold_scale_image.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.total_black_threshold_label = tk.Label(self.image_control_frame, text="Tổng ngưỡng màu đen: 0")
        self.total_black_threshold_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.area_of_black_threshold_label = tk.Label(self.image_control_frame, text="Diện tích vùng đen: 0")
        self.area_of_black_threshold_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # ======================================================================================================================
        # Một biến để kiểm soát trạng thái của webcam
        self.webcam_on = False

        # Khởi tạo video capture
        self.cap = None

        # Gọi mainloop để hiển thị cửa sổ
        self.window.mainloop()

    def turn_on_webcam(self):
        if not self.webcam_on:
            self.webcam_on = True
            self.show_webcam()

    def turn_off_webcam(self):
        if self.webcam_on:
            self.webcam_on = False
            if self.webcam_label is not None:
                self.webcam_label.grid_forget()
            if self.cap is not None:
                self.cap.release()

    def show_webcam(self):
        if self.cap is None or not self.cap.isOpened():
            self.cap = cv2.VideoCapture(0)
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (350, 350))

            # Adjust the HSV components
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            hsv_frame[:, :, 0] += self.hue_scale.get()
            hsv_frame[:, :, 1] += self.saturation_scale.get()
            hsv_frame[:, :, 2] += self.value_scale.get()
            frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2RGB)

            # Calculate the center coordinates of the frame
            center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2

            # Define the radius of the circular region
            radius = 200

            # Create a mask for the circular region
            mask = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)
            cv2.circle(mask, (center_x, center_y), radius, (255), -1)

            # Convert the mask to a boolean mask
            mask = mask.astype(bool)

            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # Apply thresholding only to the circular region
            _, thresholded_frame = cv2.threshold(gray_frame, self.threshold_scale.get(), 255, cv2.THRESH_BINARY)
            thresholded_frame[~mask] = 255  # Set giá trị màu ở bên ngoài vùng phân ngưỡng
            # Display the thresholded frame in the result label frame
            img = Image.fromarray(thresholded_frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.result_label = tk.Label(self.result_frame, image=imgtk)
            self.result_label.image = imgtk
            self.result_label.grid(row=0, column=0)

            # Display the webcam feed in the webcam_frame
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.webcam_label = tk.Label(self.webcam_frame, image=imgtk)
            self.webcam_label.image = imgtk
            self.webcam_label.grid(row=0, column=0)
        if self.webcam_on:
            self.window.after(10, self.show_webcam)
        else:
            self.cap.release()

    # =====================================================================================================================
    def choose_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.show_image(file_path)

    def show_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((350, 350), Image.LANCZOS)  # Sửa đổi từ Image.ANTIALIAS sang Image.LANCZOS
        imgtk = ImageTk.PhotoImage(image=image)
        self.image_label = tk.Label(self.image_frame, image=imgtk)
        self.image_label.image = imgtk
        self.image_label.grid(row=0, column=0)

    def update_image(self, *args):
        if hasattr(self, 'chosen_image'):
            image = self.chosen_image.copy()

            # Convert the image to HSV color space
            hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

            # Adjust the HSV components
            hsv_image[:, :, 0] += self.hue_scale_image.get()
            hsv_image[:, :, 1] += self.saturation_scale_image.get()
            hsv_image[:, :, 2] += self.value_scale_image.get()

            # Ensure that the values stay within the valid range
            hsv_image = np.clip(hsv_image, 0, 255)

            # Convert the image back to RGB color space
            rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)

            # Convert the RGB image to grayscale
            gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

            # Apply thresholding
            _, thresholded_image = cv2.threshold(gray_image, self.threshold_scale_image.get(), 255, cv2.THRESH_BINARY)

            # Display the thresholded image
            img = Image.fromarray(thresholded_image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.image_result_label = tk.Label(self.image_result_frame, image=imgtk)
            self.image_result_label.image = imgtk
            self.image_result_label.grid(row=0, column=0)

    def calculate_total_black_threshold(self, thresholded_image):
        # Tính tổng ngưỡng màu đen trong hình ảnh
        total_black_threshold = np.sum(thresholded_image == 0)
        return total_black_threshold

    def calculate_area_of_black_threshold(self, thresholded_image):
        # Tính diện tích của vùng đen trong hình ảnh
        area_of_black_threshold = cv2.countNonZero(thresholded_image)
        return area_of_black_threshold

    # Sau khi áp dụng phân ngưỡng và tách được vật thể từ nền, bạn có thể sử dụng hàm sau để vẽ contours


    def update_threshold_image(self, *args):
        if hasattr(self, 'chosen_image'):
            image = self.chosen_image.copy()

            # Calculate the center coordinates of the image
            center_x, center_y = image.shape[1] // 2, image.shape[0] // 2

            # Define the radius of the circular region
            radius = 150

            # Create a mask for the circular region
            mask = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
            cv2.circle(mask, (center_x, center_y), radius, (255), -1)

            # Convert the mask to a boolean mask
            mask = mask.astype(bool)

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

            # Apply thresholding only to the circular region
            _, thresholded_image = cv2.threshold(gray_image, self.threshold_scale_image.get(), 255, cv2.THRESH_BINARY)
            thresholded_image[~mask] = 255  # set màu vùng bên ngoài

            # Display the thresholded image in the result label frame
            img = Image.fromarray(thresholded_image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.image_result_label = tk.Label(self.image_result_frame, image=imgtk)
            self.image_result_label.image = imgtk
            self.image_result_label.grid(row=0, column=0)

            # Calculate and display the total black threshold
            total_black_threshold = self.calculate_total_black_threshold(thresholded_image)
            self.total_black_threshold_label.config(text=f"Tổng ngưỡng màu đen: {total_black_threshold}")

            # Calculate and display the area of black threshold
            area_of_black_threshold = self.calculate_area_of_black_threshold(thresholded_image)
            self.area_of_black_threshold_label.config(text=f"Diện tích vùng đen: {area_of_black_threshold}")



    # Call the update_threshold_image function initially to display the default thresholded image

    # Gọi phương thức này khi chọn hình ảnh để cập nhật biến self.chosen_image
    def show_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((350, 350), Image.LANCZOS)
        self.chosen_image = np.array(image)  # Lưu trữ hình ảnh dưới dạng mảng numpy
        imgtk = ImageTk.PhotoImage(image=image)
        self.image_label = tk.Label(self.image_frame, image=imgtk)
        self.image_label.image = imgtk
        self.image_label.grid(row=0, column=0)




# Tạo một đối tượng MyWindow để hiển thị cửa sổ
my_window = MyWindow()
