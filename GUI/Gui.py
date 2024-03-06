import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np


class MyGui:
    def __init__(self, master):
        self.master = master
        self.master.title("GUI")

        f = "Elaris"
        fs_h1 = 22
        fs_h2 = 15
        fs_h3 = 12
        fs_h4 = 10

# ------------------------------------------------- Header design ------------------------------------------------------
        # Create frame
        self.header = tk.Frame(self.master, bg="lightblue", height=100)
        self.header.pack(fill=tk.BOTH)

        # Create label
        self.title_header = tk.Label(self.header, text="GEOMETRIC ANALYSIS OF SHRIMP", fg="black", bg="lightblue",
                                     font=(f,fs_h1), pady=10)
        self.title_header.pack()

# -------------------------------------------------- Body design -------------------------------------------------------
        # Create frame
        self.body = tk.Frame(self.master)
        self.body.pack(fill=tk.BOTH, expand=True)

        # ---------------------------- Info zone -----------------------------
        self.info_zone = tk.LabelFrame(self.body, text="Information", font=(f,fs_h3))
        self.info_zone.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        self.ntu = tk.Label(self.info_zone, text="Nha Trang University", font=(f,fs_h2))
        self.ntu.grid(row=0, column=0, columnspan=2, sticky="new")

        self.med = tk.Label(self.info_zone, text="Mechatronics", font=(f,fs_h3))
        self.med.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.label_name_h = tk.Label(self.info_zone, text="Name:", font=(f,fs_h4))
        self.label_name_h.grid(row=2, column=0, sticky="w")
        self.name_h = tk.Label(self.info_zone, text="Pham Minh Hoi", font=(f,fs_h4))
        self.name_h.grid(row=2, column=1, sticky="w")

        self.label_id_h = tk.Label(self.info_zone, text="ID:", font=(f,fs_h4))
        self.label_id_h.grid(row=3, column=0, sticky="w")
        self.id_h = tk.Label(self.info_zone, text="62133748", font=(f,fs_h4))
        self.id_h.grid(row=3, column=1, sticky="w")

        self.label_name_t = tk.Label(self.info_zone, text="Name:", font=(f,fs_h4))
        self.label_name_t.grid(row=4, column=0, sticky="w")
        self.name_t = tk.Label(self.info_zone, text="Le Xuan Tung", font=(f,fs_h4))
        self.name_t.grid(row=4, column=1, sticky="w")

        self.label_id_t = tk.Label(self.info_zone, text="ID:", font=(f,fs_h4))
        self.label_id_t.grid(row=5, column=0, sticky="w")
        self.id_t = tk.Label(self.info_zone, text="62139018", font=(f,fs_h4))
        self.id_t.grid(row=5, column=1, sticky="w")

    # ---------------------------- Connect zone -----------------------------
        self.connect_zone = tk.LabelFrame(self.body, bg="red", text="Connect", font=(f,fs_h3))
        self.connect_zone.grid(row=1, column=0, padx=5, pady=5, sticky="nw")

        # ---------------------------- Table zone -----------------------------
        self.table_zone = tk.LabelFrame(self.body, text="Table", width=1100, height=730,
                                        font=(f, fs_h3))
        self.table_zone.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="n")

        self.table_notebook = ttk.Notebook(self.table_zone, width=1100, height=730)
        self.table_notebook.pack(fill=tk.BOTH, expand=True)
        self.table_zone.grid_propagate(False)

        # -------------------------- Tab Webcam ----------------------------
        px = 320
        self.webcam_tab = ttk.Frame(self.table_notebook)
        self.table_notebook.add(self.webcam_tab, text="Webcam")

        self.lb_webcamy = tk.LabelFrame(self.webcam_tab, text="webcamy", width=px, height=px)
        self.lb_webcamy.grid(row=0, column=0, padx=10, pady=10)

        self.threshold_webcamy = tk.LabelFrame(self.webcam_tab, text="thresholding webcam y", width=px, height=px)
        self.threshold_webcamy.grid(row=0, column=1)

        self.lb_webcamx = tk.LabelFrame(self.webcam_tab, text="webcamx", width=px, height=px)
        self.lb_webcamx.grid(row=1, column=0)

        self.threshold_webcamx = tk.LabelFrame(self.webcam_tab, text="thresholding webcam x", width=px, height=px)
        self.threshold_webcamx.grid(row=1, column=1)

        self.controller_webcam = tk.LabelFrame(self.webcam_tab, text="Controller", width=px, height=px * 2)
        self.controller_webcam.grid(row=0, column=2, rowspan=2, padx=10, pady=10)
        self.controller_webcam.grid_propagate(False)

        self.btn_on = tk.Button(self.controller_webcam, text="Start")
        self.btn_on.grid(row=0, column=0)
        self.btn_off = tk.Button(self.controller_webcam, text="Stop")
        self.btn_off.grid(row=0, column=1)

    # -------------------------- Tab picture --------------------------
        wi = 500
        he = 375
        self.picture_tab = ttk.Frame(self.table_zone)
        self.table_notebook.add(self.picture_tab, text="Picture")

        self.picture = tk.LabelFrame(self.picture_tab, text="Image", width=wi, height=he)
        self.picture.grid(row=0, column=0)

        self.threshold_picture = tk.LabelFrame(self.picture_tab, text="thresholding Image x", width=wi, height=he)
        self.threshold_picture.grid(row=0, column=1)

        self.controller_pictrue = tk.LabelFrame(self.picture_tab, text="Controller", width=wi, height=he)
        self.controller_pictrue.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.controller_pictrue.grid_propagate(False)

        # Add button to choose image
        self.btn_choose_image = tk.Button(self.controller_pictrue, text="Choose Image", command=self.choose_image)
        self.btn_choose_image.grid(row=0, column=0)

        self.slider = tk.Scale(self.controller_pictrue, from_=0, to=255, orient=tk.HORIZONTAL)
        self.slider.grid(row=1, column=0)

        self.entry = tk.Entry(self.controller_pictrue)
        self.entry.grid(row=1, column=1)
        self.slider.set(127)

    # ---------------------------- Parameter zone -----------------------------
        self.parameter_zone = tk.LabelFrame(self.body, bg="yellow", text="Parameter", font=(f,fs_h3))
        self.parameter_zone.grid(row=0, column=2, padx=5, pady=5, sticky="nw")

        self.height = tk.Label(self.parameter_zone, text="Height:", font=(f,fs_h4))
        self.height.grid(row=0, column=0,sticky="w")

        self.height_unit = tk.Label(self.parameter_zone, text="mm", font=(f,fs_h4))
        self.height_unit.grid(row=0, column=2, sticky="w")

        self.weight = tk.Label(self.parameter_zone, text="Weight:", font=(f,fs_h4))
        self.weight.grid(row=1, column=0, sticky="w")

        self.weight_unit = tk.Label(self.parameter_zone, text="gam", font=(f,fs_h4))
        self.weight_unit.grid(row=1, column=2, sticky="w")

        self.length = tk.Label(self.parameter_zone, text="Length:", font=(f,fs_h4))
        self.length.grid(row=2, column=0, sticky="w")

        self.length_unit = tk.Label(self.parameter_zone, text="mm", font=(f,fs_h4))
        self.length_unit.grid(row=2, column=2, sticky="w")

        self.width = tk.Label(self.parameter_zone, text="Width:", font=(f,fs_h4))
        self.width.grid(row=3, column=0, sticky="w")

        self.width_unit = tk.Label(self.parameter_zone, text="mm", font=(f,fs_h4))
        self.width_unit.grid(row=3, column=2, sticky="w")

        self.area = tk.Label(self.parameter_zone, text="Area:", font=(f,fs_h4))
        self.area.grid(row=4, column=0, sticky="w")

        self.area_unit = tk.Label(self.parameter_zone, text="mm2", font=(f,fs_h4))
        self.area_unit.grid(row=4, column=2, sticky="w")

