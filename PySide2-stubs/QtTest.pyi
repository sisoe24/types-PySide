from typing import overload
import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtWidgets
import shiboken2
import typing
T = typing.TypeVar('T')

class QTest(shiboken2.Object):
    class KeyAction:
        Click: typing.ClassVar[QTest.KeyAction] = ...
        Press: typing.ClassVar[QTest.KeyAction] = ...
        Release: typing.ClassVar[QTest.KeyAction] = ...
        Shortcut: typing.ClassVar[QTest.KeyAction] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __and__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __rand__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __rmul__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __ror__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __rsub__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __rxor__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __sub__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...
        def __xor__(self, other: typing.SupportsInt) -> QTest.KeyAction: ...

    class MouseAction:
        MouseClick: typing.ClassVar[QTest.MouseAction] = ...
        MouseDClick: typing.ClassVar[QTest.MouseAction] = ...
        MouseMove: typing.ClassVar[QTest.MouseAction] = ...
        MousePress: typing.ClassVar[QTest.MouseAction] = ...
        MouseRelease: typing.ClassVar[QTest.MouseAction] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __and__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __rand__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __rmul__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __ror__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __rsub__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __rxor__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __sub__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...
        def __xor__(self, other: typing.SupportsInt) -> QTest.MouseAction: ...

    class QBenchmarkMetric:
        AlignmentFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        BitsPerSecond: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        BranchInstructions: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        BranchMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        BusCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        BytesAllocated: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        BytesPerSecond: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CPUCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CPUMigrations: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CPUTicks: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CacheMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CachePrefetchMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CachePrefetches: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CacheReadMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CacheReads: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CacheReferences: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CacheWriteMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        CacheWrites: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        ContextSwitches: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        EmulationFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        Events: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        FramesPerSecond: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        InstructionReads: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        Instructions: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        MajorPageFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        MinorPageFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        PageFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        RefCPUCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        StalledCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        WalltimeMilliseconds: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        WalltimeNanoseconds: typing.ClassVar[QTest.QBenchmarkMetric] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __and__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __rand__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __rmul__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __ror__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __rsub__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __rxor__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __sub__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...
        def __xor__(self, other: typing.SupportsInt) -> QTest.QBenchmarkMetric: ...

    class QTouchEventSequence(shiboken2.Object):
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def commit(self, processEvents: bool = ...) -> None: ...
        @overload
        def move(self, touchId: int, pt: PySide2.QtCore.QPoint, widget: typing.Optional[PySide2.QtWidgets.QWidget] = ...) -> QTest.QTouchEventSequence: ...
        @overload
        def move(self, touchId: int, pt: PySide2.QtCore.QPoint, window: typing.Optional[PySide2.QtGui.QWindow] = ...) -> QTest.QTouchEventSequence: ...
        @overload
        def press(self, touchId: int, pt: PySide2.QtCore.QPoint, widget: typing.Optional[PySide2.QtWidgets.QWidget] = ...) -> QTest.QTouchEventSequence: ...
        @overload
        def press(self, touchId: int, pt: PySide2.QtCore.QPoint, window: typing.Optional[PySide2.QtGui.QWindow] = ...) -> QTest.QTouchEventSequence: ...
        @overload
        def release(self, touchId: int, pt: PySide2.QtCore.QPoint, widget: typing.Optional[PySide2.QtWidgets.QWidget] = ...) -> QTest.QTouchEventSequence: ...
        @overload
        def release(self, touchId: int, pt: PySide2.QtCore.QPoint, window: typing.Optional[PySide2.QtGui.QWindow] = ...) -> QTest.QTouchEventSequence: ...
        def stationary(self, touchId: int) -> QTest.QTouchEventSequence: ...

    class TestFailMode:
        Abort: typing.ClassVar[QTest.TestFailMode] = ...
        Continue: typing.ClassVar[QTest.TestFailMode] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __and__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __rand__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __rmul__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __ror__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __rsub__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __rxor__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __sub__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
        def __xor__(self, other: typing.SupportsInt) -> QTest.TestFailMode: ...
    Abort: typing.ClassVar[QTest.TestFailMode] = ...
    AlignmentFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    BitsPerSecond: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    BranchInstructions: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    BranchMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    BusCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    BytesAllocated: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    BytesPerSecond: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CPUCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CPUMigrations: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CPUTicks: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CacheMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CachePrefetchMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CachePrefetches: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CacheReadMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CacheReads: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CacheReferences: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CacheWriteMisses: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    CacheWrites: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    Click: typing.ClassVar[QTest.KeyAction] = ...
    ContextSwitches: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    Continue: typing.ClassVar[QTest.TestFailMode] = ...
    EmulationFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    Events: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    FramesPerSecond: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    InstructionReads: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    Instructions: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    MajorPageFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    MinorPageFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    MouseClick: typing.ClassVar[QTest.MouseAction] = ...
    MouseDClick: typing.ClassVar[QTest.MouseAction] = ...
    MouseMove: typing.ClassVar[QTest.MouseAction] = ...
    MousePress: typing.ClassVar[QTest.MouseAction] = ...
    MouseRelease: typing.ClassVar[QTest.MouseAction] = ...
    PageFaults: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    Press: typing.ClassVar[QTest.KeyAction] = ...
    RefCPUCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    Release: typing.ClassVar[QTest.KeyAction] = ...
    Shortcut: typing.ClassVar[QTest.KeyAction] = ...
    StalledCycles: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    WalltimeMilliseconds: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    WalltimeNanoseconds: typing.ClassVar[QTest.QBenchmarkMetric] = ...
    mouseDoubleClickInterval: typing.ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def addColumnInternal(cls, id: int, name: bytes) -> None: ...
    @classmethod
    def asciiToKey(cls, ascii: int) -> PySide2.QtCore.Qt.Key: ...
    @classmethod
    def compare_ptr_helper(cls, t1: int, t2: int, actual: bytes, expected: bytes, file: bytes, line: int) -> bool: ...
    @classmethod
    def compare_string_helper(cls, t1: bytes, t2: bytes, actual: bytes, expected: bytes, file: bytes, line: int) -> bool: ...
    @classmethod
    def createTouchDevice(cls, devType: PySide2.QtGui.QTouchDevice.DeviceType = ...) -> PySide2.QtGui.QTouchDevice: ...
    @classmethod
    def currentAppName(cls) -> bytes: ...
    @classmethod
    def currentDataTag(cls) -> bytes: ...
    @classmethod
    def currentTestFailed(cls) -> bool: ...
    @classmethod
    def currentTestFunction(cls) -> bytes: ...
    @overload
    @classmethod
    def ignoreMessage(cls, type: PySide2.QtCore.QtMsgType, message: bytes) -> None: ...
    @overload
    @classmethod
    def ignoreMessage(cls, type: PySide2.QtCore.QtMsgType, messagePattern: PySide2.QtCore.QRegularExpression) -> None: ...
    @overload
    @classmethod
    def keyClick(cls, widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyClick(cls, widget: PySide2.QtWidgets.QWidget, key: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyClick(cls, window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyClick(cls, window: PySide2.QtGui.QWindow, key: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @classmethod
    def keyClicks(cls, widget: PySide2.QtWidgets.QWidget, sequence: str, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyEvent(cls, action: QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, ascii: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyEvent(cls, action: QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyEvent(cls, action: QTest.KeyAction, window: PySide2.QtGui.QWindow, ascii: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyEvent(cls, action: QTest.KeyAction, window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyPress(cls, widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyPress(cls, widget: PySide2.QtWidgets.QWidget, key: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyPress(cls, window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyPress(cls, window: PySide2.QtGui.QWindow, key: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyRelease(cls, widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyRelease(cls, widget: PySide2.QtWidgets.QWidget, key: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyRelease(cls, window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keyRelease(cls, window: PySide2.QtGui.QWindow, key: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def keySequence(cls, widget: PySide2.QtWidgets.QWidget, keySequence: typing.Union[PySide2.QtGui.QKeySequence,str]) -> None: ...
    @overload
    @classmethod
    def keySequence(cls, window: PySide2.QtGui.QWindow, keySequence: typing.Union[PySide2.QtGui.QKeySequence,str]) -> None: ...
    @classmethod
    def keyToAscii(cls, key: PySide2.QtCore.Qt.Key) -> int: ...
    @overload
    @classmethod
    def mouseClick(cls, widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseClick(cls, window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseDClick(cls, widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseDClick(cls, window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseEvent(cls, action: QTest.MouseAction, widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], pos: PySide2.QtCore.QPoint, delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseEvent(cls, action: QTest.MouseAction, window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], pos: PySide2.QtCore.QPoint, delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseMove(cls, widget: PySide2.QtWidgets.QWidget, pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseMove(cls, window: PySide2.QtGui.QWindow, pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mousePress(cls, widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mousePress(cls, window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseRelease(cls, widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @overload
    @classmethod
    def mouseRelease(cls, window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier] = ..., pos: PySide2.QtCore.QPoint = ..., delay: int = ...) -> None: ...
    @classmethod
    def qCleanup(cls) -> None: ...
    @classmethod
    def qElementData(cls, elementName: bytes, metaTypeId: int) -> int: ...
    @classmethod
    def qExpectFail(cls, dataIndex: bytes, comment: bytes, mode: QTest.TestFailMode, file: bytes, line: int) -> bool: ...
    @overload
    @classmethod
    def qFindTestData(cls, basepath: str, file: typing.Optional[bytes] = ..., line: int = ..., builddir: typing.Optional[bytes] = ...) -> str: ...
    @overload
    @classmethod
    def qFindTestData(cls, basepath: bytes, file: typing.Optional[bytes] = ..., line: int = ..., builddir: typing.Optional[bytes] = ...) -> str: ...
    @classmethod
    def qGlobalData(cls, tagName: bytes, typeId: int) -> int: ...
    @classmethod
    def qRun(cls) -> int: ...
    @classmethod
    def qSkip(cls, message: bytes, file: bytes, line: int) -> None: ...
    @classmethod
    def qWaitForWindowActive(cls, widget: PySide2.QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    @classmethod
    def qWaitForWindowExposed(cls, widget: PySide2.QtWidgets.QWidget, timeout: int = ...) -> bool: ...
    @overload
    @classmethod
    def sendKeyEvent(cls, action: QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, code: PySide2.QtCore.Qt.Key, ascii: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], delay: int = ...) -> None: ...
    @overload
    @classmethod
    def sendKeyEvent(cls, action: QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, code: PySide2.QtCore.Qt.Key, text: str, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], delay: int = ...) -> None: ...
    @overload
    @classmethod
    def sendKeyEvent(cls, action: QTest.KeyAction, window: PySide2.QtGui.QWindow, code: PySide2.QtCore.Qt.Key, ascii: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], delay: int = ...) -> None: ...
    @overload
    @classmethod
    def sendKeyEvent(cls, action: QTest.KeyAction, window: PySide2.QtGui.QWindow, code: PySide2.QtCore.Qt.Key, text: str, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], delay: int = ...) -> None: ...
    @classmethod
    def setBenchmarkResult(cls, result: float, metric: QTest.QBenchmarkMetric) -> None: ...
    @classmethod
    def setMainSourcePath(cls, file: bytes, builddir: typing.Optional[bytes] = ...) -> None: ...
    @overload
    @classmethod
    def simulateEvent(cls, widget: PySide2.QtWidgets.QWidget, press: bool, code: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], text: str, repeat: bool, delay: int = ...) -> None: ...
    @overload
    @classmethod
    def simulateEvent(cls, window: PySide2.QtGui.QWindow, press: bool, code: int, modifier: typing.Union[PySide2.QtCore.Qt.KeyboardModifiers,PySide2.QtCore.Qt.KeyboardModifier], text: str, repeat: bool, delay: int = ...) -> None: ...
    @classmethod
    def testObject(cls) -> PySide2.QtCore.QObject: ...
    @classmethod
    def toPrettyCString(cls, unicode: bytes, length: int) -> bytes: ...
    @overload
    @classmethod
    def touchEvent(cls, widget: PySide2.QtWidgets.QWidget, device: PySide2.QtGui.QTouchDevice, autoCommit: bool = ...) -> QTest.QTouchEventSequence: ...
    @overload
    @classmethod
    def touchEvent(cls, window: PySide2.QtGui.QWindow, device: PySide2.QtGui.QTouchDevice, autoCommit: bool = ...) -> QTest.QTouchEventSequence: ...
