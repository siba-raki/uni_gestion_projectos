<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import TipoFuenteTable from './TipoFuenteTable.svelte';
    import TipoFuenteEditModal from './TipoFuenteModal.svelte';
    import TipoFuenteForm from './TipoFuenteForm.svelte';
    import Navbar from '../navbar/Navbar.svelte';

    let tipoFuentes = [];
    let tipoFuenteEditada = null;

    onMount(async () => {
        await getTipoFuentes();
    });

    async function getTipoFuentes() {
        try {
            tipoFuentes = await getData('tipo_fuentes/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deleteTipoFuente(id) {
        try {
            await deleteData(`tipo_fuentes/${id}`);
            await getTipoFuentes();
        } catch (error) {
            console.error('Error al eliminar:', error);
        }
    }

    function showModal(tipoFuente) {
        tipoFuenteEditada = tipoFuente;
    }

    function closeModal() {
        tipoFuenteEditada = null;
    }
</script>
<div>
    <Navbar />
    <TipoFuenteForm getTipoFuentes={getTipoFuentes}/>
    <div class="container mx-auto w-1/2">
        {#if tipoFuenteEditada}
        <TipoFuenteEditModal tipoFuente={tipoFuenteEditada} onClose={closeModal} getTipoFuentes={getTipoFuentes}/>
        {/if}
        <TipoFuenteTable {tipoFuentes} onEdit={showModal} onDelete={deleteTipoFuente} />
    </div>
</div>
