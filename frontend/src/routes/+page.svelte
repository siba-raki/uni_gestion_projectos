<script>
  import Facultad from '../components/facultad/Facultad.svelte';
  import Navbar from '../components/Navbar/Navbar.svelte';
  import "../app.css";
</script>


<main>
  <Navbar />
  <Facultad />
</main>

<style>
  :global(body) {
      background: #e8e6e3;
    }
</style>
