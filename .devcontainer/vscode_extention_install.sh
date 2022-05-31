#!/bin/bash
 
# Visual Studio Code :: Package list
pkglist=(
        ms-python.python
		donjayamanne.python-extension-pack
		oderwat.indent-rainbow
		pkief.material-icon-theme
		mosapride.zenkaku
		aaron-bond.better-comments
		shardulm94.trailing-spaces
		kevinrose.vsc-python-indent
		tabnine.tabnine-vscode
		njpwerner.autodocstring
		ms-python.vscode-pylance
		gruntfuggly.todo-tree
)
 
for var in ${pkglist[@]}
do
    code --install-extension $var
done