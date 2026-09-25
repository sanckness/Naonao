import streamlit as st
import streamlit.components.v1 as components

# Configuración de página de Streamlit
st.set_page_config(
    page_title="Para Nahomy • El Regalo Más Especial ✨",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inyección del código HTML, CSS y JS interactivo completo
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@400;600;700&family=Montserrat:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ff4d6d;
            --primary-light: #ff85a1;
            --accent: #ffb3c1;
            --gold: #f7d070;
            --bg-dark: #070509;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
        }

        body, html {
            width: 100%;
            height: 100vh;
            overflow: hidden;
            background: var(--bg-dark);
            font-family: 'Montserrat', sans-serif;
            color: #ffffff;
        }

        canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none;
        }

        /* BARRA DE NAVEGACIÓN SUPERIOR */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 20px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            background: linear-gradient(to bottom, rgba(7, 5, 9, 0.9), transparent);
        }

        .brand {
            font-family: 'Cinzel', serif;
            font-size: 1.1rem;
            letter-spacing: 4px;
            color: var(--accent);
            text-transform: uppercase;
        }

        .music-player-widget {
            display: flex;
            align-items: center;
            gap: 15px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 8px 20px;
            border-radius: 30px;
        }

        .music-btn {
            background: none;
            border: none;
            color: #fff;
            cursor: pointer;
            font-size: 0.8rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: all 0.3s;
        }

        .music-btn:hover {
            color: var(--primary-light);
        }

        /* CONTENEDOR PRINCIPAL MULTI-PÁGINA */
        .app-container {
            position: relative;
            z-index: 10;
            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .view-panel {
            position: absolute;
            width: 100%;
            max-width: 800px;
            padding: 45px 35px;
            background: rgba(18, 12, 24, 0.65);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border: 1px solid rgba(255, 182, 193, 0.2);
            border-radius: 32px;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.8), inset 0 1px 1px rgba(255, 255, 255, 0.2);
            text-align: center;
            opacity: 0;
            pointer-events: none;
            transform: translateY(30px) scale(0.96);
            transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .view-panel.active {
            opacity: 1;
            pointer-events: all;
            transform: translateY(0) scale(1);
        }

        /* ESTILOS DE TEXTO */
        .tagline {
            font-family: 'Cinzel', serif;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 6px;
            color: var(--primary-light);
            margin-bottom: 15px;
        }

        h1.title-large {
            font-family: 'Alex Brush', cursive;
            font-size: 4.5rem;
            line-height: 1.1;
            background: linear-gradient(135deg, #fff 0%, var(--primary-light) 50%, var(--accent) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
            text-shadow: 0 10px 40px rgba(255, 77, 109, 0.3);
        }

        p.description {
            font-size: 1.1rem;
            line-height: 1.8;
            color: rgba(255, 255, 255, 0.88);
            font-weight: 300;
            margin-bottom: 30px;
        }

        /* BOTONES DE ACCIÓN */
        .action-btn {
            background: linear-gradient(135deg, var(--primary) 0%, #c9184a 100%);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #ffffff;
            padding: 16px 40px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 4px;
            text-transform: uppercase;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 12px 35px rgba(255, 77, 109, 0.4);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            outline: none;
            margin: 10px 5px;
        }

        .action-btn:hover {
            transform: translateY(-4px) scale(1.03);
            box-shadow: 0 18px 45px rgba(255, 77, 109, 0.7);
            background: linear-gradient(135deg, var(--primary-light) 0%, var(--primary) 100%);
        }

        /* CONTADOR DE TIEMPO */
        .timer-grid {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 25px 0;
        }

        .timer-box {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 16px 20px;
            border-radius: 16px;
            min-width: 85px;
        }

        .timer-value {
            font-family: 'Cinzel', serif;
            font-size: 2rem;
            font-weight: 700;
            color: var(--gold);
        }

        .timer-unit {
            font-size: 0.65rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: rgba(255, 255, 255, 0.6);
            margin-top: 5px;
        }

        /* GALERÍA DE RAZONES */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 18px;
            margin: 25px 0;
            text-align: left;
        }

        .reason-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 182, 193, 0.15);
            padding: 20px;
            border-radius: 18px;
            transition: all 0.4s ease;
        }

        .reason-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.07);
            border-color: var(--primary-light);
        }

        .reason-icon {
            font-size: 1.6rem;
            margin-bottom: 10px;
        }

        .reason-title {
            font-family: 'Cinzel', serif;
            font-size: 0.95rem;
            color: var(--accent);
            margin-bottom: 6px;
        }

        .reason-desc {
            font-size: 0.85rem;
            line-height: 1.5;
            color: rgba(255, 255, 255, 0.75);
        }

        /* EFECTO MECANOGRAFÍA */
        .typewriter-text {
            min-height: 120px;
            font-size: 1.05rem;
            line-height: 1.9;
            color: rgba(255, 255, 255, 0.95);
            font-style: italic;
            text-align: left;
            background: rgba(0, 0, 0, 0.25);
            padding: 22px;
            border-radius: 16px;
            border-left: 3px solid var(--primary-light);
            margin-bottom: 25px;
        }

        @media (max-width: 650px) {
            h1.title-large { font-size: 3.2rem; }
            .timer-grid { gap: 8px; }
            .timer-box { min-width: 60px; padding: 10px 8px; }
            .timer-value { font-size: 1.3rem; }
            nav { padding: 15px 20px; }
            .view-panel { padding: 30px 20px; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="brand">N A H O M Y</div>
        <div class="music-player-widget">
            <button class="music-btn" onclick="toggleMusic()">🎵 <span id="music-text">Música</span></button>
            <button class="music-btn" onclick="changeTrack()">⏭️ Cambiar</button>
        </div>
    </nav>

    <canvas id="stage"></canvas>

    <audio id="audio-player" loop>
        <source src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=romantic-piano-112199.mp3" type="audio/mpeg">
    </audio>

    <div class="app-container">

        <!-- PANEL 1 -->
        <div class="view-panel active" id="panel-1">
            <div class="tagline">Una Experiencia Exclusiva</div>
            <h1 class="title-large">Hola, Mi Beba Hermosa</h1>
            <p class="description">
                Este espacio no es una página web común. Es un universo interactivo diseñado exclusivamente para recordarte lo infinitamente especial que eres para mí.
            </p>
            <button class="action-btn" onclick="goToPanel(2)">Comenzar el Viaje ✨</button>
        </div>

        <!-- PANEL 2 -->
        <div class="view-panel" id="panel-2">
            <div class="tagline">Capítulo I • Desde el Corazón</div>
            <h1 class="title-large">Una Promesa Incondicional</h1>
            <div class="typewriter-text" id="typewriter"></div>
            <button class="action-btn" onclick="goToPanel(3)">Continuar Experiencia ➔</button>
        </div>

        <!-- PANEL 3 (375 DÍAS) -->
        <div class="view-panel" id="panel-3">
            <div class="tagline">Capítulo II • El Tiempo a Tu Lado</div>
            <h1 class="title-large">Llevas Formando Parte De Mi Vida</h1>
            <p class="description">
                Cada día, hora y segundo que pasas en mi mundo es un regalo incalculable.
            </p>
            <div class="timer-grid">
                <div class="timer-box">
                    <div class="timer-value" id="days">375</div>
                    <div class="timer-unit">Días</div>
                </div>
                <div class="timer-box">
                    <div class="timer-value" id="hours">00</div>
                    <div class="timer-unit">Horas</div>
                </div>
                <div class="timer-box">
                    <div class="timer-value" id="minutes">00</div>
                    <div class="timer-unit">Minutos</div>
                </div>
                <div class="timer-box">
                    <div class="timer-value" id="seconds">00</div>
                    <div class="timer-unit">Segundos</div>
                </div>
            </div>
            <button class="action-btn" onclick="goToPanel(4)">Ver Razones Especiales ➔</button>
        </div>

        <!-- PANEL 4 -->
        <div class="view-panel" id="panel-4">
            <div class="tagline">Capítulo III • Por Qué Eres Mi Todo</div>
            <h1 class="title-large">Mis 3 Verdades</h1>
            <div class="cards-grid">
                <div class="reason-card">
                    <div class="reason-icon">💖</div>
                    <div class="reason-title">Mi Felicidad</div>
                    <div class="reason-desc">Al ser mi todo, te conviertes automáticamente en mi mayor fuente de paz y alegría diaria.</div>
                </div>
                <div class="reason-card">
                    <div class="reason-icon">🧩</div>
                    <div class="reason-title">Mi Complemento</div>
                    <div class="reason-desc">A tu lado encontré esa paz y complicidad única que encaja perfectamente con quien soy.</div>
                </div>
                <div class="reason-card">
                    <div class="reason-icon">🌹</div>
                    <div class="reason-title">Amor Incondicional</div>
                    <div class="reason-desc">A pesar de todo, de cualquier obstáculo o día difícil, yo te sigo amando y te amaré siempre.</div>
                </div>
            </div>
            <button class="action-btn" onclick="goToPanel(5)">Mensaje Final ❤️</button>
        </div>

        <!-- PANEL 5 -->
        <div class="view-panel" id="panel-5">
            <div class="tagline">Por Siempre y Para Siempre</div>
            <h1 class="title-large">Te Amo, Nahomy</h1>
            <p class="description">
                Gracias por existir, por ser exactamente como eres y por iluminar mi mundo. No hay código, regalo ni cifra que alcance para plasmar lo que vales.
            </p>
            <button class="action-btn" onclick="triggerFireworks()">Desatar Magia ✨</button>
        </div>

    </div>

    <script>
        const tracks = [
            "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=romantic-piano-112199.mp3",
            "https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8230560.mp3?filename=love-cinematic-piano-10709.mp3",
            "https://cdn.pixabay.com/download/audio/2021/09/06/audio_8b056e3012.mp3?filename=sweet-piano-romantic-6298.mp3"
        ];
        let currentTrack = 0;
        const player = document.getElementById('audio-player');
        const musicText = document.getElementById('music-text');

        function toggleMusic() {
            if (player.paused) {
                player.play();
                musicText.innerText = "Pausar";
            } else {
                player.pause();
                musicText.innerText = "Música";
            }
        }

        function changeTrack() {
            currentTrack = (currentTrack + 1) % tracks.length;
            player.src = tracks[currentTrack];
            player.play();
            musicText.innerText = "Pausar";
        }

        function goToPanel(panelNum) {
            if (player.paused && panelNum === 2) {
                toggleMusic();
            }

            document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
            setTimeout(() => {
                document.getElementById(`panel-${panelNum}`).classList.add('active');
                if (panelNum === 2) startTypewriter();
            }, 400);

            spawnBurst();
        }

        const cartaTexto = "A pesar de todo, de las distancias, de los momentos difíciles o de los días grises... yo te sigo amando y te amaré siempre. Porque eres mi todo, y al ser mi todo, te vuelves automáticamente mi felicidad, mi lugar seguro y mi complemento perfecto en esta vida.";
        let typewriterIndex = 0;
        let typewriterStarted = false;

        function startTypewriter() {
            if (typewriterStarted) return;
            typewriterStarted = true;
            const container = document.getElementById('typewriter');
            container.innerHTML = "";
            
            function type() {
                if (typewriterIndex < cartaTexto.length) {
                    container.innerHTML += cartaTexto.charAt(typewriterIndex);
                    typewriterIndex++;
                    setTimeout(type, 35);
                }
            }
            type();
        }

        const msPorDia = 1000 * 60 * 60 * 24;
        const fechaInicio = new Date(Date.now() - (375 * msPorDia));

        function updateTimer() {
            const ahora = new Date();
            const diferencia = ahora - fechaInicio;

            const dias = Math.floor(diferencia / msPorDia);
            const horas = Math.floor((diferencia / (1000 * 60 * 60)) % 24);
            const minutos = Math.floor((diferencia / 1000 / 60) % 60);
            const segundos = Math.floor((diferencia / 1000) % 60);

            document.getElementById('days').innerText = dias;
            document.getElementById('hours').innerText = horas < 10 ? '0' + horas : horas;
            document.getElementById('minutes').innerText = minutos < 10 ? '0' + minutos : minutos;
            document.getElementById('seconds').innerText = segundos < 10 ? '0' + segundos : segundos;
        }
        setInterval(updateTimer, 1000);
        updateTimer();

        const canvas = document.getElementById('stage');
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];

        function resize() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resize);
        resize();

        window.addEventListener('mousemove', (e) => {
            if (Math.random() > 0.4) {
                particles.push(new Particle(e.clientX, e.clientY, false));
            }
        });

        class Particle {
            constructor(x, y, isExplosion = false) {
                this.x = x || Math.random() * width;
                this.y = y || Math.random() * height;
                this.isExplosion = isExplosion;
                const angle = Math.random() * Math.PI * 2;
                const speed = isExplosion ? Math.random() * 8 + 2 : Math.random() * 1.5 + 0.3;
                
                this.vx = Math.cos(angle) * speed;
                this.vy = Math.sin(angle) * speed;
                this.alpha = 1;
                this.decay = isExplosion ? Math.random() * 0.02 + 0.01 : Math.random() * 0.008 + 0.003;
                this.size = isExplosion ? Math.random() * 5 + 2 : Math.random() * 3 + 1;
                this.color = ['#ff4d6d', '#ff85a1', '#ffb3c1', '#f7d070'][Math.floor(Math.random() * 4)];
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;
                if (this.isExplosion) this.vy += 0.04;
                this.alpha -= this.decay;
            }

            draw() {
                ctx.save();
                ctx.globalAlpha = Math.max(this.alpha, 0);
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }
        }

        for (let i = 0; i < 80; i++) particles.push(new Particle());

        function spawnBurst() {
            for (let i = 0; i < 40; i++) particles.push(new Particle(width / 2, height / 2, true));
        }

        function triggerFireworks() {
            for (let i = 0; i < 150; i++) particles.push(new Particle(width / 2, height / 2, true));
        }

        function animate() {
            ctx.fillStyle = 'rgba(7, 5, 9, 0.2)';
            ctx.fillRect(0, 0, width, height);

            for (let i = particles.length - 1; i >= 0; i--) {
                particles[i].update();
                particles[i].draw();
                if (particles[i].alpha <= 0) particles.splice(i, 1);
            }

            if (particles.length < 60) particles.push(new Particle());
            requestAnimationFrame(animate);
        }

        animate();
    </script>
</body>
</html>
"""

# Renderizar dentro de Streamlit usando HTML Component a pantalla completa
components.html(html_code, height=950, scrolling=False)
