import tkinter as tk
import serial.tools.list_ports
import threading

class ESP32Interface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ESP32 Interface")
        self.geometry("400x300")

        self.selected_port = tk.StringVar()
        self.selected_baudrate = tk.IntVar()
        self.received_data = tk.StringVar()

        self.connected = False

        self.detect_serial_ports()

        if self.available_ports:
            self.label_port = tk.Label(self, text="Chọn cổng COM:")
            self.label_port.pack()

            self.port_dropdown = tk.OptionMenu(self, self.selected_port, *self.available_ports)
            self.port_dropdown.pack()

            self.label_baudrate = tk.Label(self, text="Chọn tốc độ baud:")
            self.label_baudrate.pack()

            self.baudrate_menu = tk.OptionMenu(self, self.selected_baudrate, 9600, 19200, 38400, 57600, 115200)
            self.baudrate_menu.pack()

            self.connect_button = tk.Button(self, text="Kết nối", command=self.toggle_connection)
            self.connect_button.pack()

            self.label_data = tk.Label(self, text="Nhập thông tin:")
            self.label_data.pack()

            self.entry_data = tk.Entry(self)
            self.entry_data.pack()

            self.send_button = tk.Button(self, text="Gửi lệnh", command=self.send_data, state=tk.DISABLED)
            self.send_button.pack()

            self.label_received_data = tk.Label(self, text="Dữ liệu nhận được:")
            self.label_received_data.pack()

            self.received_data_label = tk.Label(self, textvariable=self.received_data)
            self.received_data_label.pack()

            # Thêm hai label mới để hiển thị trọng lượng và chiều cao
            self.label_weight = tk.Label(self, text="Weight: 0")
            self.label_weight.pack()

            self.label_height = tk.Label(self, text="Height: 0")
            self.label_height.pack()

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
        baudrate = self.selected_baudrate.get()

        if selected_port != "Unknown":
            try:
                self.esp32_serial = serial.Serial(selected_port, baudrate)
                print("Đã kết nối tới ESP32 trên cổng", selected_port, "với tốc độ baud", baudrate)
                self.connected = True
                self.connect_button.config(text="Ngắt kết nối")
                self.send_button.config(state=tk.NORMAL)
                threading.Thread(target=self.receive_data).start()
            except serial.SerialException as e:
                print("Lỗi kết nối:", e)

    def disconnect_from_esp32(self):
        if self.connected:
            try:
                self.esp32_serial.close()
                print("Đã ngắt kết nối")
                self.connected = False
                self.connect_button.config(text="Kết nối")
                self.send_button.config(state=tk.DISABLED)
            except serial.SerialException as e:
                print("Lỗi khi ngắt kết nối:", e)

    def send_data(self):
        data = self.entry_data.get()
        if self.connected and data:
            try:
                self.esp32_serial.write(data.encode())
                print("Đã gửi dữ liệu:", data)
            except serial.SerialException as e:
                print("Lỗi khi gửi dữ liệu:", e)

    def receive_data(self):
        if self.connected:
            try:
                while True:
                    if self.esp32_serial.in_waiting > 0:
                        received_data = self.esp32_serial.readline().decode().strip()
                        print("Dữ liệu nhận được:", received_data)
                        if 'weight' in received_data:
                            weight = received_data.split('weight')[1]
                            self.label_weight.config(text="Weight: " + weight)
                        elif 'rotate' in received_data:
                            height = received_data.split('rotate')[1]
                            self.label_height.config(text="rotate: " + height)
            except serial.SerialException as e:
                print("Lỗi khi nhận dữ liệu:", e)
        self.after(100, self.receive_data)

if __name__ == "__main__":
    app = ESP32Interface()
    app.mainloop()
