#!/usr/bin/env bash
# Descarga y extrae Node.js manualmente
NODE_VERSION="16.20.0" # Cambia a la versión que necesitas
curl -o node.tar.xz https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz
tar -xf node.tar.xz
mv node-v$NODE_VERSION-linux-x64 /usr/local/node
export PATH=/usr/local/node/bin:$PATH
node -v
npm -v
