from typing import overload
import PySide2.QtCore
import PySide2.QtGui
import PySide2.QtQml
import PySide2.QtQuick
import PySide2.QtWidgets
import typing
T = typing.TypeVar('T')

class QQuickWidget(PySide2.QtWidgets.QWidget):
    class ResizeMode:
        SizeRootObjectToView: typing.ClassVar[QQuickWidget.ResizeMode] = ...
        SizeViewToRootObject: typing.ClassVar[QQuickWidget.ResizeMode] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __and__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __rand__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __rmul__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __ror__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __rsub__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __rxor__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __sub__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...
        def __xor__(self, other: typing.SupportsInt) -> QQuickWidget.ResizeMode: ...

    class Status:
        Error: typing.ClassVar[QQuickWidget.Status] = ...
        Loading: typing.ClassVar[QQuickWidget.Status] = ...
        Null: typing.ClassVar[QQuickWidget.Status] = ...
        Ready: typing.ClassVar[QQuickWidget.Status] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __and__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __rand__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __rmul__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __ror__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __rsub__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __rxor__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __sub__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
        def __xor__(self, other: typing.SupportsInt) -> QQuickWidget.Status: ...
    Error: typing.ClassVar[QQuickWidget.Status] = ...
    Loading: typing.ClassVar[QQuickWidget.Status] = ...
    Null: typing.ClassVar[QQuickWidget.Status] = ...
    Ready: typing.ClassVar[QQuickWidget.Status] = ...
    SizeRootObjectToView: typing.ClassVar[QQuickWidget.ResizeMode] = ...
    SizeViewToRootObject: typing.ClassVar[QQuickWidget.ResizeMode] = ...
    sceneGraphError: typing.ClassVar[PySide2.QtCore.Signal] = ...
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    statusChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    @overload
    def __init__(self, engine: PySide2.QtQml.QQmlEngine, parent: typing.Union[PySide2.QtWidgets.QWidget,None], acceptDrops: bool = ..., accessibleDescription: str = ..., accessibleName: str = ..., autoFillBackground: bool = ..., baseSize: PySide2.QtCore.QSize = ..., childrenRect: PySide2.QtCore.QRect = ..., childrenRegion: PySide2.QtGui.QRegion = ..., contextMenuPolicy: PySide2.QtCore.Qt.ContextMenuPolicy = ..., cursor: typing.Union[PySide2.QtGui.QCursor,PySide2.QtCore.Qt.CursorShape] = ..., customContextMenuRequested: typing.Callable[..., typing.Any] = ..., destroyed: typing.Callable[..., typing.Any] = ..., enabled: bool = ..., focus: bool = ..., focusPolicy: PySide2.QtCore.Qt.FocusPolicy = ..., font: PySide2.QtGui.QFont = ..., frameGeometry: PySide2.QtCore.QRect = ..., frameSize: PySide2.QtCore.QSize = ..., fullScreen: bool = ..., geometry: PySide2.QtCore.QRect = ..., height: int = ..., inputMethodHints: typing.Union[PySide2.QtCore.Qt.InputMethodHints,PySide2.QtCore.Qt.InputMethodHint] = ..., isActiveWindow: bool = ..., layoutDirection: PySide2.QtCore.Qt.LayoutDirection = ..., locale: PySide2.QtCore.QLocale = ..., maximized: bool = ..., maximumHeight: int = ..., maximumSize: PySide2.QtCore.QSize = ..., maximumWidth: int = ..., minimized: bool = ..., minimumHeight: int = ..., minimumSize: PySide2.QtCore.QSize = ..., minimumSizeHint: PySide2.QtCore.QSize = ..., minimumWidth: int = ..., modal: bool = ..., mouseTracking: bool = ..., normalGeometry: PySide2.QtCore.QRect = ..., objectName: str = ..., objectNameChanged: typing.Callable[..., typing.Any] = ..., palette: PySide2.QtGui.QPalette = ..., pos: PySide2.QtCore.QPoint = ..., rect: PySide2.QtCore.QRect = ..., resizeMode: QQuickWidget.ResizeMode = ..., sceneGraphError: typing.Callable[..., typing.Any] = ..., size: PySide2.QtCore.QSize = ..., sizeHint: PySide2.QtCore.QSize = ..., sizeIncrement: PySide2.QtCore.QSize = ..., sizePolicy: PySide2.QtWidgets.QSizePolicy = ..., source: PySide2.QtCore.QUrl = ..., status: QQuickWidget.Status = ..., statusChanged: typing.Callable[..., typing.Any] = ..., statusTip: str = ..., styleSheet: str = ..., tabletTracking: bool = ..., toolTip: str = ..., toolTipDuration: int = ..., updatesEnabled: bool = ..., visible: bool = ..., whatsThis: str = ..., width: int = ..., windowFilePath: str = ..., windowIcon: PySide2.QtGui.QIcon = ..., windowIconChanged: typing.Callable[..., typing.Any] = ..., windowIconText: str = ..., windowIconTextChanged: typing.Callable[..., typing.Any] = ..., windowModality: PySide2.QtCore.Qt.WindowModality = ..., windowModified: bool = ..., windowOpacity: float = ..., windowTitle: str = ..., windowTitleChanged: typing.Callable[..., typing.Any] = ..., x: int = ..., y: int = ...) -> None: ...
    @overload
    def __init__(self, source: PySide2.QtCore.QUrl, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ..., acceptDrops: bool = ..., accessibleDescription: str = ..., accessibleName: str = ..., autoFillBackground: bool = ..., baseSize: PySide2.QtCore.QSize = ..., childrenRect: PySide2.QtCore.QRect = ..., childrenRegion: PySide2.QtGui.QRegion = ..., contextMenuPolicy: PySide2.QtCore.Qt.ContextMenuPolicy = ..., cursor: typing.Union[PySide2.QtGui.QCursor,PySide2.QtCore.Qt.CursorShape] = ..., customContextMenuRequested: typing.Callable[..., typing.Any] = ..., destroyed: typing.Callable[..., typing.Any] = ..., enabled: bool = ..., focus: bool = ..., focusPolicy: PySide2.QtCore.Qt.FocusPolicy = ..., font: PySide2.QtGui.QFont = ..., frameGeometry: PySide2.QtCore.QRect = ..., frameSize: PySide2.QtCore.QSize = ..., fullScreen: bool = ..., geometry: PySide2.QtCore.QRect = ..., height: int = ..., inputMethodHints: typing.Union[PySide2.QtCore.Qt.InputMethodHints,PySide2.QtCore.Qt.InputMethodHint] = ..., isActiveWindow: bool = ..., layoutDirection: PySide2.QtCore.Qt.LayoutDirection = ..., locale: PySide2.QtCore.QLocale = ..., maximized: bool = ..., maximumHeight: int = ..., maximumSize: PySide2.QtCore.QSize = ..., maximumWidth: int = ..., minimized: bool = ..., minimumHeight: int = ..., minimumSize: PySide2.QtCore.QSize = ..., minimumSizeHint: PySide2.QtCore.QSize = ..., minimumWidth: int = ..., modal: bool = ..., mouseTracking: bool = ..., normalGeometry: PySide2.QtCore.QRect = ..., objectName: str = ..., objectNameChanged: typing.Callable[..., typing.Any] = ..., palette: PySide2.QtGui.QPalette = ..., pos: PySide2.QtCore.QPoint = ..., rect: PySide2.QtCore.QRect = ..., resizeMode: QQuickWidget.ResizeMode = ..., sceneGraphError: typing.Callable[..., typing.Any] = ..., size: PySide2.QtCore.QSize = ..., sizeHint: PySide2.QtCore.QSize = ..., sizeIncrement: PySide2.QtCore.QSize = ..., sizePolicy: PySide2.QtWidgets.QSizePolicy = ..., status: QQuickWidget.Status = ..., statusChanged: typing.Callable[..., typing.Any] = ..., statusTip: str = ..., styleSheet: str = ..., tabletTracking: bool = ..., toolTip: str = ..., toolTipDuration: int = ..., updatesEnabled: bool = ..., visible: bool = ..., whatsThis: str = ..., width: int = ..., windowFilePath: str = ..., windowIcon: PySide2.QtGui.QIcon = ..., windowIconChanged: typing.Callable[..., typing.Any] = ..., windowIconText: str = ..., windowIconTextChanged: typing.Callable[..., typing.Any] = ..., windowModality: PySide2.QtCore.Qt.WindowModality = ..., windowModified: bool = ..., windowOpacity: float = ..., windowTitle: str = ..., windowTitleChanged: typing.Callable[..., typing.Any] = ..., x: int = ..., y: int = ...) -> None: ...
    @overload
    def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ..., acceptDrops: bool = ..., accessibleDescription: str = ..., accessibleName: str = ..., autoFillBackground: bool = ..., baseSize: PySide2.QtCore.QSize = ..., childrenRect: PySide2.QtCore.QRect = ..., childrenRegion: PySide2.QtGui.QRegion = ..., contextMenuPolicy: PySide2.QtCore.Qt.ContextMenuPolicy = ..., cursor: typing.Union[PySide2.QtGui.QCursor,PySide2.QtCore.Qt.CursorShape] = ..., customContextMenuRequested: typing.Callable[..., typing.Any] = ..., destroyed: typing.Callable[..., typing.Any] = ..., enabled: bool = ..., focus: bool = ..., focusPolicy: PySide2.QtCore.Qt.FocusPolicy = ..., font: PySide2.QtGui.QFont = ..., frameGeometry: PySide2.QtCore.QRect = ..., frameSize: PySide2.QtCore.QSize = ..., fullScreen: bool = ..., geometry: PySide2.QtCore.QRect = ..., height: int = ..., inputMethodHints: typing.Union[PySide2.QtCore.Qt.InputMethodHints,PySide2.QtCore.Qt.InputMethodHint] = ..., isActiveWindow: bool = ..., layoutDirection: PySide2.QtCore.Qt.LayoutDirection = ..., locale: PySide2.QtCore.QLocale = ..., maximized: bool = ..., maximumHeight: int = ..., maximumSize: PySide2.QtCore.QSize = ..., maximumWidth: int = ..., minimized: bool = ..., minimumHeight: int = ..., minimumSize: PySide2.QtCore.QSize = ..., minimumSizeHint: PySide2.QtCore.QSize = ..., minimumWidth: int = ..., modal: bool = ..., mouseTracking: bool = ..., normalGeometry: PySide2.QtCore.QRect = ..., objectName: str = ..., objectNameChanged: typing.Callable[..., typing.Any] = ..., palette: PySide2.QtGui.QPalette = ..., pos: PySide2.QtCore.QPoint = ..., rect: PySide2.QtCore.QRect = ..., resizeMode: QQuickWidget.ResizeMode = ..., sceneGraphError: typing.Callable[..., typing.Any] = ..., size: PySide2.QtCore.QSize = ..., sizeHint: PySide2.QtCore.QSize = ..., sizeIncrement: PySide2.QtCore.QSize = ..., sizePolicy: PySide2.QtWidgets.QSizePolicy = ..., source: PySide2.QtCore.QUrl = ..., status: QQuickWidget.Status = ..., statusChanged: typing.Callable[..., typing.Any] = ..., statusTip: str = ..., styleSheet: str = ..., tabletTracking: bool = ..., toolTip: str = ..., toolTipDuration: int = ..., updatesEnabled: bool = ..., visible: bool = ..., whatsThis: str = ..., width: int = ..., windowFilePath: str = ..., windowIcon: PySide2.QtGui.QIcon = ..., windowIconChanged: typing.Callable[..., typing.Any] = ..., windowIconText: str = ..., windowIconTextChanged: typing.Callable[..., typing.Any] = ..., windowModality: PySide2.QtCore.Qt.WindowModality = ..., windowModified: bool = ..., windowOpacity: float = ..., windowTitle: str = ..., windowTitleChanged: typing.Callable[..., typing.Any] = ..., x: int = ..., y: int = ...) -> None: ...
    def dragEnterEvent(self, arg__1: PySide2.QtGui.QDragEnterEvent) -> None: ...
    def dragLeaveEvent(self, arg__1: PySide2.QtGui.QDragLeaveEvent) -> None: ...
    def dragMoveEvent(self, arg__1: PySide2.QtGui.QDragMoveEvent) -> None: ...
    def dropEvent(self, arg__1: PySide2.QtGui.QDropEvent) -> None: ...
    def engine(self) -> PySide2.QtQml.QQmlEngine: ...
    def errors(self) -> typing.List[PySide2.QtQml.QQmlError]: ...
    def event(self, arg__1: PySide2.QtCore.QEvent) -> bool: ...
    def focusInEvent(self, event: PySide2.QtGui.QFocusEvent) -> None: ...
    def focusNextPrevChild(self, next: bool) -> bool: ...
    def focusOutEvent(self, event: PySide2.QtGui.QFocusEvent) -> None: ...
    def format(self) -> PySide2.QtGui.QSurfaceFormat: ...
    def grabFramebuffer(self) -> PySide2.QtGui.QImage: ...
    def hideEvent(self, arg__1: PySide2.QtGui.QHideEvent) -> None: ...
    def initialSize(self) -> PySide2.QtCore.QSize: ...
    def keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None: ...
    def keyReleaseEvent(self, arg__1: PySide2.QtGui.QKeyEvent) -> None: ...
    def mouseDoubleClickEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None: ...
    def paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None: ...
    def quickWindow(self) -> PySide2.QtQuick.QQuickWindow: ...
    def resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None: ...
    def resizeMode(self) -> QQuickWidget.ResizeMode: ...
    def rootContext(self) -> PySide2.QtQml.QQmlContext: ...
    def rootObject(self) -> PySide2.QtQuick.QQuickItem: ...
    def setClearColor(self, color: typing.Union[PySide2.QtGui.QColor,PySide2.QtCore.Qt.GlobalColor,int]) -> None: ...
    def setContent(self, url: PySide2.QtCore.QUrl, component: PySide2.QtQml.QQmlComponent, item: PySide2.QtCore.QObject) -> None: ...
    def setFormat(self, format: PySide2.QtGui.QSurfaceFormat) -> None: ...
    def setResizeMode(self, arg__1: QQuickWidget.ResizeMode) -> None: ...
    def setSource(self, arg__1: PySide2.QtCore.QUrl) -> None: ...
    def showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None: ...
    def sizeHint(self) -> PySide2.QtCore.QSize: ...
    def source(self) -> PySide2.QtCore.QUrl: ...
    def status(self) -> QQuickWidget.Status: ...
    def timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None: ...
    def wheelEvent(self, arg__1: PySide2.QtGui.QWheelEvent) -> None: ...
