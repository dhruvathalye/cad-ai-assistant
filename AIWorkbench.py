import FreeCADGui
import FreeCAD as App
import Part


class CreateBoxCommand:
    def GetResources(self):
        return {
            "MenuText": "Create Test Box",
            "ToolTip": "Creates a simple cube"
        }

    def Activated(self):
        doc = App.ActiveDocument

        if doc is None:
            doc = App.newDocument()

        box = doc.addObject("Part::Box", "TestBox")
        box.Length = 10
        box.Width = 10
        box.Height = 10

        doc.recompute()

    def IsActive(self):
        return True

class AskAICommand:
    def GetResources(self):
        return {
            "MenuText": "Ask AI",
            "ToolTip": "Generate FreeCAD geometry from a text prompt"
        }

    def Activated(self):
        from PySide import QtGui

        prompt, ok = QtGui.QInputDialog.getText(
            None,
            "Ask AI CAD Assistant",
            "Describe what you want to create:"
        )

        if not ok or not prompt:
            return

        QtGui.QMessageBox.information(
            None,
            "AI Prompt",
            "You asked:\n\n" + prompt
        )

    def IsActive(self):
        return True

FreeCADGui.addCommand("Create_Test_Box", CreateBoxCommand())


class AIWorkbench(FreeCADGui.Workbench):
    MenuText = "AI Assistant"
    ToolTip = "AI CAD Assistant Workbench"

    def Initialize(self):
        self.appendToolbar(
            "AI Tools",
            ["Create_Test_Box"]
        )

        self.appendMenu(
            "AI Tools",
            ["Create_Test_Box"]
        )

    def GetClassName(self):
        return "Gui::PythonWorkbench"
