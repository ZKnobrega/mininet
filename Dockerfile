# Base ARM64 estável (para Raspberry Pi 3)
FROM arm64v8/ubuntu:20.04

# Evita prompts do apt
ENV DEBIAN_FRONTEND=noninteractive

# Atualizar pacotes e instalar dependências básicas
RUN apt-get update && apt-get install -y \
    build-essential git sudo curl wget iproute2 iputils-ping net-tools \
    python3.9 python3.9-venv python3.9-dev python3-pip \
    openvswitch-switch openvswitch-common \
    && rm -rf /var/lib/apt/lists/*

# Criar venv para isolar Ryu
RUN python3.9 -m venv /opt/ryu-venv
ENV PATH="/opt/ryu-venv/bin:$PATH"

# Instalar Ryu com versão compatível do eventlet
RUN pip install --upgrade pip \
    && pip install "eventlet==0.30.2" ryu

# Instalar Mininet (apenas o essencial, sem Wireshark/extra GUI)
RUN git clone https://github.com/mininet/mininet.git /opt/mininet \
    && cd /opt/mininet && util/install.sh -fnv

# PATH do Mininet
ENV PATH="/opt/mininet/bin:$PATH"

# Comando padrão ao iniciar o container
CMD ["/bin/bash"]
