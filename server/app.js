import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

const publicDir = path.join(__dirname, '../public');

// Servir archivos estáticos desde la carpeta public
app.use(express.static(publicDir));

// Ruta de fallback para servir el cliente
app.use((req, res) => {
  res.sendFile(path.join(publicDir, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`🎮 SupervivenciaGame corriendo en: http://localhost:${PORT}`);
});
