from logger_tt import logger

from PySide6.QtWidgets import QFrame, QHBoxLayout

from model.animation_label import AnimationLabel


class Status:
    """
    This class controls the layout and functionality for
    the Status view on the bottom of the GUI.
    """

    def __init__(self) -> None:
        """
        Initialize the Status view. Construct the layout
        add the single fading text widget.
        """
        logger.info("Starting Status view initialization")

        # This view is contained within a QFrame to allow for styling
        self.frame = QFrame()
        self.frame.setObjectName("StatusPanel")

        # Create the main layout for the view
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(10, 1, 0, 2)

        # The main layout is contained inside the QFrame
        self.frame.setLayout(self.layout)

        # Create the single fading text widget
        self.status_text = AnimationLabel()
        self.status_text.setObjectName("StatusLabel")

        # Add the widget to the base layout
        self.layout.addWidget(self.status_text)

        logger.info("Finished Status view initialization")

    def actions_slot(self, action: str) -> None:
        """
        Slot connecting to the action panel's `actions_signal`.
        Responsible for displaying the action that was just
        triggered on the bottom status bar and fading the text
        after some time.

        :param action: the specific action being triggered
        """
        logger.info(f"Displaying fading text for action: {action}")
        if action == "clear":
            self.status_text.start_pause_fade("Cleared active mods")
        if action == "restore":
            self.status_text.start_pause_fade(
                "Restored mod list to last saved ModsConfig.xml state"
            )
        if action == "sort":
            self.status_text.start_pause_fade("Sorted active mod list!")
        if action == "import":
            self.status_text.start_pause_fade("Imported mod list from external file!")
        if action == "export":
            self.status_text.start_pause_fade("Exported active mods to external file!")
        if action == "save":
            self.status_text.start_pause_fade("Active mods saved into ModsConfig.xml!")
        if action == "run":
            self.status_text.start_pause_fade("Starting RimWorld!")
        if action == "runArgs":
            self.status_text.start_pause_fade("Editing configured run arguments...")
        if action == "edit_steam_apikey":
            self.status_text.start_pause_fade("Editing configured Steam API key...")
