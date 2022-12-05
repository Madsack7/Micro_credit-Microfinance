Unreleased
----------

    See on GitHub: `branch master <https://github.com/kivymd/KivyMD/tree/master>`_ | `compare 1.0.2/master <https://github.com/kivymd/KivyMD/compare/1.0.2...master>`_

    .. code-block:: bash

       pip install https://github.com/kivymd/KivyMD/archive/master.zip

* Bug fixes and other minor improvements.
* Add `closing_interval <https://kivymd.readthedocs.io/en/latest/components/card/#kivymd.uix.card.card.MDCardSwipe.closing_interval>`_ parameter to `MDCardSwipe <https://kivymd.readthedocs.io/en/latest/components/card/#kivymd.uix.card.card.MDCardSwipe>`_ class.
* Add implementation of elevation behavior on shaders.
* Add `validator <https://kivymd.readthedocs.io/en/latest/components/textfield/#kivymd.uix.textfield.textfield.MDTextField.validator>`_ property to `MDTextField <https://kivymd.readthedocs.io/en/latest/components/textfield/#kivymd.uix.textfield.textfield.MDTextFieldR>`_ class: the type of text field for entering Email, time, etc. Automatically sets the type of the text field as `error` if the user input does not match any of the set validation types.
* Add `theme_style_switch_animation <https://kivymd.readthedocs.io/en/latest/themes/theming/#kivymd.theming.ThemeManager.theme_style_switch_animation>`_ property to animate the colors of the application when switching the color scheme of the application `('Dark/light')`.
* Add `theme_style_switch_animation_duration <https://kivymd.readthedocs.io/en/latest/themes/theming/#kivymd.theming.ThemeManager.theme_style_switch_animation_duration>`_ property to duration of the animation of switching the color scheme of the application `("Dark/ light")`.
* `Fix <https://github.com/kivymd/KivyMD/issues/1332>`_ memory leak when dynamically adding and removing `KivyMD` widgets.
* `Fix <https://github.com/kivymd/KivyMD/pull/1344>`_ `MDBottomNavigation <https://kivymd.readthedocs.io/en/latest/components/bottomnavigation/>`_ slide transition direction.
* Add a default value for the `icon <https://kivymd.readthedocs.io/en/latest/themes/material-app/#kivymd.app.MDApp.icon>`_ attribute of `MDApp <https://kivymd.readthedocs.io/en/latest/themes/material-app/#kivymd.app.MDApp>`_ class.
* Add new properties to `MDFileManager <https://kivymd.readthedocs.io/en/latest/components/filemanager/>`_ class:

  - `icon_selection_button <https://kivymd.readthedocs.io/en/latest/components/filemanager/#kivymd.uix.filemanager.filemanager.MDFileManager.icon_selection_button>`_ - icon that will be used on the directory selection button;
  - `background_color_selection_button <https://kivymd.readthedocs.io/en/latest/components/filemanager/#kivymd.uix.filemanager.filemanager.MDFileManager.background_color_selection_button>`_ - background color of the current directory/path selection button;
  - `background_color_toolbar <https://kivymd.readthedocs.io/en/latest/components/filemanager/#kivymd.uix.filemanager.filemanager.MDFileManager.background_color_toolbar>`_ - background color of the file manager toolbar;
  - `icon_color <https://kivymd.readthedocs.io/en/latest/components/filemanager/#kivymd.uix.filemanager.filemanager.MDFileManager.icon_color>`_ - color of the folder icon when the `preview` property is set to False;
* Add binds to `MDFloatingActionButtonSpeedDial <https://kivymd.readthedocs.io/en/latest/components/button/#mdfloatingactionbuttonspeeddial>`_ `individual <https://kivymd.readthedocs.io/en/latest/components/button/#binds-to-individual-buttons>`_ buttons;
* Added functionality for using `multiple heroes <https://kivymd.readthedocs.io/en/latest/components/hero/#using-multiple-heroes-at-the-same-time>`_.
