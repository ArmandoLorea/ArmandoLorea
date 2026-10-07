import os

# Nos aseguramos de que la carpeta assets exista
os.makedirs("assets", exist_ok=True)

# 1. Generar el Título Animado RGB (titulo-animado.svg)
titulo_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="100">
  <defs>
    <linearGradient id="rainbow" x1="0%" y1="0%" x2="200%" y2="0%">
      <stop offset="0%" stop-color="#ff0000" />
      <stop offset="16%" stop-color="#ff7f00" />
      <stop offset="33%" stop-color="#ffff00" />
      <stop offset="50%" stop-color="#00ff00" />
      <stop offset="66%" stop-color="#0000ff" />
      <stop offset="83%" stop-color="#4b0082" />
      <stop offset="100%" stop-color="#9400d3" />
      <animate attributeName="x1" from="0%" to="-200%" dur="4s" repeatCount="indefinite" />
      <animate attributeName="x2" from="200%" to="0%" dur="4s" repeatCount="indefinite" />
    </linearGradient>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=VT323&amp;display=swap');
      .rgb-title { font-family: 'VT323', monospace; font-size: 42px; fill: url(#rainbow); }
      .subtitle { font-family: 'VT323', monospace; font-size: 22px; fill: #ffffff; }
    </style>
  </defs>
  <text x="50%" y="45" class="rgb-title" text-anchor="middle">Armando Fidel Lorea Sanchez</text>
  <text x="50%" y="85" class="subtitle" text-anchor="middle">Estudiante de Ingeniería en Sistemas Computacionales</text>
</svg>"""

with open("assets/titulo-animado.svg", "w", encoding="utf-8") as f:
    f.write(titulo_svg)

# 2. Generar la Terminal Oscura (terminal.svg)
terminal_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="280">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=VT323&amp;display=swap');
      .terminal-text { font-family: 'VT323', monospace; font-size: 20px; fill: #a5d6ff; }
      .terminal-cmd { font-family: 'VT323', monospace; font-size: 20px; fill: #7ee787; font-weight: bold; }
    </style>
  </defs>

  <!-- Fondo oscuro estilo editor -->
  <rect width="100%" height="100%" fill="#0d1117" rx="15" />
  
  <!-- Botones de la ventana -->
  <circle cx="30" cy="30" r="7" fill="#ff5f56" />
  <circle cx="55" cy="30" r="7" fill="#ffbd2e" />
  <circle cx="80" cy="30" r="7" fill="#27c93f" />

  <!-- Texto de la terminal -->
  <text x="40" y="80" class="terminal-cmd">$ cat tech_stack.txt</text>
  <text x="40" y="110" class="terminal-text">Frontend: HTML5, CSS3, JavaScript (ES6+), WebGL (Three.js)</text>
  <text x="40" y="140" class="terminal-text">Backend &amp; Software: Java</text>
  <text x="40" y="170" class="terminal-text">Herramientas: VS Code, NetBeans, Git</text>

  <text x="40" y="210" class="terminal-cmd">$ ls projects/ --color=auto</text>
  <text x="40" y="240" class="terminal-text">Surreal_Mex.java    SkinsArts-Studio.js</text>
</svg>"""

with open("assets/terminal.svg", "w", encoding="utf-8") as f:
    f.write(terminal_svg)

print("¡Archivos SVG generados con éxito!")