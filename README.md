# Ping-Pong (Jogo Clássico de Pong)

Um jogo simples e divertido do clássico **Pong**, recriado em **Python** utilizando a biblioteca **Pygame**.

## 🚀 Como Jogar

Este é um jogo de dois jogadores.

  * **Jogador da Esquerda (Paddle Esquerda):**
      * **$\uparrow$ (Seta Cima):** Move o paddle para cima.
      * **$\downarrow$ (Seta Baixo):** Move o paddle para baixo.
  * **Jogador da Direita (Paddle Direita):**
      * **W:** Move o paddle para cima.
      * **S:** Move o paddle para baixo.
  * **ESC:** Sai do jogo a qualquer momento.

O primeiro jogador a alcançar uma pontuação predefinida (por exemplo, 5 ou 10) vence o jogo.

## 🛠️ Instalação

Siga estes passos para ter o jogo a correr na sua máquina.

### Pré-requisitos

Certifique-se de que tem o **Python 3** instalado.

### 1\. Clonar o Repositório

```bash
git clone https://github.com/SEU_UTILIZADOR/nome-do-seu-repositorio.git
cd nome-do-seu-repositorio
```

*(Altere `SEU_UTILIZADOR/nome-do-seu-repositorio` para os detalhes do seu projeto.)*

### 2\. Instalar o Pygame

Precisa apenas de uma biblioteca: `pygame`.

```bash
pip install pygame
```

### 3\. Executar o Jogo

Basta executar o ficheiro principal em Python:

```bash
python ping_pong.py
```

*(Altere `ping_pong.py` para o nome real do seu ficheiro principal se for diferente.)*

## ⚙️ Estrutura do Projeto

O projeto é relativamente simples e está contido principalmente num único ficheiro, mas a sua estrutura de código pode incluir:

```
ping-pong-pygame/
├── ping_pong.py        # O ficheiro principal com toda a lógica do jogo
├── README.md           # Este ficheiro
├── LICENSE             # (Opcional) Informação sobre a licença
└── assets/             # (Opcional) Pasta para fontes ou sons
    ├── som_paddle.wav
    └── fonte_placar.ttf
```

## ✨ Funcionalidades

  * **Multiplayer Local:** Dois jogadores no mesmo teclado.
  * **Dificuldade Progressiva:** A velocidade da bola aumenta a cada rebatida (opcional, dependendo da sua implementação).
  * **Sistema de Pontuação:** A pontuação é exibida e atualizada em tempo real.
  * **Ecrã de Fim de Jogo:** Exibe o vencedor quando a pontuação limite é alcançada.

## 🤝 Contribuições

Contribuições são bem-vindas\! Se quiser melhorar o jogo, sinta-se à vontade para:

1.  Fazer um *Fork* do repositório.
2.  Criar um *Branch* para a sua funcionalidade (`git checkout -b feature/NovaFuncionalidade`).
3.  Fazer o *Commit* das suas alterações (`git commit -m 'Adiciona NovaFuncionalidade'`).
4.  Fazer o *Push* para o *Branch* (`git push origin feature/NovaFuncionalidade`).
5.  Abrir um **Pull Request**.

## 📜 Licença

Este projeto está licenciado sob a Licença **CC** - veja o ficheiro LICENSE para mais detalhes.