# ------------------------------------------------- Footer design ------------------------------------------------------
        # Create frame
        self.footer = tk.Frame(self.master, bg="black", height=30)
        self.footer.pack(fill=tk.BOTH)

    def choose_image(self):
        # Mở hộp thoại để chọn ảnh
        file_path = filedialog.askopenfilename(title="Choose an image",
                                               filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])

        # Hiển thị ảnh đã chọn trong label frame picture
        if file_path:
            image = Image.open(file_path)
            image = image.resize((500, 375), Image.BICUBIC)
            photo = ImageTk.PhotoImage(image)

            # Cập nhật hoặc tạo label với ảnh
            if hasattr(self, "lbl_chosen_image"):
                self.lbl_chosen_image.configure(image=photo)
                self.lbl_chosen_image.image = photo
            else:
                self.lbl_chosen_image = tk.Label(self.picture, image=photo)
                self.lbl_chosen_image.image = photo
                self.lbl_chosen_image.pack()

            # Phân ngưỡng ảnh
            img_cv = cv2.imread(file_path)
            gray_img = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

            # Tính toán tâm của ảnh
            height, width = gray_img.shape[:2]
            center_x, center_y = width // 2, height // 2

            # Tạo mask cho vùng tròn có bán kính 260 pixel
            mask_circle = np.zeros((height, width), np.uint8)
            radius = 260
            cv2.circle(mask_circle, (center_x, center_y), radius, (255, 255, 255), -1)

            # Tạo mask cho vùng bên ngoài vùng tròn
            mask_outer = np.ones((height, width), np.uint8) * 255
            cv2.circle(mask_outer, (center_x, center_y), radius, (0, 0, 0), -1)

            # Áp dụng phân ngưỡng trên cả hai vùng
            _, threshold_img_circle = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
            _, threshold_img_outer = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY)

            # Áp dụng mask cho cả hai vùng
            threshold_img_circle = cv2.bitwise_and(threshold_img_circle, threshold_img_circle, mask=mask_circle)
            threshold_img_outer = cv2.bitwise_and(threshold_img_outer, threshold_img_outer, mask=mask_outer)

            # Ghép kết quả lại với nhau
            threshold_img_combined = cv2.add(threshold_img_circle, threshold_img_outer)

            # Chuyển ảnh OpenCV thành định dạng PIL để hiển thị trong tkinter
            threshold_img_pil = Image.fromarray(threshold_img_combined)
            threshold_img_pil = threshold_img_pil.resize((500, 375), Image.BICUBIC)
            threshold_photo = ImageTk.PhotoImage(threshold_img_pil)

            # Hiển thị ảnh phân ngưỡng trong label frame threshold_picture
            if hasattr(self, "lbl_threshold_image"):
                self.lbl_threshold_image.configure(image=threshold_photo)
                self.lbl_threshold_image.image = threshold_photo
            else:
                self.lbl_threshold_image = tk.Label(self.threshold_picture, image=threshold_photo)
                self.lbl_threshold_image.image = threshold_photo
                self.lbl_threshold_image.pack()

def main():
    root = tk.Tk()
    app = MyGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
