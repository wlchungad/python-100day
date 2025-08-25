import keyboard
from time import sleep
STD_UNIT = 10

reverseCommand = {
    "w": "s",
    "a": "d",
    "s": "w",
    "d": "a"
}

class MoveCommand:
    def __init__(self, shape, dx, dy):
        self.shape = shape
        self.dx = dx
        self.dy = dy
        self.undoStack = []
        self.redoStack = []
    
    def execute(self, direction : str):
        # assume direction is keyboard w/a/s/d
        # which comes from keyboard.read_key() / stack
        self.undoStack.insert(0, direction)
        match (direction):
            case "w": self.dy += STD_UNIT
            case "a": self.dx -= STD_UNIT
            case "s": self.dy -= STD_UNIT
            case "d": self.dx += STD_UNIT
        self.redoStack.clear()

    def undo(self):
        if not self.undoStack: return
        getUndoCommand = reverseCommand[self.undoStack.pop()] # reverse according to dictionary
        self.execute(getUndoCommand)
        self.redoStack.insert(0, getUndoCommand)

    def redo(self):
        if not self.redoStack(): return
        getRedoCommand = self.redoStack.pop()
        self.execute(getRedoCommand)
        self.undoStack.insert(0, getRedoCommand)

    def report(self):
        print(f"The {self.shape} is at X = {self.dx}, Y = {self.dy}")
        print(f"Undo stack: {self.undoStack}")
        print(f"Redo stack: {self.redoStack}")

def main():
    
    movableObject = MoveCommand("Circle",0,0)
    try:
        while True:
            key = keyboard.read_key()
            match (key):
                case 'p':
                    print("You pressed p")
                case key if key in ['w', 'a', 's', 'd']:
                    print(f"You pressed {key}")
                    movableObject.execute(key)
                case 'z':
                    print("Try to undo...")
                case 'y':
                    print("try to redo...")
                case 'c':
                    if str(input(("Termination confirmed?"))) in ["Y", "y"]:
                        break
            sleep(0.1)
    except KeyboardInterrupt:
        print("Forced Tetmination detected")        
    movableObject.report()
    return 0

if __name__ == "__main__":
    main()