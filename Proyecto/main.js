
const nav = document.querySelector("nav");


nav.innerHTML= `
<div class="container-fluid">
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="./Productos.html">Menus</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="./Planes.html" role="button" data-bs-toggle="dropdown">Planes </a>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="./Planes.html">Plan Diario </a></li>
          <li><a class="dropdown-item" href="./Planes.html">Plan Semanal</a></li>
          <li><a class="dropdown-item" href="./Planes.html">Plan Mensual</a></li>
        </ul>
      </li>
      <li class=" nav-item">
              <a class="nav-link" href="./Retaurantes.html">Restaurantes</a>
          </li>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="./Cuenta.html">Cuenta</a>
      </li>
      <li class="nav-item"><a class="nav-link" href="Carrito.html"> <img src="Imagenes/carrito.png" alt="cacerola"
            style="height: 25px; width: 25px;margin-left: 5px;"></a>
      <!-- Botón para abrir modal de perfil -->
      <li>
        <div class="container">
          <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#profileModal">Abrir
            Profile</button>
        </div>
      </li>
      </li>
    </ul>
  </div>
  
  <!-- Formulario de búsqueda -->
  <form class="d-flex">
    <input class="form-control me-2" type="text" placeholder="Buscar">
    <button class="btn btn-primary" type="button">Buscar</button>
  </form>
</div>
`;


