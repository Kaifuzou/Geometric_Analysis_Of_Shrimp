import tkinter as tk
from tkinter import PhotoImage

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

        self.btn_on =tk.Button(self.connect_zone,text="Start")
        self.btn_on.grid(row=0, column=0, sticky="nsew")

        self.btn_off = tk.Button(self.connect_zone, text="Stop")
        self.btn_off.grid(row=1, column=0, sticky="nsew")


    # ---------------------------- Table zone -----------------------------
        self.table_zone = tk.LabelFrame(self.body, bg="lightblue", text="Table", width=1100, height=730, font=(f,fs_h3))
        self.table_zone.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="n")
        self.table_zone.grid_propagate(False)

        self.btn_1 = tk.Button(self.table_zone, text="Start")
        self.btn_1.grid(row=0, column=0, sticky="nsew")

        self.btn_2 = tk.Button(self.table_zone, text="Stop")
        self.btn_2.grid(row=1, column=0, sticky="nsew")



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
        # Tạo 1 frame
        self.footer = tk.Frame(self.master, bg="black", height=30)
        self.footer.pack(fill=tk.BOTH)

def main():
    root = tk.Tk()
    app = MyGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
