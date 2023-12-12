<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import PersonaTable from './PersonaTable.svelte';
    import PersonaEditModal from './PersonaModal.svelte';
    import PersonaForm from './PersonaForm.svelte';
    import Navbar from '../navbar/Navbar.svelte';

    let personas = [];
    let personaEditada = null;

    onMount(async () => {
        await getPersonas();
    });

    async function getPersonas() {
        try {
            personas = await getData('personas/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deletePersona(id) {
        try {
            await deleteData(`personas/${id}`);
            await getPersonas();
        } catch (error) {
            console.error('Error al eliminar persona:', error);
        }
    }

    function showModal(persona) {
        personaEditada = persona;
    }

    function closeModal() {
        personaEditada = null;
    }
</script>
<div>
    <Navbar />
    <PersonaForm getPersonas={getPersonas}/>
    <div class="container mx-auto w-1/2">
        {#if personaEditada}
        <PersonaEditModal persona={personaEditada} onClose={closeModal} getPersonas={getPersonas}/>
        {/if}
        <PersonaTable {personas} onEdit={showModal} onDelete={deletePersona} />
    </div>
</div>
