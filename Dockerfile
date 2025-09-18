# Usamos uma base Ubuntu 20.04, que tem compatibilidade total com as ferramentas
FROM ubuntu:20.04

# Evita perguntas durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instala todas as dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    python3.8 \
    python3-pip \
    mininet

# Instala versões específicas do Ryu e suas dependências para garantir compatibilidade
RUN pip3 install 'ryu==4.34' 'eventlet==0.35.2'

# Define o diretório de trabalho
WORKDIR /root

# Comando padrão para iniciar um terminal no ambiente
CMD ["/bin/bash"]
