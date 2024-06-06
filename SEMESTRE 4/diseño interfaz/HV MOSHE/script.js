document.addEventListener('DOMContentLoaded', function() {
    const cvContainer = document.getElementById('cv');
  
    const cvContent = `
      <h2>Mi Nombre</h2>
      <h4>Desarrollador Web</h4>
      <p>Ubicación: Ciudad, País</p>
      <hr>
      <h4>Experiencia Laboral</h4>
      <p><strong>Empresa XYZ</strong> - Desarrollador Web - 2020-2022</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      <hr>
      <h4>Educación</h4>
      <p><strong>Universidad ABC</strong> - Licenciatura en Informática - 2016-2020</p>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      <hr>
      <h4>Habilidades Técnicas</h4>
      <p>HTML, CSS, JavaScript, Bootstrap</p>
    `;
  
    cvContainer.innerHTML = cvContent;
  });
  