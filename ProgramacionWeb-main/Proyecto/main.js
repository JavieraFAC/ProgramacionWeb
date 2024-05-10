
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




var modalContent = `
<div class="modal fade" id="profileModal" tabindex="-1" aria-labelledby="profileModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-body">
        <div class="container d-flex justify-content-center align-items-center">
          <div class="card">
            <div class="upper">
              <img src="https://i.imgur.com/Qtrsrk5.jpg" class="img-fluid">
            </div>
            <div class="user text-center">
              <div class="profile">
                <img src="https://i.imgur.com/JgYD2nQ.jpg" class="rounded-circle" width="80">
              </div>
              <h4 class="mb-0">Juan Perez</h4>
              <span class="text-muted d-block mb-2">Plan Semanal</span>
              <button class="btn btn-primary btn-sm follow">Ver perfil</button>
              <div class="d-flex justify-content-between align-items-center mt-4 px-4">
                <div class="stats">
                  <h6 class="mb-0">Almuerzos</h6>
                  <span>7</span>
                </div>
                <div class="stats">
                  <h6 class="mb-0">Saldo</h6>
                  <span>$14.123</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <!-- Podría usarse un botón para cerrar el modal -->
        <!--<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>-->
      </div>
    </div>
  </div>
</div>
`;

// Agrega el contenido del modal al contenedor
document.getElementById('modal-container').innerHTML = modalContent;