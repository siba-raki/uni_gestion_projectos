<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import AutorFuenteTable from './AutorFuenteTable.svelte';
    import AutorFuenteModal from './AutorFuenteModal.svelte';
    import AutorFuenteForm from './AutorFuenteForm.svelte';
    import Navbar from '../navbar/Navbar.svelte'

    let autores = [];
    let fuentes = [];
    let autor_fuentes = [];
    let autor_fuente_editada = null;

    onMount(async () => {
        await getAutorFuentes();
        await getAutores();
        await getFuentes();
    });

    async function getAutores() {
        try {
            autores = await getData('autores/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function getFuentes() {
        try {
            fuentes = await getData('fuentes/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function getAutorFuentes() {
        try {
            autor_fuentes = await getData('autor_fuentes/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deleteAutorFuente(id) {
        try {
            await deleteData(`autor_fuentes/${id}`);
            await getAutorFuentes();
        } catch (error) {
            console.error('Error al eliminar:', error);
        }
    }

    function showModal(autor_fuente) {
        autor_fuente_editada = autor_fuente;
    }

    function closeModal() {
        autor_fuente_editada = null;
    }
    console.log(autores)
</script>
<div>
    <Navbar />
    <AutorFuenteForm fuentes={fuentes} autores={autores} getAutorFuentes={getAutorFuentes}/>
    {#if autor_fuente_editada}
    <AutorFuenteModal fuentes={fuentes} autores={autores} autor_fuente={autor_fuente_editada} onClose={closeModal} getAutorFuentes={getAutorFuentes}/>
    {/if}
    <div class="container mx-auto w-1/2">
        <AutorFuenteTable autor_fuentes={autor_fuentes} onEdit={showModal} onDelete={deleteAutorFuente}/>
    </div>
</div>
