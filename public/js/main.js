/**
 * Punto de entrada principal de la aplicación cliente (SupervivenciaGame).
 */

console.log('🧟 SupervivenciaGame inicializando...');

window.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('gameCanvas');
  if (!canvas) {
    console.error('No se encontró el elemento canvas #gameCanvas.');
    return;
  }

  // Intentar inicializar contexto WebGL (soporte para WebGL2 o WebGL estándar)
  const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
  if (!gl) {
    console.warn('WebGL no disponible, intentando contexto 2D para visualización...');
    initCanvas2DFallback(canvas);
    return;
  }

  console.log(`WebGL inicializado correctamente: ${gl.getParameter(gl.VERSION)}`);

  // Ajustar tamaño del canvas a la ventana
  function resize() {
    const dpr = window.devicePixelRatio || 1;
    const displayWidth = Math.floor(canvas.clientWidth * dpr);
    const displayHeight = Math.floor(canvas.clientHeight * dpr);

    if (canvas.width !== displayWidth || canvas.height !== displayHeight) {
      canvas.width = displayWidth;
      canvas.height = displayHeight;
      gl.viewport(0, 0, canvas.width, canvas.height);
    }
  }

  window.addEventListener('resize', resize);
  resize();

  // Bucle de renderizado inicial (Game Loop preliminar)
  let lastTime = performance.now();

  function gameLoop(currentTime) {
    const deltaTime = (currentTime - lastTime) / 1000;
    lastTime = currentTime;

    // Limpiar canvas con color ambiental oscuro
    gl.clearColor(0.06, 0.08, 0.1, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);

    requestAnimationFrame(gameLoop);
  }

  requestAnimationFrame(gameLoop);
});

function initCanvas2DFallback(canvas) {
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  function render2D() {
    ctx.fillStyle = '#0f141c';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#e6edf3';
    ctx.font = '20px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('WebGL no soportado - Modo Fallback 2D', canvas.width / 2, canvas.height / 2);
    requestAnimationFrame(render2D);
  }
  requestAnimationFrame(render2D);
}
