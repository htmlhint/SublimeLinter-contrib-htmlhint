<h1 align="center">
  <br>
  SublimeLinter contrib HTMLHint
  <br>
</h1>

<h4 align="center">A SublimeLinter plugin for HTML, using HTMLHint.</h4>

<p align="center">
  <a href="#install">How To Use</a> • <a href="/CONTRIBUTING.md">Contributing</a> • <a href="https://htmlhint.com">Website</a>
</p>

## Table of Contents

- **[Install](#install)**
- **[Settings](#settings)**

This linter plugin for [SublimeLinter][docs] provides an interface to [HTMLHint](http://htmlhint.com/). It will be used with files that have the “HTML” syntax.

## Install

SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please [follow the instructions](https://www.sublimelinter.com/en/stable/installation.html).

### Linter installation

Before using this plugin, you must ensure that `htmlhint` is installed on your system. To install `htmlhint`, do the following:

1. Install [Node.js](https://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

2. Install the latest `htmlhint` globally by typing the following in a terminal:
   ```
   npm install -g htmlhint@latest
   ```
Or install `htmlhint` locally in your project folder (**you must have package.json file there**):
    ```
    npm init -f
    npm install htmlhint@latest
    ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

**Note:** This plugin requires `htmlhint` 0.9.13 or greater. Upgrade your existing installation by running step 2 above.

### Linter configuration

In order for `htmlhint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](https://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `htmlhint`, you can proceed to install the SublimeLinter-contrib-htmlhint plugin if it is not yet installed.

### Plugin installation

Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `htmlhint`. Among the entries you should see `SublimeLinter-contrib-htmlhint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings

For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

You can configure `htmlhint` options in the way you would from the command line, with `.htmlhintrc` files. For more information, see the [htmlhintrc docs](https://htmlhint.com/rules/). The linter plugin does this by searching for a `.htmlhintrc` file itself, just as `htmlhint` does from the command line. You may provide a custom config file by setting the linter’s `"args"` setting to `["--config", "/path/to/file"]`. On Windows, be sure to double the backslashes in the path, for example `["--config", "C:\\Users\\Username\\htmlhint.conf"]`.

The path to the `.htmlhintrc` file is cached, meaning if you create a new `.htmlhintrc` that should have precedence over the previous one (meaning it is closer to the .js file) you need to clear the cache for the linter to use the new `.htmlhintrc` You can clear the cache by going to: Tools > SublimeLinter > Clear Caches.

## LICENCE

Project initially created by [@mmaday](https://github.com/mmaday) and transferred to the [HTMLHint](https://github.com/htmlhint) organization.

<a href="https://htmlhint.com"><img src="https://raw.githubusercontent.com/htmlhint/htmlhint/develop/src/img/htmlhint.png" alt="Logo HTMLHint" width="65"></a>

[MIT License](./LICENSE)

[docs]: https://sublimelinter.readthedocs.org
[installation]: https://sublimelinter.readthedocs.io/en/latest/installation.html
[locating-executables]: https://sublimelinter.readthedocs.io/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: https://www.docs.sublimetext.info/index.html
[settings]: https://sublimelinter.readthedocs.io/en/latest/settings.html
[linter-settings]: https://sublimelinter.readthedocs.io/en/latest/linter_settings.html
[inline-settings]: https://sublimelinter.readthedocs.io/en/latest/settings.html#inline-settings
