# div.-Hailo
Diverse hailo changed files
# Miscellaneous Utilities for Raspberry Pi 5 with Hailo Hat (Tachyon Device)

This repository contains various scripts and tools for use with the Raspberry Pi 5 equipped with a Hailo Hat, specifically for the Tachyon device. The utilities assist with setup, management, and demonstration tasks for this hardware combination.

## Overview

- Utilities and helpers specifically for the Raspberry Pi 5, Hailo Hat, and Tachyon device.
- Scripts may support device setup, testing, demonstration, or video analytics.
- Designed for flexibility and easy extension.

## Enabling Frame Count in Main Window

To enable the display of frame count in the main window of your detection application:

1. **Include the Required Detection Files**

   Make sure the following files are present:
   - `detection.py`
   - `detection_pipeline.py`

   Place them here:
   ```
   venv_hailo_rpi_examples/lib/python3.11/site-packages/hailo_apps/hailo_app_python/apps/detection/
   ```

   When these files are present, the application will be able to display the current frame count in the main window during detection.

2. **Using a Custom Start File**

   If you use a start file other than `madsen2.py`, you must include the following line in your start file to ensure that the frame count overlay updates properly:
   ```python
   if __name__ == "__main__":
    _maybe_init_gst()
    user_data = user_app_callback_class()
    app = DET_APP(app_callback, user_data)
    # Update textoverlay element (if present) every 100 ms
    GLib.timeout_add(100, update_framecount_overlay, app.pipeline, user_data) # <-- this has to be added
    app.run()
   ```
   This ensures that the frame count overlay is updated at regular intervals.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/k-madsenDK/div.-Hailo.git
   ```

2. **Follow the steps above to enable frame count if needed.**

3. **Explore the available utilities:**  
   Browse the repository to find scripts and tools relevant to your needs. Each tool may include its own documentation or usage notes.

4. **Dependencies:**  
   Please refer to each script’s header or README section for installation instructions and required dependencies, as these may vary.

## Contributing

Contributions are welcome! If you have a useful script or improvement for the Raspberry Pi 5, Hailo Hat, or Tachyon device, feel free to open a pull request or submit an issue.

## License

This repository is licensed under the MIT License.

---

*For more information about the Raspberry Pi 5, the Hailo Hat, or the Tachyon device, please refer to their official documentation or contact the repository maintainer.*
