"""
Test backup creation
"""

import pytest
from PyQt6 import QtCore
from vorta.store.models import ArchiveModel, EventLogModel


def test_create(qapp, qtbot):
    """Test for manual archive creation"""
    main = qapp.main_window
    main.archiveTab.refresh_archive_list()
    qtbot.waitUntil(lambda: main.archiveTab.archiveTable.rowCount() > 0, **pytest._wait_defaults)

    qtbot.mouseClick(main.createStartBtn, QtCore.Qt.MouseButton.LeftButton)
    qtbot.waitUntil(lambda: 'Backup finished.' in main.progressText.text(), **pytest._wait_defaults)
    qtbot.waitUntil(lambda: main.createStartBtn.isEnabled(), **pytest._wait_defaults)

    assert EventLogModel.select().count() == 2
    assert ArchiveModel.select().count() == 7
    assert main.createStartBtn.isEnabled()
    assert main.archiveTab.archiveTable.rowCount() == 7
    assert main.scheduleTab.logTableWidget.rowCount() == 2