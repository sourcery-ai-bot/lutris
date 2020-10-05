# Standard Library
from gettext import gettext as _

from lutris.gui.config import DIALOG_HEIGHT
from lutris.gui.config import DIALOG_WIDTH
from lutris.gui.config.common import GameDialogCommon
from lutris.gui.dialogs import Dialog

# Lutris Modules


class EditGameConfigDialog(Dialog, GameDialogCommon):
    """Game config edit dialog."""

    def __init__(self, parent, game):
        super().__init__(_("Configure %s") % game.name, parent=parent)
        self.game = game
        self.lutris_config = game.config
        self.slug = game.slug
        self.runner_name = game.runner_name

        self.set_default_size(DIALOG_WIDTH, DIALOG_HEIGHT)

        self.build_notebook()
        self.build_tabs("game")
        self.build_action_area(self.on_save)
        self.connect("delete-event", self.on_cancel_clicked)
        self.show_all()
