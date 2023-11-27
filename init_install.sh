#!/bin/bash

# Función para detectar el sistema operativo
detectar_sistema() {
  if [ -f /etc/os-release ]; then
    # Cargar variables de /etc/os-release
    . /etc/os-release
    SISTEMA=$ID
  elif [ -f /etc/redhat-release ]; then
    SISTEMA="rocky"
  else
    echo "No se pudo detectar el sistema operativo compatible."
    exit 1
  fi
}

# Función para instalar Docker en Ubuntu

instalar_docker_ubuntu() {

echo "Instalando docker y docker compose en Ubuntu."

  sudo apt-get update

  sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

  echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  sudo apt-get update

  sudo apt-get install -y docker-ce docker-ce-cli containerd.io

  sudo docker --version

  sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

  sudo chmod +x /usr/local/bin/docker-compose

  docker-compose --version

  sudo apt-get update

  # Instalar NVM (Node Version Manager)

  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

  # Cargar NVM en la terminal actual
  source ~/.bashrc
  # O reinicia la terminal

  # Instalar Node.js (versión 19)
  nvm install 19

  node -v
  npm -v

  cd /opt/uni_gestion_projectos/frontend

  npm i


}

# Función para instalar Docker en Rocky Linux


instalar_docker_rocky() {

  echo "Instalando docker y docker compose en Roky."

  sudo dnf update -y

  sudo dnf install -y yum-utils device-mapper-persistent-data lvm2

  sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

  sudo dnf install docker-ce docker-ce-cli containerd.io

  sudo systemctl start docker

  sudo systemctl enable docker

  echo "Instalando node y npm ."

  sudo curl -fsSL https://rpm.nodesource.com/setup_19.x | sudo bash -

  sudo dnf makecache

  sudo dnf install -y nodejs

  node -v

  npm -v

  cd /opt/uni_gestion_projectos/frontend

  npm i
}

# Detectar el sistema operativo
detectar_sistema

# Instalar Docker según el sistema operativo detectado
case $SISTEMA in
  ubuntu)
    instalar_docker_ubuntu
    ;;
  rocky)
    instalar_docker_rocky
    ;;
  *)
    echo "Sistema operativo no compatible."
    exit 1
    ;;
esac

echo "Docker se ha instalado correctamente en $SISTEMA."