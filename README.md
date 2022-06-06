## Minimal File Watcher For Easier Development
***Auto-Reload* (*ARD*) is a minimal and easily-extensible file watcher system.** It supports easy customization and extensibility through intuitive rewrite and configuration of 1 config file and the script itself.

## Setting Up Your auto_reload.config.json file
There are 3 different parameters to set up in your config file.

- Application run command.
    - **i.e. node app.js** 
- File watcher endings.
    - **i.e. "js" for JavaScript or "html" for HTML files**
- Directories to exclude.
    - **i.e. "node_modules", ".git", or ".idea"**

See the example directory for an example.

## Using The Tool

Run Auto-Reload by running the Python script **main.py** in your root project directory (you should know how).

Windows

```python main.py```

Unix-Like

```python3 main.py```

Stopping the script is as simple as clicking **Ctrl-C** as any program.
