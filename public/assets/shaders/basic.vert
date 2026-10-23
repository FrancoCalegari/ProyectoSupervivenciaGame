// Vertex Shader 2D básico
attribute vec2 a_position;
uniform vec2 u_resolution;

void main() {
  // Convertir posición de píxeles (0 a width, 0 a height) a clip space (-1.0 a +1.0)
  vec2 zeroToOne = a_position / u_resolution;
  vec2 zeroToTwo = zeroToOne * 2.0;
  vec2 clipSpace = zeroToTwo - 1.0;

  gl_Position = vec4(clipSpace * vec2(1, -1), 0, 1);
}
