<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import FacultadTable from './FacultadTable.svelte';
    import FacultadEditModal from './FacultadModal.svelte';
    import FacultadForm from './FacultadForm.svelte';

    let facultades = [];
    let facultadEditada = null;

    onMount(async () => {
        await getFacultades();
    });

    async function getFacultades() {
        try {
            facultades = await getData('facultades/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deleteFacultad(id) {
        try {
            await deleteData(`facultades/${id}`);
            await getFacultades();
        } catch (error) {
            console.error('Error al eliminar facultad:', error);
        }
    }

    function showModal(facultad) {
        facultadEditada = facultad;
    }

    function closeModal() {
        facultadEditada = null;
    }
</script>
<div>
    <FacultadForm getFacultades={getFacultades}/>
    <div class="container mx-auto w-1/2">
        {#if facultadEditada}
        <FacultadEditModal facultad={facultadEditada} onClose={closeModal} getFacultades={getFacultades}/>
        {/if}
        <FacultadTable {facultades} onEdit={showModal} onDelete={deleteFacultad} />
    </div>
</div>
