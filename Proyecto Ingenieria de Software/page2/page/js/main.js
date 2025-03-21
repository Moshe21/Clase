// Datos de ejemplo para los módulos
const MODULES = [
    {
        id: 1,
        title: 'Introducción a Casos de Uso',
        description: 'Aprende los fundamentos de la documentación de casos de uso, incluyendo la identificación de actores y la escritura de escenarios.'
    },
    {
        id: 2,
        title: 'Diagramas UML',
        description: 'Creación de diagramas UML para casos de uso, aprende a representar visualmente las interacciones del sistema.'
    },
    {
        id: 3,
        title: 'Metodologías Ágiles',
        description: 'Implementación de casos de uso en metodologías ágiles, integración con historias de usuario y criterios de aceptación.'
    }
];

document.addEventListener('DOMContentLoaded', function() {
    // Cargar módulos en la página principal
    const modulesList = document.getElementById('modulesList');
    if (modulesList) {
        MODULES.forEach(module => {
            const moduleHtml = `
                <div class="col-md-4">
                    <div class="module-card card h-100" data-module-id="${module.id}">
                        <div class="card-body">
                            <h3 class="card-title">
                                <i class="fas fa-book-reader mb-2"></i> ${module.title}
                            </h3>
                            <p class="card-text">${module.description}</p>
                            <a href="./module.html?id=${module.id}" class="btn btn-primary">
                                <i class="fas fa-arrow-right"></i> Ver módulo
                            </a>
                        </div>
                    </div>
                </div>
            `;
            modulesList.insertAdjacentHTML('beforeend', moduleHtml);
        });
    }

    // Navegación suave
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animaciones al hacer scroll
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.module-card, .feature, .activity-item');

        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight;

            if(elementPosition < screenPosition) {
                element.classList.add('animate-in');
            }
        });
    };

    // Inicializar animaciones
    document.querySelectorAll('.module-card, .feature, .activity-item').forEach(element => {
        element.classList.add('fade-up');
    });

    // Eventos de scroll
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll();

    // Manejo de módulos interactivos
    document.querySelectorAll('.module-card').forEach(module => {
        module.addEventListener('click', function(e) {
            if (!e.target.classList.contains('btn')) {
                const link = this.querySelector('.btn');
                if (link) {
                    link.click();
                }
            }
        });
    });
});