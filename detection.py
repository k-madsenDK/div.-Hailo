import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib
from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import GStreamerDetectionApp

class user_app_callback_class(app_callback_class):
    def __init__(self):
        super().__init__()
        # more fields can be added if needed

def app_callback(pad, info, user_data):
    buffer = info.get_buffer()
    if buffer is None:
        return Gst.PadProbeReturn.OK
    user_data.increment()
    return Gst.PadProbeReturn.OK

def update_framecount_overlay(pipeline, user_data):
    overlay = pipeline.get_by_name("framecount_overlay")
    if overlay is not None:
        overlay.set_property(
            "text",
            f"Frame: {user_data.get_count()}"
        )
    return True

if __name__ == "__main__":
    user_data = user_app_callback_class()
    app = GStreamerDetectionApp(app_callback, user_data)
    GLib.timeout_add(100, update_framecount_overlay, app.pipeline, user_data)
    app.run()
