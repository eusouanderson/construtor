#!/bin/bash

# adiciona permissão root ao construtor
chmod +x /home/anderson/Projetos/construtor/construtor.py

# Verifica se o python esta instalado
if ! command -v python3 &>/dev/null; then
   echo "O Python 3 não está instalado. Instale-o antes de prosseguir."
   exit 1
fi

# Verifica se o arquivo ~/.bashrc existe
if [ -f ~/.bashrc ]; then
  # Verifica se o alias já está definido
  if grep -q "alias construtor" ~/.bashrc; then
    echo "Alias 'construtor' já está definido."
  else
    # Adiciona o alias ao arquivo ~/.bashrc
    echo "alias construtor='/bin/python ${PWD}/construtor.py'" >> ~/.bashrc
    echo "Alias 'construtor' adicionado com sucesso ao arquivo ~/.bashrc."
    echo "Por favor, abra um novo terminal ou execute 'source ~/.bashrc' para carregar as alterações."
  fi
else
  echo "Arquivo ~/.bashrc não encontrado. O alias não pode ser adicionado."
fi
