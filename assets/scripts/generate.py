import base64
import os

# 1. Función para convertir tus PNG a Base64
def png_a_base64(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print(f"⚠️  No se encontró la imagen: {ruta_archivo}")
        return ""
    with open(ruta_archivo, "rb") as img_file:
        img_codificada = base64.b64encode(img_file.read()).decode('utf-8')
        return f"data:image/png;base64,{img_codificada}"

# 2. Rutas a tus imágenes PNG originales (Asegúrate de ejecutar el script desde la raíz del repo)
logo_tlalocan = png_a_base64("assets/logos/tlalocan.png")
logo_netbeans = png_a_base64("assets/logos/netbeans.png")
logo_visual   = png_a_base64("assets/logos/visual.png")

# 3. Diseño del SVG (Terminal, Texto, Animación RGB y Base64)
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="850" height="600">
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
      .rgb-title {{ font-family: 'VT323', monospace; font-size: 38px; fill: url(#rainbow); }}
      .subtitle {{ font-family: 'VT323', monospace; font-size: 22px; fill: #ffffff; }}
      .terminal-text {{ font-family: 'VT323', monospace; font-size: 20px; fill: #a5d6ff; }}
      .terminal-cmd {{ font-family: 'VT323', monospace; font-size: 20px; fill: #7ee787; font-weight: bold; }}
    </style>
  </defs>

  <!-- Fondo oscuro estilo editor -->
  <rect width="100%" height="100%" fill="#0d1117" rx="15" />
  
  <!-- Barra superior de la terminal -->
  <circle cx="30" cy="30" r="7" fill="#ff5f56" />
  <circle cx="55" cy="30" r="7" fill="#ffbd2e" />
  <circle cx="80" cy="30" r="7" fill="#27c93f" />

  <!-- Título principal -->
  <text x="40" y="80" class="rgb-title">Armando Fidel Lorea Sanchez</text>
  <text x="40" y="115" class="subtitle">Estudiante de Ingeniería en Sistemas Computacionales</text>

  <!-- Insertar Logos PNG en Base64 -->
  <image x="40" y="140" width="80" height="80" href="{logo_tlalocan}" />
  <image x="140" y="140" width="80" height="80" href="{logo_netbeans}" />
  <image x="240" y="140" width="80" height="80" href="{logo_visual}" />

  <!-- Texto de la terminal: Habilidades y Proyectos -->
  <text x="40" y="270" class="terminal-cmd">$ cat tech_stack.txt</text>
  <text x="40" y="300" class="terminal-text">Frontend: HTML5, CSS3, JavaScript (ES6+), WebGL (Three.js)</text>
  <text x="40" y="330" class="terminal-text">Backend &amp; Software: Java</text>
  <text x="40" y="360" class="terminal-text">Herramientas: VS Code, NetBeans, Git</text>

  <text x="40" y="410" class="terminal-cmd">$ ls projects/ --color=auto</text>
  <text x="40" y="440" class="terminal-text">Surreal_Mex.java    SkinsArts-Studio.js</text>
  
  <text x="40" y="490" class="terminal-cmd">$ ./play_music.sh</text>
  <text x="40" y="520" class="terminal-text">Now playing: guns.lol playlist 🎵</text>
  <text x="40" y="550" class="terminal-text">▶ S3RL - Bad Boy | Sefa - In De Hemel</text>

</svg>"""

# 4. Guardar el archivo generado en la carpeta assets
output_path = "assets/banner-dark.svg"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as file:
    file.write(svg_content)

print("¡Banner generado exitosamente en assets/banner-dark.svg! 🚀")