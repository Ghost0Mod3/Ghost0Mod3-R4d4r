# gui/windows/unknown.py

import tkinter as tk
from tkinter import ttk


class UnknownWindow:

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
            "Unknown Network"
        )

        self.window.geometry(
            "700x750"
        )

        self.build_ui()

    def build_ui(self):

        title = tk.Label(
            self.window,
            text="Unknown Network",
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
                "UNKNOWN"
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
            "Confidence",
            "LOW",
            2
        )

        details_frame = ttk.LabelFrame(
            self.window,
            text="Target Details"
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

        investigation_frame = ttk.LabelFrame(
            self.window,
            text="Investigation"
        )

        investigation_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.add_row(
            investigation_frame,
            "Signal Quality",
            "Unknown",
            0
        )

        self.add_row(
            investigation_frame,
            "Potential Match",
            "None",
            1
        )

        self.add_row(
            investigation_frame,
            "Last Seen",
            "Now",
            2
        )

        self.add_row(
            investigation_frame,
            "Status",
            "Pending Review",
            3
        )

        notes_frame = ttk.LabelFrame(
            self.window,
            text="Classifier Notes"
        )

        notes_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        tk.Label(
            notes_frame,
            text="No Signature Match Found"
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        tk.Label(
            notes_frame,
            text="Manual Review Recommended"
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        tk.Label(
            notes_frame,
            text="Candidate For Future Classifier Rules"
        ).pack(
            anchor="w",
            padx=10,
            pady=2
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

        self.investigation_var = tk.BooleanVar(
            value=True
        )

        self.monitor_var = tk.BooleanVar(
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
            text="Investigation Mode",
            variable=self.investigation_var
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

        self.progress["value"] = 50

        actions_frame = ttk.LabelFrame(
            self.window,
            text="Discovery Actions"
        )

        actions_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.save_signature_var = tk.BooleanVar(
            value=True
        )

        self.learn_var = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            actions_frame,
            text="Save Signature",
            variable=self.save_signature_var
        ).pack(
            anchor="w",
            padx=10
        )

        ttk.Checkbutton(
            actions_frame,
            text="Learn New Category",
            variable=self.learn_var
        ).pack(
            anchor="w",
            padx=10
        )

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
            fg="orange",
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
            width=14,
            command=self.refresh
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Investigate",
            width=14,
            command=self.investigate
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Save Signature",
            width=14,
            command=self.save_signature
        ).pack(
            side=tk.LEFT,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Close",
            width=14,
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
            font=(
                "Arial",
                10,
                "bold"
            )
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
            "Unknown network refreshed"
        )

    def investigate(self):

        print(
            "Investigation started"
        )

    def save_signature(self):

        print(
            "Signature saved"
        )