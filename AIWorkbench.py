import FreeCAD
import FreeCADGui
import Part


class CreateBoxCommand:
    def GetResources(self):
        return {
            "MenuText": "Create Test Box",
            "ToolTip": "Create a simple test box",
        }

    def Activated(self):
        doc = FreeCAD.ActiveDocument

        if doc is None:
            doc = FreeCAD.newDocument("Cad_AI_Test")

        box = Part.makeBox(20, 20, 20)

        obj = doc.addObject("Part::Feature", "AI_Test_Box")
        obj.Shape = box

        doc.recompute()

    def IsActive(self):
        return True
    
class AskAICommand:
    def GetResources(self):
        return {
            "MenuText": "Ask AI",
            "ToolTip": "Generate CAD from a text prompt",
        }

    def Activated(self):
        from PySide import QtGui

        prompt, ok = QtGui.QInputDialog.getText(
            None,
            "CAD AI Assistant",
            "Describe the part you want to create:"
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

class CadAIWorkbench(FreeCADGui.Workbench):
    MenuText = "CAD AI Assistant"
    ToolTip = "AI assistant for FreeCAD"

    def Initialize(self):
        FreeCADGui.addCommand(
            "Create_Test_Box",
            CreateBoxCommand()
        )

        FreeCADGui.addCommand(
            "Ask_AI",
            AskAICommand()
        )

        self.appendToolbar(
            "CAD AI Tools",
            ["Create_Test_Box", "Ask_AI"]
        )   

        self.appendMenu(
             "CAD AI Tools",
             ["Create_Test_Box", "Ask_AI"]
)

    def GetClassName(self):
        return "Gui::PythonWorkbench"