document.addEventListener('DOMContentLoaded', function() {
    // Obtener el ID del módulo de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const moduleId = parseInt(urlParams.get('id'));

    if (!moduleId) {
        showError('ID de módulo no especificado');
        return;
    }

    // Verificar que MODULES esté disponible
    if (typeof MODULES === 'undefined') {
        showError('Error al cargar los datos del módulo');
        return;
    }

    // Encontrar el módulo correspondiente
    const module = MODULES.find(m => m.id === moduleId);

    if (!module) {
        showError('Módulo no encontrado');
        return;
    }

    // Actualizar el contenido de la página
    document.getElementById('moduleTitle').textContent = module.title;
    document.getElementById('moduleHeading').textContent = module.title;
    document.getElementById('moduleDescription').textContent = module.description;

    // Inicializar barra de progreso con animación
    setTimeout(() => {
        const progressBar = document.querySelector('.progress-bar');
        progressBar.style.width = '30%';
        progressBar.setAttribute('aria-valuenow', '30');
    }, 500);

    // Manejar interacciones con actividades
    document.querySelectorAll('.activity-item').forEach(item => {
        item.addEventListener('click', function() {
            this.classList.toggle('active');
            // Actualizar la barra de progreso cuando se completa una actividad
            updateProgress();
        });
    });
});

// Función para mostrar errores
function showError(message) {
    const container = document.querySelector('.container');
    container.innerHTML = `
        <div class="alert alert-danger mt-4" role="alert">
            <i class="fas fa-exclamation-circle"></i> ${message}
            <p class="mt-2">
                <a href="./index.html" class="btn btn-primary">
                    <i class="fas fa-home"></i> Volver al inicio
                </a>
            </p>
        </div>
    `;
}

// Función para actualizar el progreso
function updateProgress() {
    const activities = document.querySelectorAll('.activity-item');
    const completedActivities = document.querySelectorAll('.activity-item.active');
    const progressPercentage = (completedActivities.length / activities.length) * 100;

    const progressBar = document.querySelector('.progress-bar');
    progressBar.style.width = `${progressPercentage}%`;
    progressBar.setAttribute('aria-valuenow', progressPercentage);
}