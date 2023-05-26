# Installing VS Code

Visual Studio Code (VS Code) is a free and open-source code editor developed by Microsoft.

To install it on your system open the [VS Code home page](https://code.visualstudio.com/) and download the installer for your operating system (we assume, it's Windows 11).

Run the installer, and follow the on-screen instructions.

In case of any problems, please refer to the [official installation guide](https://code.visualstudio.com/docs/setup/windows).

## Adding Extensions

Visual Studio Code is a very powerful editor, but can be more useful with extensions. Extensions are small programs that add new features to VS Code.

We will need two extensions for our work: one for working with WSL and another for Python development.

First start a WSL session with:

```powershell
> wsl ~
```

And launch VS Code with the following command:

```sh
code
```

If this is the first time you doing this, it will ask you to install the `Remote - WSL extension`. Click on the Install button and wait for the installation to complete.

You will need one more extension for Python development. It's called [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and is useful for syntax highlighting and code completion. To install it, press `Ctrl+Shift+X` to open the Extensions panel, type `Python` in the search box, and click on the `Install` button.
