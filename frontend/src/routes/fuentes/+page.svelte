<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import FuenteTable from './FuenteTable.svelte';
    import FuenteEditModal from './FuenteModal.svelte';
    import FuenteForm from './FuenteForm.svelte';
    import Navbar from '../navbar/Navbar.svelte';

    let fuentes = [];
    let tipoFuentes = [];
    let fuenteEditada = null;

    onMount(async () => {
        await getFuentes();
        await getTipoFuentes();
    });

    async function getFuentes() {
        try {
            fuentes = await getData('fuentes/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function getTipoFuentes() {
        try {
            tipoFuentes = await getData('tipo_fuentes/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deleteFuente(id) {
        try {
            await deleteData(`fuentes/${id}`);
            await getFuentes();
        } catch (error) {
            console.error('Error al eliminar fuente:', error);
        }
    }

    function showModal(fuente) {
        fuenteEditada = fuente;
    }

    function closeModal() {
        fuenteEditada = null;
    }
</script>
<div>
    <Navbar />
    <FuenteForm getFuentes={getFuentes} tipoFuentes={tipoFuentes}/>
    <div class="container mx-auto">
        {#if fuenteEditada}
        <FuenteEditModal fuente={fuenteEditada} onClose={closeModal} tipoFuentes={tipoFuentes} getFuentes={getFuentes}/>
        {/if}
        <FuenteTable {fuentes} onEdit={showModal} onDelete={deleteFuente}/>
    </div>
</div>
