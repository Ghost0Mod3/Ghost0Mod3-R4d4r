from gui.windows.flock import FlockWindow
from gui.windows.camera import CameraWindow
from gui.windows.police import PoliceWindow
from gui.windows.general import GeneralWindow
from gui.windows.unknown import UnknownWindow


def open_category_window(
    parent,
    target
):

    category = target.get(
        "category",
        "UNKNOWN"
    )

    if category == "FLOCK":

        FlockWindow(
            parent,
            target
        )

    elif category == "CAMERA":

        CameraWindow(
            parent,
            target
        )

    elif category == "POLICE":

        PoliceWindow(
            parent,
            target
        )

    elif category == "GENERAL":

        GeneralWindow(
            parent,
            target
        )

    else:

        UnknownWindow(
            parent,
            target
        )