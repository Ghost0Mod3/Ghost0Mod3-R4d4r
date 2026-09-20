import tkinter as tk
from tkinter import ttk


class GeneralWindow:

    def __init__(
        self,
        parent,
        target
    ):

        self.target = target

        self.window = tk.Toplevel(
            parent
        )

        self.window.title(
            "General Network"
        )

        self.window.geometry(
            "700x700"
        )

        self.build_ui()

    def build_ui(self):

        title = tk.Label(
            self.window,
            text="General Network",
            font=(
                "Arial",
                18,
                "bold"
            )
        )

        title.pack(
            pady=10
        )

        classification_frame = ttk.LabelFrame(
            self.window,
            text="Classification"
        )

        classification_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.add_row(
            classification_frame,
            "Category",
            self.target.get(
                "category",
                "GENERAL"
            ),
            0
        )

        self.add_row(
            classification_frame,
            "Risk",
            self.target.get(
                "risk",
                "Unknown"
            ),
            1
        )

        self.add_row(
            classification_frame,
            "Profile",
            "Standard",
            2
        )

        details_frame = ttk.LabelFrame(
            self.window,
            text="Network Details"
        )

        details_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.add_row(
            details_frame,
            "SSID",
            self.target.get(
                "ssid",
                "Unknown"
            ),
            0
        )

        self.add_row(
            details_frame,
            "BSSID",
            self.target.get(
                "bssid",
                "Unknown"
            ),
            1
        )

        self.add_row(
            details_frame,
            "RSSI",
            self.target.get(
                "rssi",
                "Unknown"
            ),
            2
        )

        self.add_row(
            details_frame,
            "Channel",
            self.target.get(
                "channel",
                "Unknown"
            ),
            3
        )

        self.add_row(
            details_frame,
            "Security",
            self.target.get(
                "crypto",
                "Unknown"
            ),
            4
        )

        analysis_frame = ttk.LabelFrame(
            self.window,
            text="Network Analysis"
        )

        analysis_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.add_row(
            analysis_frame,
            "Signal Quality",
            "Good",
            0
        )

        self.add_row(
            analysis_frame,
            "Risk Score",
            self.target.get(
                "risk",
                "Unknown"
            ),
            1
        )

        self.add_row(
            analysis_frame,
            "Last Seen",
            "Now",
            2
        )

        self.add_row(
            analysis_frame,
            "Status",
            "Detected",
            3
        )

        monitor_frame = ttk.LabelFrame(
            self.window,
            text="Monitoring"
        )

        monitor_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.audio_var = tk.BooleanVar(
            value=True
        )

        self.rssi_var = tk.BooleanVar(
            value=True
        )

        self.monitor_var = tk.BooleanVar(
            value=True
        )

        self.refresh_var = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            monitor_frame,
            text="Audio Alerts",
            variable=self.audio_var
        ).pack(
            anchor="w",
            padx=10
        )

        ttk.Checkbutton(
            monitor_frame,
            text="RSSI Alerts",
            variable=self.rssi_var
        ).pack(
            anchor="w",
            padx=10
        )

        ttk.Checkbutton(
            monitor_frame,
            text="Continuous Monitoring",
            variable=self.monitor_var
        ).pack(
            anchor="w",
            padx=10
        )

        ttk.Checkbutton(
            monitor_frame,
            text="Auto Refresh",
            variable=self.refresh_var
        ).pack(
            anchor="w",
            padx=10
        )

        signal_frame = ttk.LabelFrame(
            self.window,
            text="Signal Strength"
        )

        signal_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.progress = ttk.Progressbar(
            signal_frame,
            orient="horizontal",
            length=500,
            mode="determinate"
        )

        self.progress.pack(
            padx=10,
            pady=5
        )

        self.progress["value"] = 60

        status_frame = ttk.LabelFrame(
            self.window,
            text="Tracking Status"
        )

        status_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.status_label = tk.Label(
            status_frame,
            text="ACTIVE",
            fg="green",
            font=(
                "Arial",
                12,
                "bold"
            )
        )

        self.status_label.pack(
            pady=5
        )

        button_frame = tk.Frame(
            self.window
        )

        button_frame.pack(
            pady=15
        )

        tk.Button(
            button_frame,
            text="Refresh",
            width=12,
            command=self.refresh
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Monitor",
            width=12,
            command=self.monitor
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Close",
            width=12,
            command=self.window.destroy
        ).pack(
            side=tk.LEFT,
            padx=5
        )

    def add_row(
        self,
        parent,
        label,
        value,
        row
    ):

        tk.Label(
            parent,
            text=f"{label}:",
            font=("Arial", 10, "bold")
        ).grid(
            row=row,
            column=0,
            padx=10,
            pady=4,
            sticky="w"
        )

        tk.Label(
            parent,
            text=str(value)
        ).grid(
            row=row,
            column=1,
            padx=10,
            pady=4,
            sticky="w"
        )

    def refresh(self):

        print(
            "General window refreshed"
        )

    def monitor(self):

        print(
            "General monitoring enabled"
        )