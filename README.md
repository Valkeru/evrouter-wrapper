Simple wrapper for evrouter to remap `Zoom In` and `Zoom Out` keys on M$ Natural Keyboard 4000
-
This tool generates evrouter config and puts it in `~/.evrouterrc` file, then start (or restart) evrouter.

How to use:  
```bash
./ewrapper
```
No any option required.  
Installation:  
```bash
make install
```
By default installation directory is $HOME/.local/bin  
To customize installation path use `INSTALL_PATH` option:  
```bash
make install INSTALL_PATH=/opt/bin
```