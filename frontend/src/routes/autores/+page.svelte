<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import AutorTable from './AutorTable.svelte';
    import AutorModal from './AutorModal.svelte';
    import AutorForm from './AutorForm.svelte';
    import Navbar from '../navbar/Navbar.svelte'

    let autores = [];
    let personas = [];
    let autorEditada = null;

    onMount(async () => {
        await getAutores();
        await getPersonas();
    });

    async function getAutores() {
        try {
            autores = await getData('autores/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function getPersonas() {
        try {
            personas = await getData('personas/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deleteAutor(id) {
        try {
            await deleteData(`autores/${id}`);
            await getAutores();
        } catch (error) {
            console.error('Error al eliminar autor:', error);
        }
    }

    function showModal(autor) {
        autorEditada = autor;
    }

    function closeModal() {
        autorEditada = null;
    }
</script>
<div>
    <Navbar />
    <AutorForm personas={personas} getAutores={getAutores}/>
    {#if autorEditada}
    <AutorModal personas={personas} autor={autorEditada} onClose={closeModal} getAutores={getAutores}/>
    {/if}
    <div class="container mx-auto w-1/2">
        <AutorTable {autores} onEdit={showModal} onDelete={deleteAutor} />
    </div>
</div>
