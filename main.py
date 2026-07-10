import tkinter as tk
from tkinter import ttk, messagebox
import re
import customtkinter as ctk

import matplotlib.pyplot as plt

from tkinter import filedialog
from data import load_data
from models import Relation

from models import WeddingData, RELATIONS
from ga import run_ga
from fitness import decode_solution

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class WeddingGAApp:
    def __init__(self):
        self.data = WeddingData()
        self.history = []

        self.root = ctk.CTk()
        self.root.title("Wedding Seating Optimization System")
        self.root.geometry("1400x850")

        self.build_ui()

    def build_ui(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        file_menu.add_command(
            label="Lưu dữ liệu"
        )

        file_menu.add_command(
            label="Mở dữ liệu"
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Thoát",
            command=self.root.quit
        )

        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        self.root.config(menu=menubar)

        header = ctk.CTkFrame(
            self.root,
            corner_radius=20,
            fg_color=("#3B82F6", "#1E40AF")
        )
        header.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            header,
            text="🎉 WEDDING SEATING OPTIMIZATION SYSTEM",
            font=("Segoe UI", 30, "bold"),
            text_color="white"
        ).pack(pady=(10, 0))

        ctk.CTkLabel(
            header,
            text="Genetic Algorithm for Wedding Seating Arrangement",
            font=("Segoe UI", 14)
        ).pack(pady=(0, 10))

        stats = ctk.CTkFrame(self.root)
        stats.pack(fill="x", padx=10, pady=5)

        # Card khách
        card_guest = ctk.CTkFrame(
            stats,
            fg_color="#2563EB",
            corner_radius=20)
        card_guest.pack(
            side="left",
            padx=10,
            pady=10,
            expand=True,
            fill="x"
        )
        # Card quan hệ
        card_relation = ctk.CTkFrame(
            stats,
            fg_color="#EC4899",
            corner_radius=15)

        # Card fitness
        card_fitness = ctk.CTkFrame(
            stats,
            fg_color="#10B981",
            corner_radius=15)

        # Card bàn
        card_table = ctk.CTkFrame(
            stats,
            fg_color="#F59E0B",
            corner_radius=15)

        self.lbl_guest_count = ctk.CTkLabel(
            card_guest,
            text="0",
            font=("Segoe UI", 24, "bold")
        )
        self.lbl_guest_count.pack(pady=(10, 0))

        ctk.CTkLabel(
            card_guest,
            text="👥 Khách"
        ).pack(pady=(0, 10))

        # Card Quan hệ
        card_relation = ctk.CTkFrame(stats, corner_radius=15)
        card_relation.pack(side="left", padx=10, pady=10)

        self.lbl_relation_count = ctk.CTkLabel(
            card_relation,
            text="0",
            font=("Segoe UI", 24, "bold")
        )
        self.lbl_relation_count.pack(pady=(10, 0))

        ctk.CTkLabel(
            card_relation,
            text="❤️ Quan hệ"
        ).pack(pady=(0, 10))

        # Card Fitness
        card_fitness = ctk.CTkFrame(stats, corner_radius=15)
        card_fitness.pack(side="left", padx=10, pady=10)

        self.lbl_fitness = ctk.CTkLabel(
            card_fitness,
            text="0",
            font=("Segoe UI", 24, "bold")
        )
        self.lbl_fitness.pack(pady=(10, 0))

        ctk.CTkLabel(
            card_fitness,
            text="🎯 Fitness"
        ).pack(pady=(0, 10))

        # Card Bàn
        card_table = ctk.CTkFrame(stats, corner_radius=15)
        card_table.pack(side="left", padx=10, pady=10)

        self.lbl_table_count = ctk.CTkLabel(
            card_table,
            text="3",
            font=("Segoe UI", 24, "bold")
        )
        self.lbl_table_count.pack(pady=(10, 0))

        ctk.CTkLabel(
            card_table,
            text="🪑 Bàn"
        ).pack(pady=(0, 10))

        main = ctk.CTkFrame(self.root)
        main.pack(fill="both", expand=True, padx=10, pady=10)

        left = ctk.CTkFrame(main)
        left.pack(side="left", fill="y", padx=5, pady=5)

        center = ctk.CTkFrame(main)
        center.pack(side="left", fill="y", padx=5, pady=5)

        right = ctk.CTkFrame(main)
        right.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        ctk.CTkLabel(left, text="👥 Quản lý khách", font=(
            "Segoe UI", 18, "bold")).pack(pady=10)

        self.entry_guest = ctk.CTkEntry(
            left, width=250, placeholder_text="Tên khách")
        self.entry_guest.pack(pady=5)

        ctk.CTkButton(
            left,
            text="➕ Thêm khách",
            fg_color="#3B82F6",
            hover_color="#2563EB",
            corner_radius=12,
            height=40,
            command=self.add_guest
        ).pack(pady=5)

        self.txt_guests = ctk.CTkTextbox(left, width=250, height=120)
        self.txt_guests.pack(pady=5)

        ctk.CTkButton(left, text="📋 Thêm danh sách",
                      command=self.add_guest_list).pack(pady=5)
        ctk.CTkButton(
            left,
            text="📂 Import CSV",
            command=self.import_csv
        ).pack(pady=5)
        ctk.CTkButton(left, text="🗑 Xóa khách",
                      command=self.remove_guest).pack(pady=5)

        guest_frame = ctk.CTkFrame(left)
        guest_frame.pack(fill="both", expand=True)

        guest_scroll = ttk.Scrollbar(
            guest_frame,
            orient="vertical"
        )

        self.tree_guest = ttk.Treeview(
            guest_frame,
            columns=("name",),
            show="headings",
            yscrollcommand=guest_scroll.set
        )

        guest_scroll.config(
            command=self.tree_guest.yview
        )

        self.tree_guest.heading(
            "name",
            text="Tên khách"
        )
        self.tree_guest.column(
            "name",
            width=220,
            anchor="w"
        )

        self.tree_guest.pack(
            side="left",
            fill="both",
            expand=True
        )

        guest_scroll.pack(
            side="right",
            fill="y"
        )

        ctk.CTkLabel(center, text="❤️ Quan hệ", font=(
            "Segoe UI", 18, "bold")).pack(pady=10)

        self.cb1 = ttk.Combobox(center, state="readonly")
        self.cb1.pack(fill="x", padx=5, pady=5)

        self.cb2 = ttk.Combobox(center, state="readonly")
        self.cb2.pack(fill="x", padx=5, pady=5)

        self.cb_relation = ttk.Combobox(
            center, state="readonly", values=list(RELATIONS.keys()))
        self.cb_relation.pack(fill="x", padx=5, pady=5)

        ctk.CTkButton(center, text="❤️ Thêm quan hệ",
                      command=self.add_relation).pack(pady=5)

        relation_frame = ctk.CTkFrame(center)
        relation_frame.pack(fill="both", expand=True)

        relation_scroll = ttk.Scrollbar(
            relation_frame,
            orient="vertical"
        )

        self.tree_relation = ttk.Treeview(
            relation_frame,
            columns=("g1", "g2", "rel", "score"),
            show="headings",
            yscrollcommand=relation_scroll.set
        )

        relation_scroll.config(
            command=self.tree_relation.yview
        )

        relation_scroll.pack(
            side="right",
            fill="y"
        )

        self.tree_relation.pack(
            side="left",
            fill="both",
            expand=True
        )
        for col, txt in [
            ("g1", "Khách 1"),
            ("g2", "Khách 2"),
            ("rel", "Quan hệ"),
            ("score", "Điểm")
        ]:
            self.tree_relation.heading(col, text=txt)

        self.tree_relation.column(
            "g1",
            width=120
        )

        self.tree_relation.column(
            "g2",
            width=120
        )

        self.tree_relation.column(
            "rel",
            width=120
        )

        self.tree_relation.column(
            "score",
            width=60,
            anchor="center"
        )

        ctk.CTkLabel(right, text="⚙️ Thuật toán GA", font=(
            "Segoe UI", 18, "bold")).pack(pady=10)

        param = ctk.CTkFrame(right)
        param.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(param, text="Số bàn").grid(
            row=0, column=0, padx=5, pady=5)
        self.ent_tables = ctk.CTkEntry(param, width=80)
        self.ent_tables.insert(0, "3")
        self.ent_tables.grid(row=0, column=1)

        ctk.CTkButton(
            param,
            text="▶ Chạy GA",
            fg_color="#10B981",
            hover_color="#059669",
            height=40,
            command=self.run_algorithm
        ).grid(
            row=0, column=2, padx=10)
        ctk.CTkButton(param, text="📈 Biểu đồ", command=self.show_chart).grid(
            row=0, column=3, padx=10)

        self.result_tree = ttk.Treeview(
            right,
            columns=("guest",),
            show="tree headings"
        )

        self.result_tree.heading(
            "#0",
            text="🪑 Bàn"
        )

        self.result_tree.heading(
            "guest",
            text="👤 Khách"
        )

        result_frame = ctk.CTkFrame(right)
        result_frame.pack(fill="both", expand=True, padx=10, pady=10)

        result_scroll = ttk.Scrollbar(
            result_frame,
            orient="vertical"
        )

        self.result_tree = ttk.Treeview(
            result_frame,
            columns=("guest",),
            show="tree headings",
            yscrollcommand=result_scroll.set
        )

        result_scroll.config(
            command=self.result_tree.yview
        )

        self.result_tree.heading("#0", text="Bàn")
        self.result_tree.heading("guest", text="Khách")

        self.result_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        result_scroll.pack(
            side="right",
            fill="y"
        )

        self.status_bar = ctk.CTkLabel(
            self.root,
            text="Sẵn sàng",
            anchor="w"
        )

        self.status_bar.pack(
            fill="x",
            padx=10,
            pady=5
        )
        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="white",
            foreground="black",
            fieldbackground="white",
            rowheight=28
        )
        style.map(
            "Treeview",
            background=[("selected", "#3B82F6")],
            foreground=[("selected", "white")]
        )

        style.configure(
            "Treeview.Heading",
            background="#2563EB",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )

    def update_stats(self):
        self.lbl_guest_count.configure(
            text=f"👥 Khách: {len(self.data.guests)}")
        self.lbl_relation_count.configure(
            text=f"❤️ Quan hệ: {len(self.data.relations)}")
        self.lbl_table_count.configure(
            text=self.ent_tables.get()
        )

    def refresh_guests(self):
        for item in self.tree_guest.get_children():
            self.tree_guest.delete(item)

        for g in self.data.guests:
            self.tree_guest.insert("", "end", values=(g,))

        self.cb1["values"] = self.data.guests
        self.cb2["values"] = self.data.guests
        self.update_stats()

    def add_guest(self):
        name = self.entry_guest.get().strip()

        if self.data.add_guest(name):
            self.refresh_guests()
            self.entry_guest.delete(0, tk.END)

    def add_guest_list(self):
        content = self.txt_guests.get("1.0", "end").strip()

        if not content:
            return

        names = re.split(r'[\n\r\t,;]+', content)

        for name in names:
            self.data.add_guest(name.strip())

        self.refresh_guests()
        self.txt_guests.delete("1.0", "end")

    def remove_guest(self):
        selected = self.tree_guest.selection()

        if not selected:
            return

        item = selected[0]
        guest = self.tree_guest.item(item, "values")[0]

        self.data.remove_guest(guest)
        self.refresh_guests()

    def add_relation(self):
        g1 = self.cb1.get()
        g2 = self.cb2.get()
        rel = self.cb_relation.get()

        if not g1 or not g2 or not rel:
            return

        self.data.add_relation(g1, g2, rel)

        for item in self.tree_relation.get_children():
            self.tree_relation.delete(item)

        for r in self.data.relations:
            self.tree_relation.insert("", "end",
                                      values=(r.guest1, r.guest2,
                                              r.relation_type, r.score))

        self.update_stats()

    def run_algorithm(self):
        if len(self.data.guests) < 2:
            messagebox.showwarning("Thông báo", "Cần ít nhất 2 khách")
            return

        matrix = self.data.build_matrix()

        solution, fitness, history = run_ga(
            relation_matrix=matrix,
            num_guests=len(self.data.guests),
            num_tables=int(self.ent_tables.get())
        )

        self.status_bar.configure(
            text="Đang tối ưu..."
        )
        self.status_bar.configure(
            text="Tối ưu hoàn tất"
        )

        self.history = history

        self.lbl_fitness.configure(
            text=f"{fitness}"
        )

        tables = decode_solution(
            solution,
            self.data.guests
        )

        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        for table_id, guests in tables.items():

            parent = self.result_tree.insert(
                "",
                "end",
                text=f"🪑 Bàn {table_id}"
            )

            for guest in guests:

                self.result_tree.insert(
                    parent,
                    "end",
                    text=f"👤 {guest}"
                )

    def show_chart(self):
        if not self.history:
            return

        plt.figure(figsize=(8, 4))
        plt.plot(self.history)
        plt.title("Fitness History")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.grid()
        plt.show()

    def import_csv(self):

        file_name = filedialog.askopenfilename(
            filetypes=[
                ("CSV Files", "*.csv")
            ]
        )

        if not file_name:
            return

        try:

            names, matrix = load_data(
                file_name
            )

            self.data.guests.clear()
            self.data.relations.clear()

            for name in names:
                self.data.add_guest(name)

            for i in range(len(names)):
                for j in range(i + 1, len(names)):

                    score = matrix[i][j]

                    if score > 0:

                        self.data.relations.append(
                            Relation(
                                names[i],
                                names[j],
                                "Import CSV",
                                score
                            )
                        )

            self.refresh_guests()

            self.tree_relation.delete(
                *self.tree_relation.get_children()
            )

            for r in self.data.relations:

                self.tree_relation.insert(
                    "",
                    "end",
                    values=(
                        r.guest1,
                        r.guest2,
                        r.relation_type,
                        r.score
                    )
                )

            self.update_stats()

            messagebox.showinfo(
                "Thành công",
                f"Đã import {len(names)} khách"
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )


if __name__ == "__main__":
    app = WeddingGAApp()
    app.root.mainloop()
