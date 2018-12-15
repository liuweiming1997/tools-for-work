#!/bin/bash

set -e

function sync_vim() {
  echo "sync_vim......."
  echo "---------------------------------->"
  cd ~/.vim/
  git pull --rebase origin master
  ./send-vimrc.sh
  # git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
  vim +PluginInstall +qall
}

function sync_zsh() {
  echo "sync_zsh......."
  echo "---------------------------------->"
  cd ~/.zsh/
  git pull --rebase origin master
  ./send-zshrc-file.sh
}

function sync_sublime() {
  echo "sync_sublime......."
  echo "---------------------------------->"
  cd ~/.config/sublime-text-3/
  git delworkspace .
  git pull --rebase origin master
}

sync_vim
sync_zsh
sync_sublime

