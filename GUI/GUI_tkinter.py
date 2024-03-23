import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import ttk
import serial.tools.list_ports
from PIL import Image
import threading

class GUI:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.image_logo_path = r"D:\DA_Tot_Nghiep\Pycharm\images\Pic\logo.jpg"
        self.image_logo = Image.open(self.image_logo_path)
        self.photo_logo = ImageTk.PhotoImage(self.image_logo)


        heightwc = 500
        widthwc = 500
        h1 = 20
        h2 = 15
        h3 = 10
        fonttext= "Arial"

        self.selected_port = tk.StringVar()
        self.selected_baudrate = tk.IntVar()  # Thay đổi thành kiểu IntVar để lưu trữ giá trị số nguyên

        self.connected = False

        self.detect_serial_ports()
#------------------------------------------------------ Header ---------------------------------------------------------
        self.header = tk.Frame(self.window, bg="lightblue", height=40)
        self.header.grid(row=0, column=0, sticky="ew")
        self.header.pack_propagate(0)
        self.header_title = tk.Label(self.header, text="Header",font=("Arial", h1), bg="lightblue")
        self.header_title.pack()

#------------------------------------------------------ body -----------------------------------------------------------
        self.body = tk.Frame(self.window)
        self.body.grid(row=1, column=0, sticky="n")

     #------------------------------------------------ note ------------------------------------------------------------
        self.body_note = tk.Frame(self.body)
        self.body_note.grid(row=0, column=0, sticky="n", pady = 20)
        #--------------------------------------------- Information -----------------------------------------------------
        self.note_info = tk.LabelFrame(self.body_note, height=230, width=200)
        self.note_info.grid(row=0, column=0, pady = 10, padx=10)
        self.note_info.grid_propagate(False)

        self.lb_logo = tk.Label(self.note_info, image=self.photo_logo)
        self.lb_logo.grid(row=0, column=0, columnspan=2, pady= 15, padx=10)
        self.info_lb_name_nb1 = tk.Label(self.note_info, text="Name:", font=(fonttext, h3))
        self.info_lb_name_nb1.grid(row=1, column=0, sticky="w", padx=10)
        self.info_name_nb1 = tk.Label(self.note_info, text="Pham Minh Hoi", font=(fonttext, h3))
        self.info_name_nb1.grid(row=1, column=1, sticky="w", padx=10)
        self.info_lb_id_nb1 = tk.Label(self.note_info, text="ID:", font=(fonttext, h3))
        self.info_lb_id_nb1.grid(row=2, column=0, sticky="w", padx=10)
        self.info_id_nb1 = tk.Label(self.note_info, text="62133748", font=(fonttext, h3))
        self.info_id_nb1.grid(row=2, column=1, sticky="w", padx=10)
        self.info_lb_name_nb2 = tk.Label(self.note_info, text="Name:", font=(fonttext, h3))
        self.info_lb_name_nb2.grid(row=3, column=0, sticky="w", padx=10)
        self.info_name_nb2 = tk.Label(self.note_info, text="Le Xuan Tung", font=(fonttext, h3))
        self.info_name_nb2.grid(row=3, column=1, sticky="w", padx=10)
        self.info_lb_id_nb2 = tk.Label(self.note_info, text="ID:", font=(fonttext, h3))
        self.info_lb_id_nb2.grid(row=4, column=0, sticky="w", padx=10)
        self.info_id_nb2 = tk.Label(self.note_info, text="62133748", font=(fonttext, h3))
        self.info_id_nb2.grid(row=4, column=1, sticky="w", padx=10)

        #---------------------------------------------- Connect --------------------------------------------------------
        self.note_connect = tk.LabelFrame(self.body_note, height=120, width=200)
        self.note_connect.grid(row=1, column=0)
        self.note_connect.grid_propagate(False)

        if self.available_ports:

            self.fr_label_port = tk.Frame(self.note_connect)
            self.fr_label_port.grid(row=0, column=0, sticky="w")
            self.label_port = tk.Label(self.fr_label_port, text="Port:", font=(fonttext, h3))
            self.label_port.grid(row=0, column=0, sticky = "w")

            self.port_dropdown = tk.OptionMenu(self.fr_label_port, self.selected_port, *self.available_ports)
            self.port_dropdown.grid(row=0, column=1, sticky = "w")

            self.label_baudrate = tk.Label(self.fr_label_port, text="Baudrate:", font=(fonttext, h3))
            self.label_baudrate.grid(row=1, column=0, sticky = "w")
            # Tạo menu để chọn tốc độ baud
            self.baudrate_menu = tk.OptionMenu(self.fr_label_port, self.selected_baudrate, 9600, 19200, 38400, 57600, 115200)
            self.baudrate_menu.grid(row=1, column=1, sticky = "w")

            self.fr_connect_button = tk.Frame(self.note_connect)
            self.fr_connect_button.grid(row=1, column=0, sticky = "e")
            self.connect_button = tk.Button(self.fr_connect_button, text="Kết nối", command=self.toggle_connection)
            self.connect_button.grid(row=0, column=0, sticky = "ew", columnspan=2)

        # ---------------------------------------------- Connect -------------------------------------------------------

            self.note_controller = tk.LabelFrame(self.body_note, text="Controller", height=150, width=200)
            self.note_controller.grid(row=2, column=0)
            self.note_controller.grid_propagate(False)

            # frame light
            self.controller_light = tk.Frame(self.note_controller)
            self.controller_light.grid(row=0, column=0, pady=5)
            self.light_lb = tk.Label(self.controller_light, text="Light:")
            self.light_lb.grid(row=0, column=0)
            self.light_lb_ltop = tk.Label(self.controller_light, text="Top")
            self.light_lb_ltop.grid(row=1, column=0)
            self.light_cb_ltop = tk.Checkbutton(self.controller_light)
            self.light_cb_ltop.grid(row=2, column=0)
            self.light_lb_lleft = tk.Label(self.controller_light, text="Left")
            self.light_lb_lleft.grid(row=1, column=1)
            self.light_cb_lleft = tk.Checkbutton(self.controller_light)
            self.light_cb_lleft.grid(row=2, column=1)
            self.light_lb_lright = tk.Label(self.controller_light, text="Right")
            self.light_lb_lright.grid(row=1, column=2)
            self.light_cb_lright = tk.Checkbutton(self.controller_light)
            self.light_cb_lright.grid(row=2, column=2)
            self.light_lb_lbehind = tk.Label(self.controller_light, text="Behind")
            self.light_lb_lbehind.grid(row=1, column=3)
            self.light_cb_lbehind = tk.Checkbutton(self.controller_light)
            self.light_cb_lbehind.grid(row=2, column=3)
            self.light_lb_lopposite = tk.Label(self.controller_light, text="Opposite")
            self.light_lb_lopposite.grid(row=1, column=4)
            self.light_cb_lopposite = tk.Checkbutton(self.controller_light)
            self.light_cb_lopposite.grid(row=2, column=4)

            # frame webcam
            self.controller_webcam = tk.Frame(self.note_controller)
            self.controller_webcam.grid(row=1, column=0, sticky = "w", pady=5)

            self.webcam_lb = tk.Label(self.controller_webcam, text="Webcam:")
            self.webcam_lb.grid(row=0, column=0)
            self.webcam_btn_on = tk.Button(self.controller_webcam, text="On", command=self.on_button_click)
            self.webcam_btn_on.grid(row=0, column=1, padx = 10)
            self.webcam_btn_off = tk.Button(self.controller_webcam, text="Off", command=self.off_button_click, state="disabled")
            self.webcam_btn_off.grid(row=0, column=2)

            self.cap1 = None
            self.cap2 = None

            self.update()


    # ------------------------------------------------ main ------------------------------------------------------------
        self.body_main = tk.Frame(self.body, bg = "black")
        self.body_main.grid(row=0, column=1, sticky="n")

    # Body main notebook
        self.main_notebook = ttk.Notebook(self.body_main)
        self.main_notebook.grid(row=0, column=1)
        # Data tab
        self.notebook_data = ttk.Frame(self.main_notebook)
        self.main_notebook.add(self.notebook_data, text="Data")

    # label frame webcam
        self.data_webcamy = tk.LabelFrame(self.notebook_data, text="Webcam Top", height=heightwc, width=widthwc)
        self.data_webcamy.grid(row=0, column=0, pady =10, padx=5)
        self.data_webcamx = tk.LabelFrame(self.notebook_data, text="Webcam Right", height=heightwc, width=widthwc)
        self.data_webcamx.grid(row=0, column=1, padx=5)

        self.canvas1 = tk.Canvas(self.data_webcamy, width=500, height=500)
        self.canvas1.pack()

        self.canvas2 = tk.Canvas(self.data_webcamx, width=500, height=500)
        self.canvas2.pack()

    # label frame controller
        self.data_fr_controller = tk.Frame(self.notebook_data, height=230, width=240)
        self.data_fr_controller.grid(row=0, column=2, columnspan=2, sticky="ns", pady=10)

        self.controller_lbfr_controller = tk.LabelFrame(self.data_fr_controller, text="Controller", height=230, width=240)
        self.controller_lbfr_controller.grid(row=0, column=0, columnspan=2, sticky="n", pady=10, padx=5)
        self.controller_lbfr_controller.grid_propagate(False)

        self.connected_fr_manual = tk.Frame(self.controller_lbfr_controller)
        self.connected_fr_manual.grid(row=0, column=0, pady=5, padx=5)

        self.manual_lb_rotate = tk.Label(self.connected_fr_manual, text="Rotate:")
        self.manual_lb_rotate.grid(row=0, column=0, sticky = "w")
        self.manual_et_rotate = tk.Entry(self.connected_fr_manual)
        self.manual_et_rotate.grid(row=0, column=1)
        self.manual_lb_light = tk.Label(self.connected_fr_manual, text="Light:")
        self.manual_lb_light.grid(row=1, column=0, sticky = "w")
        self.manual_et_light = tk.Entry(self.connected_fr_manual)
        self.manual_et_light.grid(row=1, column=1)
        self.manual_lb_id_shrimp = tk.Label(self.connected_fr_manual, text="ID Shrimp:")
        self.manual_lb_id_shrimp.grid(row=2, column=0, sticky = "w")
        self.manual_et_id_shrimp = tk.Entry(self.connected_fr_manual)
        self.manual_et_id_shrimp.grid(row=2, column=1)
        self.manual_lb_actual_weight = tk.Label(self.connected_fr_manual,text="Actual weight:")
        self.manual_lb_actual_weight.grid(row=3, column=0, sticky = "w")
        self.manual_et_actual_weight = tk.Entry(self.connected_fr_manual)
        self.manual_et_actual_weight.grid(row=3,column=1)

        self.connected_fr_btn = tk.Frame(self.controller_lbfr_controller)
        self.connected_fr_btn.grid(row=1, column=0, sticky = "w", pady=5, padx=30)
        self.manual_btn_send = tk.Button(self.connected_fr_btn, text="Send", command=self.send_send_command)
        self.manual_btn_send.grid(row=0, column=0)
        self.manual_btn_save = tk.Button(self.connected_fr_btn, text="Save")
        self.manual_btn_save.grid(row=0, column=1, padx = 20)
        self.manual_btn_auto = tk.Button(self.connected_fr_btn, text="Auto", command=self.send_auto_command)
        self.manual_btn_auto.grid(row=0, column=2)

        self.connected_fr_note = tk.Frame(self.controller_lbfr_controller)
        self.connected_fr_note.grid(row=2, column=0, sticky="w")
        self.note_lb_tile = tk.Label(self.connected_fr_note, text="Note")
        self.note_lb_tile.grid(row=0, column=0, sticky="w")
        self.note_lb_rotate = tk.Label(self.connected_fr_note, text="Rotate:")
        self.note_lb_rotate.grid(row=1, column=0, sticky="w")
        self.note_info_rotate = tk.Label(self.connected_fr_note, text="Min >=0, Max <=180")
        self.note_info_rotate.grid(row=1, column=1, sticky="w")
        self.note_lb_light = tk.Label(self.connected_fr_note, text="Light:")
        self.note_lb_light.grid(row=2, column=0, sticky="w")
        self.note_info_light = tk.Label(self.connected_fr_note, text="Min >=1, Max <=3")
        self.note_info_light.grid(row=2, column=1, sticky="w")

    # controller - status
        self.controler_lbfr_status = tk.LabelFrame(self.data_fr_controller, text="Status", height=250, width=240)
        self.controler_lbfr_status.grid(row=1, column=0, columnspan=2, sticky="n", pady=10, padx=5)
        self.controler_lbfr_status.grid_propagate(False)

        self.status_fr_light = tk.Frame(self.controler_lbfr_status)
        self.status_fr_light.grid(row=0, column=0, pady=10, padx= 10)
        self.light_lb_tilte = tk.Label(self.status_fr_light, text="Light:")
        self.light_lb_tilte.grid(row=0, column=0)

        self.status_light_lb_ltop = tk.Label(self.status_fr_light, text="Top")
        self.status_light_lb_ltop.grid(row=1, column=0)
        self.status_light_cb_ltop = tk.Label(self.status_fr_light, text="OFF")
        self.status_light_cb_ltop.grid(row=2, column=0)
        self.status_light_lb_lleft = tk.Label(self.status_fr_light, text="Left")
        self.status_light_lb_lleft.grid(row=1, column=1)
        self.status_light_cb_lleft = tk.Label(self.status_fr_light, text="OFF")
        self.status_light_cb_lleft.grid(row=2, column=1)
        self.status_light_lb_lright = tk.Label(self.status_fr_light, text="Right")
        self.status_light_lb_lright.grid(row=1, column=2)
        self.status_light_cb_lright = tk.Label(self.status_fr_light, text="OFF")
        self.status_light_cb_lright.grid(row=2, column=2)
        self.status_light_lb_lbehind = tk.Label(self.status_fr_light, text="Behind")
        self.status_light_lb_lbehind.grid(row=1, column=3)
        self.status_light_cb_lbehind = tk.Label(self.status_fr_light, text="OFF")
        self.status_light_cb_lbehind.grid(row=2, column=3)
        self.status_light_lb_lopposite = tk.Label(self.status_fr_light, text="Opposite")
        self.status_light_lb_lopposite.grid(row=1, column=4)
        self.status_light_cb_lopposite = tk.Label(self.status_fr_light, text="OFF")
        self.status_light_cb_lopposite.grid(row=2, column=4)

        self.status_fr_rotate_weight = tk.Frame(self.controler_lbfr_status)
        self.status_fr_rotate_weight.grid(row=1, column=0, sticky="w", padx=10)
        self.rotate_lb_tilte = tk.Label(self.status_fr_rotate_weight, text="Rotate:")
        self.rotate_lb_tilte.grid(row=0, column=0)
        self.rotate_lb_value = tk.Label(self.status_fr_rotate_weight, text="0")
        self.rotate_lb_value.grid(row=0, column=1)
        self.rotate_lb_unit = tk.Label(self.status_fr_rotate_weight, text="Degrees")
        self.rotate_lb_unit.grid(row=0, column=2)

        self.weight_lb_tilte = tk.Label(self.status_fr_rotate_weight, text="Weight:")
        self.weight_lb_tilte.grid(row=1, column=0, sticky="w")
        self.weight_lb_value = tk.Label(self.status_fr_rotate_weight, text="0")
        self.weight_lb_value.grid(row=1, column=1, sticky="w")
        self.weight_lb_unit = tk.Label(self.status_fr_rotate_weight, text="Gam")
        self.weight_lb_unit.grid(row=1, column=2, sticky="w")
        self.light_lv_lb_tilte = tk.Label(self.status_fr_rotate_weight, text="Light Lv:")
        self.light_lv_lb_tilte.grid(row=2, column=0)
        self.light_lv_value = tk.Label(self.status_fr_rotate_weight, text="0")
        self.light_lv_value.grid(row=2, column=1)





