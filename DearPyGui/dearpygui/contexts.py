from contextlib import contextmanager
from typing import List, Any, Callable, Union
import dearpygui.core as internal_dpg

########################################################################################################################
# context manager container wrappers
########################################################################################################################

@contextmanager
def file_dialog(*args, id:str='', width: int =0, height: int =0, label: str ='', callback: Callable =None, show: bool =True, 
					default_path: str ='', default_filename: str ='.', file_count: int =0, modal: bool =False, directory_selector: bool =False):
   
   try:
        widget = internal_dpg.add_file_dialog(*args, id=id, width=width, height=height, label=label, callback=callback, show=show,
                                              default_path=default_path, default_filename=default_filename, file_count=file_count,
                                              modal=modal, directory_selector=directory_selector)
        internal_dpg.push_container_stack(widget)
        yield widget
   finally:
        internal_dpg.pop_container_stack()


@contextmanager
def table(*args, header_row: bool = True, width: int = 0, height: int = 0, inner_width: int = 0, show: bool = True, parent: str = "",
		before: str = "", resizable: bool = False, reorderable: bool = False, hideable: bool = False, sortable: bool = False,   
		context_menu_in_body: bool = False, row_background: bool = False, borders_innerH: bool = False, borders_outerH: bool = False,
		borders_innerV: bool = False, borders_outerV: bool = False, policy: int = 0, no_host_extendX: bool = False,
		no_host_extendY: bool = False, no_keep_columns_visible: bool = False, precise_widths: bool = False, no_clip: bool = False,
		pad_outerX: bool = False, no_pad_outerX: bool = False, no_pad_innerX: bool = False, scrollX: bool = False, scrollY: bool = False,
        id:str='', indent=-1, callback: Callable = None, sort_multi: bool = False, sort_tristate: bool = False):
    """Wraps add_table() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
			**header_row: show headers at the top of the columns
			**width: 
			**height: 
			**inner_width:
			**show: Attempt to render
			**parent: Parent this item will be added to. (runtime adding)
			**before: This item will be displayed before the specified item in the parent. (runtime adding)
			**resizable: Enable resizing columns
	        **reorderable: Enable reordering columns in header row
	        **hideable: Enable hiding/disabling columns in context menu.
	        **sortable: Enable sorting.
	        **context_menu_in_body: Right-click on columns body/contents will display table context menu.
			**row_background: Set each RowBg color with ImGuiCol_TableRowBg or ImGuiCol_TableRowBgAlt (equivalent of calling TableSetBgColor with ImGuiTableBgFlags_RowBg0 on each row manually)
	        **borders_innerH: Draw horizontal borders between rows.
	        **borders_outerH: Draw horizontal borders at the top and bottom.
	        **borders_innerV: Draw vertical borders between columns.
	        **borders_outerV: Draw vertical borders on the left and right sides.
	        **policy: sizing policy
			**no_host_extendX: Make outer width auto-fit to columns, overriding outer_size.x value. Only available when ScrollX/ScrollY are disabled and Stretch columns are not used.
			**no_host_extendY: Make outer height stop exactly at outer_size.y (prevent auto-extending table past the limit). Only available when ScrollX/ScrollY are disabled. Data below the limit will be clipped and not visible.
			**no_keep_columns_visible: Disable keeping column always minimally visible when ScrollX is off and table gets too small. Not recommended if columns are resizable.
			**precise_widths: Disable distributing remainder width to stretched columns (width allocation on a 100-wide table with 3 columns: Without this flag: 33,33,34. With this flag: 33,33,33). With larger number of columns, resizing will appear to be less smooth.
			**no_clip: Disable clipping rectangle for every individual columns.
	        **pad_outerX: Default if BordersOuterV is on. Enable outer-most padding. Generally desirable if you have headers.
	        **no_pad_outerX: Default if BordersOuterV is off. Disable outer-most padding.
	        **no_pad_innerX: Disable inner padding between columns (double inner padding if BordersOuterV is on, single inner padding if BordersOuterV is off).
	        **scollX: Enable horizontal scrolling. Require 'outer_size' parameter of BeginTable() to specify the container size. Changes default sizing policy. Because this create a child window, ScrollY is currently generally recommended when using ScrollX.
	        **scollY: Enable horizontal vertical.

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_table(*args, header_row=header_row, width = width, height = height, inner_width = inner_width,
		    show = show, parent = parent, before = before, resizable = resizable, reorderable = reorderable, hideable = hideable,
		    sortable = sortable, context_menu_in_body = context_menu_in_body, row_background = row_background,
		    borders_innerH = borders_innerH, borders_outerH = borders_outerH, borders_innerV = borders_innerV,
		    borders_outerV = borders_outerV, policy = policy, no_host_extendX = no_host_extendX,
		    no_host_extendY = no_host_extendY, no_keep_columns_visible = no_keep_columns_visible, precise_widths = precise_widths,
		    no_clip = no_clip, pad_outerX = pad_outerX, no_pad_outerX = no_pad_outerX, no_pad_innerX = no_pad_innerX,
		    scrollX = scrollX, scrollY = scrollY, id=id, indent=indent, callback=callback, sort_multi=sort_multi,
            sort_tristate=sort_tristate)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def drawlist(*args, id:str='', width: int = 0, height: int = 0, show: bool = True, parent: str = "", before: str = ""):
    try:
        widget = internal_dpg.add_drawlist(*args, id=id, width = width, height = height, show=show, parent=parent, before=before)
        internal_dpg.push_container_stack(widget)
        yield widget

    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def viewport_drawlist(*args, id:str='', front: bool = True, show: bool = True):
    try:
        widget = internal_dpg.add_viewport_drawlist(*args, id=id, show=show, front=front)
        internal_dpg.push_container_stack(widget)
        yield widget

    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def table_row(*args, id:str='', show: bool = True, parent: str = "", before: str = ""):
    try:
        widget = internal_dpg.add_table_row(*args, id=id, show=show, parent=parent, before=before)
        internal_dpg.push_container_stack(widget)
        yield widget

    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def draw_layer(*args, id:str='', show: bool = True, parent: str = "", before: str = ""):
    try:
        widget = internal_dpg.add_draw_layer(*args, id=id, show=show, parent=parent, before=before)
        internal_dpg.push_container_stack(widget)
        yield widget

    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def window(*args, width: int = 200, height: int = 200, autosize: bool = False,
           no_resize: bool = False, no_title_bar: bool = False, no_move: bool = False, no_scrollbar: bool = False,
           no_collapse: bool = False, horizontal_scrollbar: bool = False, no_focus_on_appearing: bool = False,
           no_bring_to_front_on_focus: bool = False, menubar: bool = False, no_close: bool = False,
           no_background: bool = False, label: str = '', show: bool = True, collapsed: bool = False,
           modal: bool = False, popup: bool = False,
           on_close: Callable = None, min_size: List[int]=[32, 32], max_size: List[int] = [30000, 30000], id:str=''):
    """Wraps add_window() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **width: Width of the item.
        **height: Height of the item.
        **autosize: Autosized the window to fit it's items.
        **no_resize: Allows for the window size to be changed or fixed
        **no_title_bar: Title name for the title bar of the window
        **no_move: Allows for the window's position to be changed or fixed
        **no_scrollbar: Disable scrollbars (window can still scroll with mouse or programmatically)
        **no_collapse: Disable user collapsing window by double-clicking on it
        **horizontal_scrollbar: Allow horizontal scrollbar to appear (off by default).
        **no_focus_on_appearing: Disable taking focus when transitioning from hidden to visible state
        **no_bring_to_front_on_focus: Disable bringing window to front when taking focus (e.g. clicking on it or
            programmatically giving it focus)
        **menubar: Decides if the menubar is shown or not.
        **no_close: Decides if the window can be closed.
        **no_background:
        **label: Displayed name of the item.
        **show: sets if the item is shown or not window.
        **on_close: Callback ran when window is closed
        **min_size: Minimum window size
        **max_size: Maximum window size
        **modal: Sets window to modal mode
        **popup: Sets window to popup mode

    Returns:
        None
    """
    try:

        widget = internal_dpg.add_window(*args, width=width, height=height, autosize=autosize,
                                        no_resize=no_resize, no_title_bar=no_title_bar, no_move=no_move,
                                        no_scrollbar=no_scrollbar, no_collapse=no_collapse,
                                        horizontal_scrollbar=horizontal_scrollbar,
                                        no_focus_on_appearing=no_focus_on_appearing,
                                        no_bring_to_front_on_focus=no_bring_to_front_on_focus,
                                        menubar=menubar, no_close=no_close,
                                        no_background=no_background, label=label, show=show, 
                                        collapsed=collapsed, on_close=on_close,
                                        min_size=min_size, max_size=max_size, id=id, modal=modal,
                                        popup=popup)
        internal_dpg.push_container_stack(widget)
        yield widget

    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def menu_bar(*args, show: bool = True, parent: str = "", before: str = "", id:str='', indent=-1):
    """Wraps add_menu_bar() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **show: Decides if the item is shown of not.
        **parent: Parent this item will be added to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_menu_bar(*args, show=show, parent=parent, before=before, id=id, indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def menu(*args, label: str = "", show: bool = True, parent: str = "",
         before: str = "", enabled: bool = True, id:str='', indent=-1):
    """Wraps add_menu() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **label: Displayed name of the item.
        **show: Decides if the item is shown of not.
        **parent: Parent this item will be added to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **enabled: Will enable or disable the menu.

    Returns:
        None
    """
    try: 
        widget = internal_dpg.add_menu(*args, label=label, show=show, parent=parent,
                                    before=before, enabled=enabled, id=id, indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def child(*args, show: bool = True, parent: str = "", before: str = "", width: int = 0,
          height: int = 0, border: bool = True, autosize_x: bool = False, autosize_y: bool = False,
          no_scrollbar: bool = False, horizontal_scrollbar: bool = False, menubar: bool = False, id:str='', 
          indent=-1):
    """Wraps add_child() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        show: Decides if the item is shown of not.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **width: Width of the item.
        **height: Height of the item.
        **border: Shows/Hides the border around the sides
        **autosize_x: Autosize the window to fit its items in the x.
        **autosize_y: Autosize the window to fit its items in the y.
        **no_scrollbar: Disable scrollbars (window can still scroll with mouse or programmatically)
        **horizontal_scrollbar: Allow horizontal scrollbar to appear (off by default)
        **menubar: adds a bar to add menus

    Returns:
        None
    """
    try: 
        widget = internal_dpg.add_child(*args, show=show, parent=parent, before=before, width=width,
                                     height=height, border=border, autosize_x=autosize_x, autosize_y=autosize_y,
                                     no_scrollbar=no_scrollbar, horizontal_scrollbar=horizontal_scrollbar,
                                     menubar=menubar, id=id, indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def collapsing_header(*args, label: str = "", show: bool = True,
                     parent: str = "", before: str = "",closable: bool = False, 
                      default_open: bool = False, open_on_double_click: bool = False, open_on_arrow: bool = False, 
                      leaf: bool = False, bullet: bool = False, id:str='', indent=-1):
    """Wraps add_collapsing_header() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **label: Displayed name of the item.
        **show: Decides if the item is shown of not.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **closable: Decides if the header can be collapsed.
        **default_open: Decides if item is open by default.
        **open_on_double_click: Need double-click to open node.
        **open_on_arrow: Only open when clicking on the arrow part.
        **leaf: No collapsing, no arrow (use as a convenience for leaf nodes).
        **bullet: Display a bullet instead of arrow.


    Returns:
        None
    """
    try:
        widget = internal_dpg.add_collapsing_header(*args, show=show, label=label, parent=parent, before=before, 
                                                    closable=closable, default_open=default_open, 
                                                    open_on_double_click=open_on_double_click,
                                                    open_on_arrow=open_on_arrow, leaf=leaf, bullet=bullet, id=id,
                                                    indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def group(*args, show: bool = True, parent: str = "", before: str = "", width: int = 0,
          horizontal: bool = False, horizontal_spacing: float = -1.0, id:str='', indent=-1):
    """Wraps add_group() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **show: Decides if the item is shown of not.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **width: Width of the item.
        **horizontal: Adds the items on the same row by default.
        **horizontal_spacing: Decides the spacing for the items.

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_group(*args, show=show, parent=parent, before=before, width=width,
                                     horizontal=horizontal, horizontal_spacing=horizontal_spacing, id=id,
                                     indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def node(*args, label: str = "", show: bool = True, draggable: bool = True,
         parent: str = "", before: str = "", x_pos: int = 100, y_pos: int = 100, id:str=''):
    """Wraps add_node() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **label: Displayed name of the item.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **show: sets if the item is shown or not window.
        **draggable: Allow node to be draggable.
        **x_pos: x position the node will start at
        **y_pos: y position the node will start at

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_node(*args, label=label, show=show, parent=parent, before=before, 
                                                    draggable=draggable, x_pos=x_pos, y_pos=y_pos, id=id)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def node_attribute(*args, show: bool = True, output: bool = False,
         static: bool = False, parent: str = "", before: str = "", shape: int = 54010, id:str=''
         , indent=-1):
    """Wraps add_node_attribute() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **show: sets if the item is shown or not window.
        **output: Set as output attribute
        **static: Set as static attribute

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_node_attribute(*args, show=show, parent=parent, before=before, 
                                                    output=output, static=static, shape=shape, id=id,
                                                    indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def node_editor(*args, show: bool = True, parent: str = "", before: str = "", callback: Callable = None, 
                delink_callback: Callable = None, id:str=''):
    """Wraps add_node_editor() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **show: sets if the item is shown or not window.
        **link_callback: Callback ran when a new link is created
        **delink_callback: Callback ran when a link is detached

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_node_editor(*args, show=show, parent=parent, before=before, 
                                           callback=callback, delink_callback=delink_callback, id=id)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def staging_container(*args, id:str=''):
    """Wraps add_menu_bar() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **show: Decides if the item is shown of not.
        **parent: Parent this item will be added to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_staging_container(id=id)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()

@contextmanager
def tab_bar(*args, reorderable: bool = False, callback: Callable = None, callback_data: Any = None,  show: bool = True,
            parent: str = "", before: str = "", id:str='', indent=-1):
    """Wraps add_tab_bar() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **reorderable: Allows for moveable tabs.
        **callback: Registers a callback.
        **callback_data: Callback data.
        **show: Decides if the item is shown of not.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_tab_bar(*args, reorderable=reorderable, callback=callback, callback_data=callback_data,
                                       show=show, parent=parent, before=before, id=id, indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def tab(*args, closable: bool = False, label: str = "", show: bool = True,
        no_reorder: bool = False, leading: bool = False, trailing: bool = False, no_tooltip: bool = False,
        parent: str = "", before: str = "", id:str='', indent=-1):
    """Wraps add_tab() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **closable: creates a button on the tab that can hide the tab.
        **label: Displayed name of the item.
        **show: Decides if the item is shown of not.
        **no_reorder: Disable reordering this tab or having another tab cross over this tab
        **leading: Enforce the tab position to the left of the tab bar (after the tab list popup button)
        **trailing: Enforce the tab position to the right of the tab bar (before the scrolling buttons)
        **no_tooltip: Disable tooltip for the given tab
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_tab(*args, closable=closable, label=label, show=show, parent=parent,
                                    before=before, no_reorder=no_reorder, leading=leading, 
                                    trailing=trailing, no_tooltip=no_tooltip, id=id, indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def tree_node(*args, label: str = "", show: bool = True, parent: str = "", 
              before: str = "", default_open: bool = False, open_on_double_click: bool = False, 
              open_on_arrow: bool = False, leaf: bool = False, bullet: bool = False, id:str='',
              selectable: bool = False, indent=-1):
    """Wraps add_tree_node() and automates calling end().

    Args:
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **label: Displayed name of the item.
        **show: Decides if the item is shown of not.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **default_open: Decides if item is open by default.
        **open_on_double_click: Need double-click to open node.
        **open_on_arrow: Only open when clicking on the arrow part.
        **leaf: No collapsing, no arrow (use as a convenience for leaf nodes).
        **bullet: Display a bullet instead of arrow.

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_tree_node(*args, show=show, parent=parent,
                                            before=before, default_open=default_open, 
                                            open_on_double_click=open_on_double_click, 
                                            open_on_arrow=open_on_arrow,
                                            leaf=leaf, bullet=bullet, label=label, id=id, selectable=selectable,
                                            indent=indent)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def tooltip(*args, parent: str = "", before: str = "", show: bool = True, id:str=''):
    """Wraps add_tooltip() and automates calling end().

    Args:
        tipparent: Sets the item's tool tip to be the same as the named item's tool tip.
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **show: Decides if the item is shown of not.

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_tooltip(*args, parent=parent, before=before, show=show, id=id)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()


@contextmanager
def popup(*args, mousebutton: int = 1, modal: bool = False, parent: str = "", 
          before: str = "", width: int = 0, height: int = 0, show: bool = True, id:str=''):
    """Wraps add_popup() and automates calling end().

    Args:
        popupparent: Parent that the popup will be assigned to.
        name: Unique name used to programmatically refer to the item. If label is unused this will be the label,
            anything after "##" that occurs in the name will not be shown on screen.
        **mousebutton: The mouse code that will trigger the popup. Default is 1 or mvMouseButton_Right.
            (mvMouseButton_Left, mvMouseButton_Right, mvMouseButton_Middle, mvMouseButton_X1, mvMouseButton_X2)
        **modal: Makes the popup modal.
        **parent: Parent to add this item to. (runtime adding)
        **before: This item will be displayed before the specified item in the parent. (runtime adding)
        **width: Width of the item.
        **height: Height of the item.
        **show: Decides if the item is shown of not.

    Returns:
        None
    """
    try:
        widget = internal_dpg.add_popup(*args, mousebutton=mousebutton, modal=modal, parent=parent,
                                     before=before, width=width, height=height, show=show, id=id)
        internal_dpg.push_container_stack(widget)
        yield widget
    finally:
        internal_dpg.pop_container_stack()