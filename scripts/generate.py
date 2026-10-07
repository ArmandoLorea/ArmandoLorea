import base64
import os

os.makedirs("assets", exist_ok=True)

# Función para incrustar PNGs sin perder calidad
def get_base64(ruta):
    if not os.path.exists(ruta):
        print(f"⚠️ Falta la imagen: {ruta}")
        return ""
    with open(ruta, "rb") as f:
        img_codificada = base64.b64encode(f.read()).decode('utf-8')
        return f"data:image/png;base64,{img_codificada}"

# Cargar tus logos
logo_tlalocan = get_base64("assets/tlalocan.png")
logo_netbeans = get_base64("assets/netbeans.png")
logo_visual   = get_base64("assets/visual.png")

# Dibujar el SVG con todo el texto en Rainbow
svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="850" height="550">
  <defs>
    <!-- Gradiente Rainbow Infinito -->
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
      .rainbow-text {{ font-family: 'Courier New', Courier, monospace; font-weight: bold; fill: url(#rainbow); }}
      .title {{ font-size: 34px; }}
      .subtitle {{ font-size: 20px; }}
      .terminal {{ font-size: 18px; }}
    </style>
  </defs>

  <!-- Fondo oscuro -->
  <rect width="100%" height="100%" fill="#0d1117" rx="15" />
  
  <!-- Controles de ventana -->
  <circle cx="30" cy="30" r="7" fill="#ff5f56" />
  <circle cx="55" cy="30" r="7" fill="#ffbd2e" />
  <circle cx="80" cy="30" r="7" fill="#27c93f" />

  <!-- Cabecera -->
  <text x="50%" y="70" class="rainbow-text title" text-anchor="middle">Armando Fidel Lorea Sanchez</text>
  <text x="50%" y="105" class="rainbow-text subtitle" text-anchor="middle">Estudiante de Ingeniería en Sistemas Computacionales</text>

  <!-- Logos -->
  <image x="325" y="130" width="200" height="100" href="{logo_tlalocan}" />
  
  <image x="280" y="250" width="120" height="60" href="{logo_netbeans}" />
  <image x="450" y="250" width="120" height="60" href="{logo_visual}" />

  <!-- Tech Stack -->
  <text x="50" y="380" class="rainbow-text terminal">$ cat tech_stack.txt</text>
  <text x="50" y="410" class="rainbow-text terminal">> Frontend: HTML5, CSS3, JavaScript (ES6+), WebGL (Three.js)</text>
  <text x="50" y="440" class="rainbow-text terminal">> Backend &amp; Software: Java</text>
  <text x="50" y="470" class="rainbow-text terminal">> Herramientas: VS Code, NetBeans, Git</text>
</svg>"""

with open("assets/banner-completo.svg", "w", encoding="utf-8") as file:
    file.write(svg_content)

print("¡Banner generado con éxito en assets/banner-completo.svg!")