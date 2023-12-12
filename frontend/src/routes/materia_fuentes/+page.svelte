<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import MateriaFuenteTable from './MateriaFuenteTable.svelte';
    import MateriaFuenteModal from './MateriaFuenteModal.svelte';
    import MateriaFuenteForm from './MateriaFuenteForm.svelte';
    import Navbar from '../navbar/Navbar.svelte'

    let materias = [];
    let fuentes = [];
    let materia_fuentes = [];
    let materia_fuente_editada = null;

    onMount(async () => {
        await getMateriaFuentes();
        await getMaterias();
        await getFuentes();
    });

    async function getMaterias() {
        try {
            materias = await getData('materias/');
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

    async function getMateriaFuentes() {
        try {
            materia_fuentes = await getData('materia_fuentes/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deleteMateriaFuente(id) {
        try {
            await deleteData(`materia_fuentes/${id}`);
            await getMateriaFuentes();
        } catch (error) {
            console.error('Error al eliminar:', error);
        }
    }

    function showModal(materia_fuente) {
        materia_fuente_editada = materia_fuente;
    }

    function closeModal() {
        materia_fuente_editada = null;
    }
</script>
<div>
    <Navbar />
    <MateriaFuenteForm fuentes={fuentes} materias={materias} getMateriaFuentes={getMateriaFuentes}/>
    {#if materia_fuente_editada}
    <MateriaFuenteModal fuentes={fuentes} materias={materias} materia_fuente={materia_fuente_editada} onClose={closeModal} getMateriaFuentes={getMateriaFuentes}/>
    {/if}
    <div class="container mx-auto w-1/2">
        <MateriaFuenteTable materia_fuentes={materia_fuentes} onEdit={showModal} onDelete={deleteMateriaFuente} />
    </div>
</div>