# ---------------------------------------------------Data webcam--------------------------------------------------------
        self.notebook_webcam = ttk.Frame(self.main_notebook)
        self.main_notebook.add(self.notebook_webcam, text="Webcam")

        # Data picture
        self.notebook_picture = ttk.Frame(self.main_notebook)
        self.main_notebook.add(self.notebook_picture, text="Picture")

# ------------------------------------------------------ Footer ---------------------------------------------------------
        self.footer = tk.Frame(self.window, bg="lightblue", height=40)
        self.footer.grid(row=2, column=0, sticky="ew")
        self.footer.pack_propagate(0)
        self.footer_title = tk.Label(self.footer, text="Footer", font=("Arial", h1), bg="lightblue")
        self.footer_title.pack()

    #------------------------------------------------------ DEF ------------------------------------------------------------

    # ----------------------------------------------- connect ---------------------------------------------------------
    def detect_serial_ports(self):
        self.available_ports = [port.device for port in serial.tools.list_ports.comports()]
        if not self.available_ports:
            self.available_ports = ["Unknown"]

    def toggle_connection(self):
        if not self.connected:
            self.connect_to_esp32()
        else:
            self.disconnect_from_esp32()

    def connect_to_esp32(self):
        selected_port = self.selected_port.get()
        baudrate = self.selected_baudrate.get()  # Sử dụng .get() để lấy giá trị từ IntVar

        if selected_port != "Unknown":
            try:
                self.esp32_serial = serial.Serial(selected_port, baudrate)
                print("Đã kết nối tới ESP32 trên cổng", selected_port, "với tốc độ baud", baudrate)
                self.connected = True
                self.connect_button.config(text="Ngắt kết nối")
                # Thêm code xử lý kết nối thành công ở đây nếu cần
            except serial.SerialException as e:
                print("Lỗi kết nối:", e)
                # Thêm code xử lý lỗi kết nối ở đây nếu cần

    def connect_to_esp32(self):
        selected_port = self.selected_port.get()
        baudrate = self.selected_baudrate.get()

        if selected_port != "Unknown":
            try:
                self.esp32_serial = serial.Serial(selected_port, baudrate)
                print("Đã kết nối tới ESP32 trên cổng", selected_port, "với tốc độ baud", baudrate)
                self.connected = True
                self.connect_button.config(text="Ngắt kết nối")
                # Start a thread to continuously listen for data from ESP32
                self.listen_to_esp32_thread = threading.Thread(target=self.listen_to_esp32)
                self.listen_to_esp32_thread.daemon = True
                self.listen_to_esp32_thread.start()
            except serial.SerialException as e:
                print("Lỗi kết nối:", e)

    def listen_to_esp32(self):
        while self.connected:
            try:
                data = self.esp32_serial.readline().decode().strip()
                if data.startswith("rotate"):
                    rotate_value = data.split("rotate")[1].strip()
                    self.rotate_lb_value.config(text=rotate_value)
                elif data.startswith("weight"):
                    weight_value = data.split("weight")[1].strip()
                    self.weight_lb_value.config(text=weight_value)
                elif data.startswith("light"):
                    light_value = data.split("light")[1].strip()
                    self.light_lv_value.config(text=light_value)
                elif data == "caption":
                    # Truyền đường dẫn bạn muốn lưu hình ảnh vào đây
                    save_path = "D:/DA_Tot_Nghiep/Pycharm/images/Pic"
                    self.save_images(save_path)
            except serial.SerialException as e:
                print("Lỗi khi nhận dữ liệu từ ESP32:", e)

    def save_images(self, save_path):
        if self.cap1 is not None and self.cap2 is not None:
            ret1, frame1 = self.cap1.read()
            ret2, frame2 = self.cap2.read()

            if ret1 and ret2:
                # Lưu frame từ webcam 1
                filename1 = (save_path + "/webcam1_" + str(self.rotate_lb_value.cget("text")) + "_"+
                             str(self.weight_lb_value.cget("text")) + "_" + str(self.light_lv_value.cget("text")) + ".jpg")
                cv2.imwrite(filename1, frame1)

                # Lưu frame từ webcam 2
                filename2 = (save_path + "/webcam2_" + str(self.rotate_lb_value.cget("text")) + "_"+
                             str(self.weight_lb_value.cget("text")) + "_" + str(self.light_lv_value.cget("text")) + ".jpg")
                cv2.imwrite(filename2, frame2)

                print("Đã lưu hình ảnh từ 2 webcam.")

    def disconnect_from_esp32(self):
        if self.connected:
            try:
                self.esp32_serial.close()
                print("Đã ngắt kết nối")
                self.connected = False
                self.connect_button.config(text="Kết nối")
            except serial.SerialException as e:
                print("Lỗi khi ngắt kết nối:", e)

    def send_auto_command(self):
        if self.connected:
            try:
                self.esp32_serial.write(b"1\n")  # Send "auto" command
                print("Sent 'auto' command to ESP32")
            except serial.SerialException as e:
                print("Error sending command:", e)

    def send_send_command(self):
        if self.connected:
            try:
                self.esp32_serial.write(b"0\n")  # Send "auto" command
                print("Sent 'send' command to ESP32")
            except serial.SerialException as e:
                print("Error sending command:", e)


    def on_button_click(self):
        self.webcam_btn_on['state'] = 'disabled'
        self.webcam_btn_off['state'] = 'normal'
        self.cap1 = cv2.VideoCapture(0)
        self.cap2 = cv2.VideoCapture(1)

    def off_button_click(self):
        self.webcam_btn_on['state'] = 'normal'
        self.webcam_btn_off['state'] = 'disabled'
        if self.cap1 is not None:
            self.cap1.release()
        if self.cap2 is not None:
            self.cap2.release()

    def update(self):
        if self.cap1 is not None and self.cap2 is not None:
            ret1, frame1 = self.cap1.read()
            if ret1:
                frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                frame1 = Image.fromarray(frame1)
                self.photo1 = ImageTk.PhotoImage(image=frame1)
                self.canvas1.create_image(0, 0, image=self.photo1, anchor=tk.NW)

            ret2, frame2 = self.cap2.read()
            if ret2:
                frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                frame2 = Image.fromarray(frame2)
                self.photo2 = ImageTk.PhotoImage(image=frame2)
                self.canvas2.create_image(0, 0, image=self.photo2, anchor=tk.NW)

        self.window.after(10, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root, "Shrimp")
    root.mainloop()