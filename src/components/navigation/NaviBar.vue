<script setup>
import NaviBarIcons from '/src/components/navigation/NaviBarIcons.vue'
</script>

<template>
  <div class="navbar-jsalv">
    <nav class="navbar navbar-dark bg-dark">
      <div class="d-flex align-items-center">
        <a class="navbar-brand navbar-title-jsalv ms-4" href="#">
          <RouterLink to="/">jsalv</RouterLink>
        </a>

        <div class="dropdown nav-dropdown">
          <button
            class="btn btn-secondary dropdown-toggle btn-sm"
            type="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Apps
          </button>
          <ul class="dropdown-menu larger-menu">
            <li class="app-dropdown-item">
              <RouterLink to="/">Home</RouterLink>
            </li>
            <li class="app-dropdown-item">
              <RouterLink to="/flags">Flags</RouterLink>
            </li>
            <li class="app-dropdown-item">
              <RouterLink to="/scene-starter">SceneStarter</RouterLink>
            </li>
            <li class="app-dropdown-item">
              <RouterLink to="/facial-expressions">Facial Expressions</RouterLink>
            </li>
            <li class="app-dropdown-item">
              <RouterLink to="/bass-practice">Bass Practice</RouterLink>
            </li>
            <li class="app-dropdown-item">
              <RouterLink to="/vocal-practice">Vocal Practice</RouterLink>
            </li>
            <li class="app-dropdown-item">
              <RouterLink to="/dance-practice">Dance Practice</RouterLink>
            </li>
            <li class="app-dropdown-item">
              <RouterLink to="/dice">Dice Roller</RouterLink>
            </li>
          </ul>
        </div>
      </div>

      <NaviBarIcons class="me-4" />
    </nav>
  </div>
</template>

<style>
.navbar-title-jsalv > * {
  font-size: 1.2rem;
  text-decoration: none !important;
  font-weight: bold !important;
  color: lightgray !important;
}

.app-dropdown-item {
  margin-left: 0.75rem;
  padding-bottom: 0.75rem;
}

.app-dropdown-item > a {
  font-size: 1.1rem;
  text-decoration: none !important;
  font-weight: bold !important;
}

.larger-menu {
  min-width: 14rem !important;
}
</style>
